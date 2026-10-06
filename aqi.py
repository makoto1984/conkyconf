#!/usr/bin/python3

import os
import requests
import json

def aqicolor(aqivalue):
    if aqivalue <= 50:
        return 'green'
    elif aqivalue <= 100:
        return 'yellow'
    elif aqivalue <= 150:
        return 'orange'
    else:
        return 'red'

def windcolor(wind_speed):
    if wind_speed > 32.6:
        return 'red'
    elif wind_speed > 24.4:
        return 'orange'
    elif wind_speed > 17.1:
        return 'yellow'
    elif wind_speed > 10.7:
        return 'blue'
    else:
        return 'white'

token="TOKEN HERE"
res=requests.get("https://api.waqi.info/feed/beijing/chaoyangaotizhongxin/?token="+token)
data=json.loads(res.text)
aqivalue=data['data']['aqi']
dominant=data['data']['dominentpol']
pm25=data['data']['iaqi']['pm25']['v']
pm10=data['data']['iaqi']['pm10']['v']
o3=data['data']['iaqi']['o3']['v']
no2=data['data']['iaqi']['no2']['v']
so2=data['data']['iaqi']['so2']['v']
co=data['data']['iaqi']['co']['v']
temp=data['data']['iaqi']['t']['v']
baro=data['data']['iaqi']['p']['v']
humid=data['data']['iaqi']['h']['v']
wind=data['data']['iaqi']['w']['v']

print("${color white}${alignc}北京市\n")
print("${alignc}AQI: ${color "+aqicolor(aqivalue)+"}"+str(aqivalue)+"\t${color white}"+dominant+"\n")
print("PM2.5: "+str(pm25)+"\tPM10: "+str(pm10)+"\tO3 : "+str(o3)+"\nNO2: "+str(no2)+"\tSO2: "+str(so2)+"\tCO: "+str(co)+"\n")
print("湿度: "+str(humid)+"%\t気圧: "+str(baro)+"hPa\n温度: "+str(temp)+"℃\t風: ${color "+windcolor(wind)+"}"+str(wind)+"m/s${color white}\n")
