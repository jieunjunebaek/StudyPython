# 함수 선언 및 사용

# 더하기 함수 사용
from dataclasses import replace


def add(a, b):
    res= a + b
    return res

# 함수 사용
print(add(25757, 477527588))

mid_val = add(3,4)
print(mid_val *3)


# 매개변수 영어로는 parameter 또는 arguments 라고 하는 수학의 함수 f(x)에서 x 를 의미합니다. 

# 함수종류
# 1. 입력값(매개변수)가 없는 형태
def say_hello():
    return "Hello~"

print(say_hello())  #rkqt : Hello~
print(say_hello(),'my dear')  #rkqt : Hello~ my dear

val = say_hello()
print(val.replace('o~', ''))  #rkqtr : Hell

# 2. 결과값이 없는 형태
def say_hello(name):
    print(f'Hello~ {name}')
    return None  #None을 리턴하는거라 생략가능

say_hello('Hugo') #rkqt : Hello~ Hugo

# 3. 둘다 없는 형태
def say_goodbye():
    print('Bye bye~')

say_goodbye()  #역시 리턴값 생략됨

# 4. 매개변수를 지정하는 형태
def multi(x, y):
    return x * y

print(multi(x = 8, y = 4))
print(multi(8, 4))

# 5. 매개변수 개수가 일정하지 않는 형태
def plus(*args):  #args = arguments의 약어
    res = 0
    for i in args:
        res += i
    return res

print(plus(1, 2, 3, 4))
print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 6. 함수 결과가 하나 이상인 형태
def mul_and_div(x, y):
    mul = x * y
    div = x / y
    return (mul, div)  #튜플

(res1, res2) = mul_and_div(7,8)
print(res1, res2)


def cal(x, y):
    return (x+y, x-y, x*y, x/y)
    
res1, res2, res3, res4 = cal(9,5)
print(res1, res2, res3, res4)
print(type(cal(1,2)))



