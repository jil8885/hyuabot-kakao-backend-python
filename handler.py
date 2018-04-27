from food.food_main import make_string_food
from transport.shuttle_main import shuttle_main
from transport.subway import subway_seoul, subway_erica
from transport.bus import bus_request
import sqlite3


button_list = ["학식", "교통", "날씨", "기타 기능", "캠퍼스 변경"]
seoul_cafeteria_list = ["학생식당", "교직원식당", "사랑방", "신교직원식당", "제1생활관식당",  "제2생활관식당", "행원파크", "처음으로"]
erica_cafeteria_list =  ["학생식당", "교직원식당", "푸드코트", "창업보육센터", "기숙사식당", "처음으로"]
destination_list = ['시내', '강남', '수원/성남', '처음으로']

def handler(content, campus = 1):
    global button_list, seoul_cafeteria_list, erica_cafeteria_list
    if content == "학식":
        string = "식단을 알고 싶은 식당을 선택해주세요."
        if campus == 1:
            button_list = erica_cafeteria_list
        else:
            button_list = seoul_cafeteria_list
    elif content in seoul_cafeteria_list[:-1]:
        button_list = seoul_cafeteria_list
        string = make_string_food(content, campus)
    elif content in erica_cafeteria_list[:-1]:
        button_list = erica_cafeteria_list
        string = make_string_food(content, campus)
    elif content == "교통":
        if campus == 1:
            string = '원하시는 서비스를 선택해주세요.'
            button_list = ['버스', '지하철', '셔틀버스','처음으로']
        else:
            string = subway_seoul()
            button_list = ["학식", "교통", "날씨", "기타 기능", "캠퍼스 변경"]
    elif content == "셔틀버스":
        string = '시간표를 알고 싶은 정류장을 선택해주세요.'
        button_list = ['셔틀콕', '한대앞역', '예술인A', '기숙사', '처음으로']
    elif content == "셔틀콕":
        string = '셔틀콕 >> 한대앞\n'
        string += shuttle_main('shuttleA', 'toSubway') + '\n\n'
        string += '셔틀콕 >> 예술인A\n'
        string += shuttle_main('shuttleB', 'toTerminal') + '\n\n'
        string += '셔틀콕 >> 한대앞 >> 예술인A\n'
        string += shuttle_main('shuttleA', 'cycle')
    elif content == "한대앞역":
        string = shuttle_main('subway')
    elif content == "예술인A":
        string = shuttle_main('terminal')
    elif content == "기숙사":
        string = shuttle_main('dorm')
    elif content == "지하철":
        button_list = ['버스', '지하철', '셔틀버스', '처음으로']
        string = subway_erica()
    elif content == "버스":
        button_list = destination_list
        string = '원하시는 분류를 선택해주세요.'
    elif content in destination_list[:-1]:
        button_list = ['버스', '지하철', '셔틀버스', '처음으로']
        string = bus_request(content)
    elif content == "처음으로":
        button_list =   ["학식", "교통", "날씨", "기타 기능", "캠퍼스 변경"]
        string = "처음으로 돌아갑니다."
    else:
        string = content
    return string, button_list