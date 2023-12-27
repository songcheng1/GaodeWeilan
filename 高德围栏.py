# -*- coding: utf-8 -*-
import requests

def get_administrative_boundary(key, keywords):
    url = "https://restapi.amap.com/v3/config/district"
    params = {
        "keywords": keywords,
        "key": key,
        "subdistrict": 1, # 是否显示下一级行政区域1(显示), 0(不显示)
        "extensions": "all",
    }
    response = requests.get(url, params=params)
    print(response.text, '\n\n\n')
    data = response.json()
    return data['districts'][0]["polyline"]


# 高德api_key
key = "xxxxxxxxxxxxxx"

# keywords 行政区域名全程或者对应的adcode
keywords = "上海"
# keywords = '闵行区'
keywords = '310112'

result = get_administrative_boundary(key, keywords)
# print(result)
