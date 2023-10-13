import csv

import requests, json, csv
import pandas as pd
import googlemaps as gmaps
import time

# 도로명주소 위도경도변환
def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization":"KakaoAK 0cb3626cfd41cc904af909ce97391d0a"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    return api_json

test_data = pd.read_csv('df_drop.csv', encoding='utf-8')
test_data.head(6)

data = get_location('전라남도 진도군 신비의바닷길 74')
data['documents'][0]['x']

# 위도경도로 두 지점사이 거리계산
from numpy import sin, cos, arccos, pi, round


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees


def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians


def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2, unit='kilometers'):
    theta = longitude1 - longitude2

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )

    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)


def getfesdot(fesname):
    fes = pd.read_csv('C:\\Users\\j\\Documents\\카카오톡 받은 파일\\festival_좌표추가.csv')
    find = fes['축제명'] == fesname
    idx = fes[find]['좌표'].index

    x = float(fes[find]['좌표'][idx[0]].split(',')[0])
    y = float(fes[find]['좌표'][idx[0]].split(',')[1])
    return x,y

fes = pd.read_csv('C:\\Users\\j\\Documents\\카카오톡 받은 파일\\festival_좌표추가.csv')

with open('C:\\Users\\j\\Downloads\\sooncheon_gr_ps_V0.1.json', 'r', encoding='utf-8') as f:
    sooncheon = f.read()

data = json.loads(sooncheon)

print(len(data))
data[0]['x']
def getdistance(fesname):
    distance = []
    x_1, y_1 = getfesdot(fesname)
    for i in range(len(data)):
        x_2 = float(data[i]['y'])
        y_2 = float(data[i]['x'])
        distance.append(getDistanceBetweenPointsNew(x_1, y_1, x_2, y_2))
    return distance

getdistance('함평나비대축제')


getDistanceBetweenPointsNew(x,y, 34.2983013331782,126.527417390146)

