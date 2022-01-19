# 예외처리 - 가장중요!!!!!!!!!!!!!!!!!

from os import device_encoding
from tkinter import PIESLICE


def add(a,b):
    return a+b


def minus(a,b):
    return a-b


def multi(a,b):
    return a*b


def divide(a,b):
    return a/b

print('사칙연산시작')
a, b = 4, 1
numbers = [3, 6, 9]

try:
    print(f'나누기결과 : {divide(a, b)}')  # 예외발생
    res = int(numbers[1])*8
    num = int(input('수를 입력하세요'))

except ZeroDivisionError as e:
    print(f'예외발생! {e}')

except IndexError as e:
    print(f'인덱스 예외. 추가처리2 {e}')

except ValueError as e:
    print(f'숫자만 가능합니다')

except Exception as e:
    print(f'알 수 없는 예외. 추가처리3 {e}')

finally:
    print(f'곱하기결과: {multi(a,b)}')
    print(f'더하기결과: {add(a,b)}')
    print(f'빼기결과: {minus(a,b)}')



print('사칙연산종료')

