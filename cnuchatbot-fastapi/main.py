from fastapi import FastAPI
from fastapi.responses import JSONResponse

from common.model import KakaoRequest
from common.day import Day

from controller.shuttle import shuttleController as Shuttle
from controller.library import libraryController as Library
from controller.caferteria import cafeteriaController as Cafeteria
from controller.caferteria import hallController as Hall
from controller.information import informationController as Info


app = FastAPI()


# shuttle
@app.post("/shuttle/home")  # 도착 시간 정보
async def get_shuttle_time():
    json_info = Shuttle.get_time()
    return JSONResponse(json_info)


@app.post("/shuttle/image")  # 노선 이미지
async def get_shuttle_image(req: KakaoRequest):
    utter = req.userRequest.utterance  # A노선표 or B노선표 or C노선표
    json_info = Shuttle.get_image(utter)
    return JSONResponse(json_info)


# library
@app.post("/library/home")  # 도서관 시간 정보
async def get_library_time():
    json_info = Library.get_library_time()
    return JSONResponse(json_info)


@app.post("/library/seats")  # 열람실 좌석 현황
async def get_library_seats():
    json_info = Library.get_library_seats()
    return JSONResponse(json_info)


@app.post("/library/image")  # 도서관 층별 이미지
async def get_library_image():
    json_info = Library.get_library_image()
    return JSONResponse(json_info)


# cafeteria
@app.post("/cafeteria/home")
async def get_cafeteria_time():
    json_info = Cafeteria.get_cafeteria_time()
    return JSONResponse(json_info)


@app.post("/cafeteria/dorm/home")
async def get_dorm_options():  # 오늘 식단과 선택지(날짜)
    json_info = Cafeteria.get_dorm_menu(Day.TODAY.value)
    return JSONResponse(json_info)


@app.post("/cafeteria/dorm/menu")
async def get_dorm_menu(req: KakaoRequest):
    utter = req.userRequest.utterance  # 월요일기숙사, 화요일기숙사 ...
    kor_day = utter[:3]  # 월요일 ...
    json_info = Cafeteria.get_dorm_menu(Day.decode_kor_day(kor_day))
    return JSONResponse(json_info)


@app.post("/cafeteria/hall/home")
async def get_hall_options(req: KakaoRequest):  # 특정 회관에 맞는 선택 옵션(날짜)들과 오늘 식단
    utter = req.userRequest.utterance  # 제2학생회관, 제3학생회관, 제4학생회관, 생활과학대학
    json_info = Cafeteria.get_hall_menu(Day.TODAY.value, Hall.encode_place(utter))
    return JSONResponse(json_info)


@app.post("/cafeteria/hall/menu")
async def get_hall_menu(req: KakaoRequest):
    utter = req.userRequest.utterance  # 월요일제2학생회관 ... 월요일제3학생회관 ... 월요일생활과학대학
    kor_day = utter[:3]  # 월요일 ...
    place = utter[3:]  # 제2학생회관 ...
    json_info = Cafeteria.get_hall_menu(Day.decode_kor_day(kor_day), Hall.encode_place(place))
    return JSONResponse(json_info)

# information
@app.post("/information/global/event")
def get_global_event():
    json_info = Info.get_global_event()
    return JSONResponse(json_info)

@app.post('/information/global/recruit')
def get_global_recruit():
    json_info = Info.get_global_recruit()
    return JSONResponse(json_info)