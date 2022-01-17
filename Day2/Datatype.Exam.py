# 자료형
from platform import python_branch
from typing import Tuple
from unicodedata import name


print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))


# 숫자형
# 기본적으로 정수형 int와 실수형 float 입니다.

금액 = 12_345_666
print(금액)
bruce_eckel = 'Life is short, you need python'
print(bruce_eckel)
bruce_eckel = "Life is short, you need python"
print(bruce_eckel)
bruce_eckel

bruce_eckel = "Life is short.\nYou need python" #한줄띄울때 "\n" 써주면됨//
print(bruce_eckel)

bruce_eckel = "Life is short.\\You need python" #'\'를 문자로 표현하고 싶을때 "\\" 표기//
print(bruce_eckel)

bruce_eckel = '''Life is short.\\You need python
파이썬이뭐라고
진짜영화''' #여러줄의 문자열을 써야할 경우 '''를 써서 표기//
print(bruce_eckel)

# 불형
val_sum = 1000
print(val_sum == 1000)  #True가나옴
print(val_sum == 9)  #False가나옴

bl_true = True
print(type(bl_true))
print(bl_true == True) #"=="로 참거짓 확인//
print(bl_true is True) #참거짓 확인시 "is"를 써도 가능//

print(a is None)
print(val_sum is 1000)

# 의미가 있는 bool
print(bool(1)) #boll=1 True
print(bool(0)) #bool=2 False

# 복합형 - 리스트
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)

#b = [i for i in range(54000)]  #이런방법도 있는데 나중에 한다고하심//
#print(b)

arr2 = ['Life', 'is', 'short', 'you', 'need', 'python', 3]
print(arr2)

arr3 = [[1,2,3],[4,5,6]]
print(arr3)

# 빈 리스트 생성 
arr4 = list()
print(arr4)  #[]로 출력됨, None이아님


# 튜플 () 사용 - 편집이불가
Tuple1 = (1, 2, 3, 4)
print(Tuple1)

# 딕셔너리
spiderman = {'name' : '피터파커',
             'age' : 18,
             'weapon' : '웹슈터'}

print(spiderman)  ##전체정보가 다 나옴 as {'name': '피터파커', 'age': 18, 'weapon': '웹슈터'}
print(spiderman['name'])  ##as 피터파커


# 집합
sel_int = set([1,2,3,4,5,4,6,7,1,2,2])
print(sel_int) ##중복제거됨 as {1, 2, 3, 4, 5, 6, 7}

