# 웹페이지 긁어오기
# from urllib.request import Request, urlopen

# req = Request ('http://www.naver.com')
# res = urlopen(req)
# print(res.status)  #결과값 200 나옴, 웹페이지를 찾았단 내용 (404 : web page not found)

# 외부 Request 패키지 추가 설치
# PIP Install Requests

import requests 
url = 'http://www.naver.com'
res = requests.get(url)

# print(res.status_code)
print(res.text)
