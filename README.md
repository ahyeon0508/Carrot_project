# Carrot_project
## About Project
&nbsp;&nbsp;&nbsp;본 프로젝트는 2020 공개SW개발자대회 출품작입니다.

### 1. 프로젝트 소개
&nbsp;&nbsp;&nbsp;현대화가 진행됨에 따라서 미래식량에 대한 고민은 나날이 증가하고 있다. 또한 고도의 산업화에 따라 젊은 층의 농업종사자비율은 감소세이며, 이에 농산품의 해외 수입의존도가 높아지고 있다.
농업 환경에서도 현재는 기계화된 장비들의 일부 도움이 있으나 상시 철저한 관리가 요구되는 일부 품종들에 대해 요구되는 생산량과 생산에 필요한 환경구축 자체에 다소 제약이 있는 실정이다.
위와 같은 상황을 개선하기 위하여 본 팀은 '지능적 농업 시스템을 통한 생산성 증가'라는 주제를 기반으로 AI를 통한 작물 재배 프로제트를 구성하였다.  
&nbsp;&nbsp;&nbsp;본 프로젝트에서는 재배 난이도가 높은 작물들을 대표하여 '당근'을 선택하여 당근 육성을 목표로 프로젝트를 진행하였다.  

### 2. 개발 환경 및 개발 언어
|| tool |
| ------ | ------ |
| 개발언어 | ![issue badge](https://img.shields.io/badge/python-3.6.11-blue.svg) ![issue badge](https://img.shields.io/badge/kotlin-1.3-yellowgreen) |
| 라이브러리 | ![issue badge](https://img.shields.io/badge/openCV-4.3.0-red) ![issue badge](https://img.shields.io/badge/pytorch-1.5.1%2Bcpu-orange) ![issue badge](https://img.shields.io/badge/Django-2.2.14-yellow.svg) |
| Open API | [OpenWeatherMAP API](http://zeldahagoshipda.com) |
| 개발환경 | Windows |
| 클라우드 환경 | [heroku](https://www.heroku.com/) |
| 데이터베이스 환경 | ![issue badge](https://img.shields.io/badge/SQL-postgreSQL-lightgrey.svg) |

### 3. 시스템 구성 및 아키텍쳐

 &nbsp;&nbsp;&nbsp;본 프로젝트는 하드웨어(라즈베리파이, 아두이노), API 서버, 모바일 앱(Android) 로 구성되어 있다.  
 각각의 기능은 아래와 같다.
 
 | 구성 | 역할 |
 | ------ | ------ |
 | 하드웨어 | 하우스 내에 설치 되어 하우스 내의 환경 데이터를 API 서버에 전송한다. |
 | API 서버 | 하드웨어로부터 하우스 환경 데이터를 전송받아 강화학습을 기반으로 하우스의 환경을 일정하게 유지하기 위한 행동(action)정보를 하드웨어로 전송한다. |
 | 모바일 앱 | 현재 하우스 내 상황과 날씨 정보를 보여준다. |
 
 
 
 &nbsp;&nbsp;&nbsp;프로젝트의 구조도는 아래와 같다.
 
 
 ![프로젝트 구조도](https://user-images.githubusercontent.com/42201356/103167936-ba0fc780-4872-11eb-9426-f56c07269cba.jpg)
 
 #### work flow
  1. 하우스 내 센서에 의한 재배 환경 데이터 추출
  2. 클라우드 서버로 데이터 전송
  3. 서버내 DB저장 및 AI기술에 의한 환경제어 피드백을 재해환경(하우스)에 송신
  4. 재배환경에 대한 DB데이터를 주기적으로 학습하여 AI최적화
  5. 전달된 피드백을 확인하고 해당 작업을 하우스가 수행
  6. 관리자는 하우스 환경상태를 앱으로 항시 확인 가능
  
  ## Usage
  ### 1. API 서버 url  
  http://carrot-project.herokuapp.com/
  
  #### API 서버 접속 후 화면
  <img src = "https://user-images.githubusercontent.com/42201356/103168410-5b4c4d00-4876-11eb-8399-acb8b336d74e.JPG" width="85%" height="85%" alt="API 서버 접속 후 화면">
  
  ### 2. API 서버 요청 스펙
  
  `GET /carrots/`: 하우스 내 모든 환경 데이터 기록을 json 리스트로 반환
  
  
  `POST /carrots/write` : 현재 하우스 내의 상태를 서버에 전달
  
  
  `GET /carrots/<int:pk>/` : 특정 시점의 하우스 환경 데이터 반환
  
  
  `UPDATE /carrots/<int:pk>/update/` : 특정 시점의 하우스 환경 데이터 수정
  
  
  `DELETE /carrots/<int:pk>/delete/` : 특정 시점의 하우스 환경 데이터 삭제
  
  `GET /carrots/current-status/` : 가장 최근의 하우스 환경 데이터 반환
  
  `GET /carrots/get-action/` : 최근 상태를 확인하여 하우스에 어떤 처리가 필요한지 반환
  
  
  ### 3. 안드로이드 어플리케이션 화면 예시
  
  
  <img src="https://user-images.githubusercontent.com/42201356/103171198-8c844780-488d-11eb-9bff-8b950817452f.jpg" width="40%" height="40%" alt="안드로이드 어플리케이션 화면 예시">
  
  ### 4. 시연 영상
  ⬇이미지 클릭
  
  
  <a href="https://youtu.be/tgzScbCC2yE"><img src="https://user-images.githubusercontent.com/42201356/103171761-1a623180-4892-11eb-8af6-e3b7b9981dc0.png" width="50%" height="50%"></img></a>
  
  ## Contributor
  + 서경대학교 컴퓨터공학부 이태학  
  + 숭실대학교 소프트웨어학부 김지헌
  + 숭실대학교 소프트웨어학부 변지현
  + 숭실대학교 소프트웨어학부 이아현
