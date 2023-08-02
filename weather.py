import requests
from datetime import datetime

key='key'
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

def itemsParser(items:dict):
    data={}

    for i in items:
        data[i['category']]=i['obsrValue']
    return data

def hourFormat(hour:int|str) -> str:
    _h=str(hour)
    if len(_h)==1:
        _h="0"+_h
    return _h

def getWeatherThen(date) -> dict:
    """
    result['hour']['category']
    INFO        CATE    VALUE
    *습도	    REH     92
    *1h 강수	RN1     0
    *1h 기온	T1H     24.9
    *풍향	    VEC     349
    """
    params ={
        'serviceKey' : key, 
        'pageNo' : '1', 
        'numOfRows' : '1000', 
        'dataType' : 'JSON', 
        'base_date' : date, 
        'base_time' : "0300", 
        'nx' : '51', 
        'ny' : '110' 
    }
    result={}
    
    for i in range(23):
        params['base_time']=f'{hourFormat(i+1)}00'
        response = requests.get(url, params=params)
        try:
            items=response.json()['response']['body']['items']['item']
            result[f'{i+1}']=itemsParser(items)
        except KeyError:
            result[f'{i+1}']=None
    return result

def getWeatherToday() -> dict:
    return getWeatherThen(datetime.now().strftime('%Y%m%d'))
