# 주석이래
# 문자열 표현방법
print('hello, world')
print ("hello, world")  ##쌍따옴표도 허용되는 파이썬
print('''hello, world''')

# 숫자연산 출력
print (3+4)

# 변수사용
a = '안녕하세요'
b = '반갑습니다.'
print(a) 
print(b)
print(a, b)

# 수학연산
print(5+6)
print(5-6)
print(5*6)
print(5/3)
print(5//3)  ##//하면 정수로 값이 나옴
print(5%3)  ##나눈 값의 나머지
print(2**10) ##거듭제곱

print(int(5/3)) ##정수로 값이 나옴 >> 1
print(int('10')) ##십이나 ten으로는 인식안됨

print(float(5)) ##실수 5.0 나옴

# TYPE 확인
print(type(10)) ##int
print(type(10.0)) ##float

print(type('안녕')) ##str

# 괄호 (연산자 우선 순위)
print(2+(3*5))
print((2+3)*5)
