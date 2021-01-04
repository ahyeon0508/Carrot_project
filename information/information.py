import json
import requests
import serial
from tracking import *
from time import sleep
import math

arduino = serial.Serial('COM3', 9600)


while True:
    # 이미지 주소
    imgSrc = "./2.jpg"

    # 당근 상태 값으로 받아오기
    stateValue = 0
    stateList = []

    stateList.append(yellowOrange_tracking(imgSrc))
    stateList.append(white_tracking(imgSrc))
    stateList.append(darkBrown_tracking(imgSrc))
    stateList.append(black_tracking(imgSrc))

    for i in range(4):
        if stateList[i] != 0:
            stateValue = stateList[i]
            break


    # 아두이노 센서값 받아오기
    a = arduino.readline()
    a = a.decode()
    a = json.loads(a)


    # 온도
    count = 0
    temperature = float(a.get('tempvalue'))
    if count == 0 and math.isnan(temperature): # 첫 관측시기에 온도값이 NaN일 경우
        temperature = 0
        count += 1
    elif math.isnan(temperature):           # 성장 도중 관측시 온도값이 NaN일 경우
        temperature = temp
        count += 1
    else:                                   # 온도값이 정상으로 출력될 경우
        temp = temperature
        count += 1


    # 수분
    wetness = float(a.get('moisture'))
    if wetness > 950:                      # 수분이 부족한 상태
        wetness = 0
    elif 850 < wetness <= 950:
        wetness = 1
    elif 750 < wetness <= 850:
        wetness = 2
    elif 650 < wetness <= 750:
        wetness = 3
    elif 550 < wetness <= 650:
        wetness = 4
    elif 450 < wetness <= 550:
        wetness = 5
    elif 350 < wetness <= 450:
        wetness = 6
    else:                                   # 수분이 충분한 상태
        wetness = 7


    # json 형식으로 전달
    result = {'temperature': temperature, 'wetness' : wetness, 'end_status' : stateValue}
    response = requests.post(url="https://carrot-project.herokuapp.com/carrots/write/", data=json.dumps(result), headers={'Content-Type': 'application/json'})

    # 당근이 노란색/주황색을 띄면 종료
    if stateValue == 100:
        break
    else:
        sleep(3600)