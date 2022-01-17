# 연산자
from os import stat
from tkinter import CURRENT


a = 11
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 문자열연산
# 문자열 빼기 나누기 곱하기(문자열X문자열) 없음 FYI.문자열X5는 가능 
stat1 = 'hello' 
stat2 = 'world'
print(stat1, stat2)  #as hello world
print(stat1+stat2)  #as helloworld

res = stat1, stat2  #튜플 as ('hello', 'world')
print(res)

res = stat1+ stat2  #as helloworld
print(res)
print(stat1*5)  #as hellohellohellohellohello


# 문자열 길이
print(len(stat1))
stat3 ='안녕하세요?'
print(len(stat3)) #6

# 문자열 인덱스, 리스트와 동일한 작업
# print(stat3[0])  #as 안
# print(stat3[1])  #as 녕
# print(stat3[2])  #as 하
# print(stat3[5])  #as ? FYI. [6]이면 오류남//

###################### 단축키 : 선택 후 Ctrl + / 전체 주석처리 & 해제는 한번 더

print(stat3[-1])  #as ? 마이너스는 역순으로 길이 계산
print(stat3[-6])  #as 안

stat4 = "저리가" + stat3[3:]
print(stat3,stat4)  #as 저리가세요?


# 문자열 자르기
일시 = '2022-01-17 14:39:35'

print(일시[0:4],'년')  #년도만 자르기 : 0:4로 해줘야 2022 나옴
print(일시[:4],'년')  #0생략해도 가능

print(일시[5:7],'월')  
print(일시[8:10],'일')  
print(일시[11:13],'시')  
print(일시[14:16],'분')  
print(일시[17:19],'초')  
print(일시[17:],'초')  #마지막 글자수 생략가능


print(일시[-5:-3],'분')  
print(일시[-6:-1])

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a)  #as [1, 19, 3, 4, 5]

# 문자별 포맷팅
str1 = "I'm so happy {0} U. are {1}?". format('to', 'you')  #{0}=변수 as I'm so happy to U. are you?
print(str1)

첫번째 ='투'
두번째 ='유'
str1 = "I'm so happy {0} U. are {1}?". format(첫번째, 두번째)  #as I'm so happy 투 U. are 유?
print(str1)

### 75-78 & 82-83 같은거!!!!!!!!!!!!!!!!!!!!

str2 =f"I'm so happy {첫번째} U. are {두번째}?"  #as I'm so happy 투 U. are 유?
print(str2)


## 숫자 천단위 콤마
money = 10000000000000000000000000000000000000
print(format(money,',d'))

from datetime import datetime
now=datetime.now() #현재일시생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math
myPi = math.pi
print(myPi)

print('{0}'.format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}')

full_name = 'Hugo MG Sung'
age = 47
greeting = '''안녕하세요. 저는 {0}입니다. 
나이는 {1}살 이구요.'''.format(full_name, age)
print(greeting)

greeting = f'''안녕하세요. 저는 {full_name}입니다. 
나이는 {age:0.2f}살 이구요.'''  #as 안녕하세요. 저는 Hugo MG Sung입니다. 나이는 47.00살 이구요.
print(greeting)

part_name = full_name.split()
print(part_name)  #as ['Hugo', 'MG', 'Sung']
print(type(part_name))  ##타입 : <class 'list'>


test = 'hey, guys'
print(test.split(','))  #as ['hey', ' guys']

# |(파이프)로 SPLIT
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)

# 단어교체 REPLACE
print(full_name.replace('Hugo MG', 'Ashley'))

# STRIP == ORACLE TRIM과 동일
aaa = '    Hello, world   '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())


# 문자열 단어 찾기 INDEX / COUNT
print(full_name.index('H'))  #as 0 (Hugo 첫번째)
print(full_name.index('u'))  #as 1 (Hugo 두번째) / 대소문자구문함
print(full_name.count('u'))  #as 2 (Hugo Sung 총 두개)


# FIND 
print(full_name.find('X'))  #as -1 == 이름에 X가 없다는뜻이라고함
print(full_name.find('MG'))  #as 5 (Hugo MG 순서대로) 

# 문자열 내에 특정 문자 및 문자열을 추가하는 join()
print('.'.join(full_name))  #값: H.u.g.o. .S.u.n.g
print('--'.join(full_name)) #값: H--u--g--o-- --S--u--n--g


# 글자를 모두 대문자로 변경하는 upper()와 소문자로 변경하는 lower()
print(full_name.upper())  #값: 'HUGO SUNG'
print(full_name.lower())  #값: 'hugo sung'








