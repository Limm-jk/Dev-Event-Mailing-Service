import os
from datetime import datetime
from pytz import timezone
# from crawling_yes24 import parsing_beautifulsoup, extract_book_data
# from github_utils import get_github_repo, upload_github_issue
from github import Github

from crawling import crawling_event


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "event-autoMailing-Demo"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")
    
    title = f"오늘의 이벤트 - {today_data}"
    
    content = crawling_event()
    
    # repo에 접근
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    
    repo.create_issue(title=title, body=content)