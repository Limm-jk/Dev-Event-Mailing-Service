import requests
import os

from bs4 import BeautifulSoup
from datetime import datetime

def __main__():
    target_url = 'https://github.com/brave-people/Dev-Event'

    # url 객체 생성
    response = requests.get(target_url)

    #웹 소스코드 추출
    html = response.text
    
    # br을 기준으로 주제가 나뉨
    # <br>로 split한 arr기준 index 20부터 21년 1월
    br_HTML = list(html.split('<br>')[20:])   

    # print(br_HTML[0]) #소스코드 확인
    soup = BeautifulSoup(br_HTML[1], 'html.parser')
    links = soup.findAll("li")
    # print(links)
    event_arr = []
    for i in links:
        event_body = i.findAll("li")
        event_title = i.findAll("strong")
        if len(event_body) > 0:
            event_obj = event_title + event_body
            event_arr.append(event_obj)
        
    print(event_arr[0])

if __name__ == '__main__':
    __main__()