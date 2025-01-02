# 스케쥴링? 특정시간에 작업을 예약하고 실행하는 프로세스
import schedule # 스케쥴
import time     # 시간
import requests # http 요청
from bs4 import BeautifulSoup # 파싱

def perform_web_crawling():
    response = requests.get("http://www.naver.com")
    soup = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

    # 매일 정해진 시간에 동작하도록 구현

schedule.every().day.at("09:44").do(job)

# 1분에 한번씩 크롤링
# schedul.every(1).minute.do(job)

while True :
    schedule.run_pending() # 대기중인 작업을 수행하는 함수
    time.sleep(1) # 1초동안 대기, cpu 사용량을 줄이기 위해서 사용
