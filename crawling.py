import requests
import os

from bs4 import BeautifulSoup
from datetime import datetime

def split_day(body):
    """
    output = arr
    arr[0] = month
    arr[1] = date
    arr[2] = month&date(for sort)
    """
    str_body = str(body)
    split_str = str_body.split('.')
    """
    expected
    '<li>신청: 02', ' 04(목) 14:00 / 02', ' 05(금) 14:00</li>'
    """
    month = split_str[-2][-2:]
    day = split_str[-1][1:3]
    MnD = month + day
    return [month,day,MnD]
    
def crawling_event():
    target_url = 'https://github.com/brave-people/Dev-Event'

    # url 객체 생성
    response = requests.get(target_url)

    #웹 소스코드 추출
    html = response.text
    
    # br을 기준으로 주제가 나뉨
    # <br>로 split한 arr기준 index 20부터 21년 1월
    br_HTML = list(html.split('<br>')[20:])   

    # print(br_HTML[0]) #소스코드 확인
    soup = BeautifulSoup(br_HTML[0], 'html.parser')
    events = soup.findAll("li")
    # print(links)
    
    current_content = ''
    for i in events:
        event_body = i.findAll("li")
        event_title = i.find("strong")
        if len(event_body) > 0:
            link = event_body[3].select("a")[0].attrs['href']
            due_date = split_day(event_body[2])
            # event_info = [event_title.text, link]
            # event_info = event_info + split_day(event_body[2])
            # content = f"<a href={link}> " + event_title.text + "</a>" + " / 마감 일자 : " + due_date[0] + "월 " + due_date[1] + "일 <br/>\n"
            content = f"[{event_title.text}]({link})" + "\n -마감 일자 : " + due_date[0] + "월 " + due_date[1] + "일\n -"+ event_body[1].text + " <br/>\n "
            current_content += content
            
        
    return current_content

def __main__():
    print(crawling_event())

if __name__ == '__main__':
    __main__()
