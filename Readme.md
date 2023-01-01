# 이벤트 크롤러

*Dev-Event* 저장소를 이용합니다. 항상 감사합니다.

### Crawling 접근
큰 주제는 br을 기준으로 나누어 진다는 점을 생각하여 크롤링한 html 데이터를 <br>으로 스플릿
```python
#웹 소스코드 추출
html = response.text
    
# br을 기준으로 주제가 나뉨
# <br>로 split한 arr기준 index 20부터 21년 1월
br_HTML = list(html.split('<br>')[20:])
```

이벤트가 li태그에 묶여있음. 하지만, findAll을 사용하면 li의 내부에도 li를 사용하여 중복 검색 됨.  
-> findAll('li')의 결과에 한번 더 findAll을 사용하여 필요한 것만 추출
```python
links = soup.findAll("li")

for i in links:
        event_body = i.findAll("li") # 리스트로 묶여있는 행사 정보
        event_title = i.findAll("strong") # 행사 title
        if len(event_body) > 0:
            event_obj = event_title + event_body
            event_arr.append(event_obj)
```

 
