# 부산버스 노선별 이용건수
import csv
from re import S

file_name = '부산버스.csv'
f = open('부산버스.csv', mode = 'r', encoding='utf-8')

reader = csv.reader(f, delimiter=',')  #구분자가 , 일 경우
next(reader) #헤더없애줌

for line in reader:
    print(line)

f.close()

