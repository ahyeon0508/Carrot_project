import numpy as np
import cv2
from sklearn.cluster import KMeans

# 색상 범위 설정
lower_yellowOrange = (80, 100, 100)
upper_yellowOrange = (140, 255, 255)
lower_white = (-10, 0, 255)
upper_white = (10, 0, 255)
lower_darkBrown = (100, 100, 40)
upper_darkBrown = (120, 148, 69)
lower_black = (-10, 0, 0)
upper_black = (10, 0, 0)


# 각컬러의 분율 확인
# https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/ 제공
def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def color_processing(img, lower_color, upper_color):
    # BGR to HSV 변환
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 색상 범위를 제한하여 mask 생성
    img_mask = cv2.inRange(img_hsv, lower_color, upper_color)

    # 원본 이미지를 가지고 Object 추출 이미지로 생성
    img_result = cv2.bitwise_and(img, img, mask=img_mask)

    # height, width 통합
    image = img_result.reshape((img_result.shape[0] * img_result.shape[1], 3))

    return image

def yellowOrange_tracking(imgSrc):
    # 이미지 파일을 읽어온다
    img = cv2.imread(imgSrc)

    # 컬러 추적
    image = color_processing(img, lower_yellowOrange, upper_yellowOrange)

    # 클러스터링
    k = 2
    clt = KMeans(n_clusters=k)
    clt.fit(image)

    hist = centroid_histogram(clt)

    try:
        if hist[1] > 0:
            return 100
    except IndexError:
        return 0

def white_tracking(imgSrc):
    # 이미지 파일을 읽어온다
    img = cv2.imread(imgSrc)

    # 흰색 컬러 추적
    image = color_processing(img, lower_white, upper_white)

    # 클러스터링
    k = 2
    clt = KMeans(n_clusters=k)
    clt.fit(image)

    hist = centroid_histogram(clt)

    try:
        if hist[1] > 0:
            return 300
    except IndexError:
        return 0

def darkBrown_tracking(imgSrc):
    # 이미지 파일을 읽어온다
    img = cv2.imread(imgSrc)

    # 짙은 갈색 컬러 추적
    image = color_processing(img, lower_darkBrown, upper_darkBrown)

    # 클러스터링
    k = 2
    clt = KMeans(n_clusters=k)
    clt.fit(image)

    hist = centroid_histogram(clt)

    try:
        if hist[1] > 0:
            return 301
    except IndexError:
        return 0

def black_tracking(imgSrc):
    # 이미지 파일을 읽어온다
    img = cv2.imread(imgSrc)

    # 흑색 컬러 추적
    image = color_processing(img, lower_black, upper_black)

    # 클러스터링
    k = 2
    clt = KMeans(n_clusters=k)
    clt.fit(image)

    hist = centroid_histogram(clt)

    try:
        if hist[1] > 0:
            return 301
    except IndexError:
        return 0