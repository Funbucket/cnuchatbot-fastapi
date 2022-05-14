<h1 align="center">Welcome to CNU(츠누) Bot 👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Funbucket/cnuchatbot-fastapi" target="_blank">
  </a>
  <a href="https://github.com/Funbucket/cnuchatbot-fastapi" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" />
  </a>  
</p>

<p align="center">
<img alt="character" width="300" src="https://github.com/Funbucket/cnuchatbot-fastapi/blob/main/assets/char.jpg" />

</p>

### 🔑 채널 아이디 : cnubot

### 📷 Qr 코드

<img alt="Qr코드" width="200" height="200" src="https://github.com/Funbucket/cnuchatbot/blob/master/image/qrcode.png"/>

<br><br>

## 📜 사용방법

<img alt="사용방법" height="500" src="https://github.com/Funbucket/cnuchatbot/blob/master/image/KakaoTalk_20210301_223747528.gif"/>

- <b>츠누봇 시작하기</b>

  - <b>👉학식 : [기숙사식당 , 제1학생회관, 제2학생회관, 제3학생회관] 식단 및 운영 시간 </b>
  - <b>👉셔틀 : [A노선 , B노선 , C노선] 정류장별 버스 잔여시간 및 노선표</b>
  - <b>👉열람실 : 도서관 층별지도보기 및 열람실 총 좌석 , 잔여좌석 운영여부 </b>
  - <b>👉알뜰정보 : 최신 학사정보, 최신 문화정보 , 각종 충남대학교 전화번호 </b>

## 📚 출처

- 1번 공휴일 판별
  - [공공데이터포털](https://www.data.go.kr/data/15012690/openapi.do)
- 2번 KaKao OpenBuilder i JsonFormat
  - [jil8885](https://github.com/jil8885/django-kakao-i-hanyang/blob/gcloud/common/sender.py)

## 🖋 co-development

👤 Chanhyuk Park

- Mail: [chanhyuk-tech@kakao.com](mailto:chanhyuk-tech@kakao.com)
- GitHub: [@PARKCHANHYUK](https://github.com/ChanhyukPark-Tech)

👤 Haechang Joe

- Mail: [ouchc@icloud.com](mailto:ouchc@icloud.com)
- GitHub: [@JOEHAECHANG](https://github.com/Funbucket)

## 📝 License

Copyright © 2021 [조해창](https://github.com/Funbucket) [박찬혁](https://github.com/ChanhyukPark-Tech).<br/>
FeedBack ---- > https://open.kakao.com/o/sm0C6bZc
This project is [MIT](https://github.com/Funbucket/cnuchatbot/blob/master/LICENSE) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

## 프로젝트 실행하기(Windows)

> 가상환경 설치하기

    $ python -m venv venv

> 가상환경 실행하기

    $ source venv/bin/activate

> Django 설치하기

    $ pip install django

> 데이터베이스 적용하기 (manage.py 파일이 있는 곳에서 명령어 치기)

    $ python manage.py makemigrations
    $ python manage.py migrate

> admin에 접속했을때 사용할 슈퍼유저 만들기

    $ python manage.py createsuperuser

> 프로젝트 실행해보기

    $ python3 manage.py runserver

> 가상환경 종료하기

    $deactivate
