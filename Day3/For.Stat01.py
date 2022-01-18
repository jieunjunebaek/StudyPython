# 기본 For 구문 - 흐름제어
# for 변수 in list(tuple, str):
#     수행할 문장1
#     수행할 문장2

# arr = [1, 2, 3, 4, 5, 555]

# for i in arr:
#     print(f'{i:8.2f}') #8.2에서 8은 정수자리 8칸을 할당하라는 의미 그래서 값:     1.00 이렇게 나옴

# arr = list(range(1,100))

# for i in arr:
#     print(f'{i:0.2f}')

# 튜플로 For 문
# arr2 = ('me', 'my', 'friend', 'jane')
# for item in arr2:
#     print(f'{item:>10}')

# 합계 For 문

numbers = list(range(1,21))
res = 0
for item in numbers:
    res += item
print(f'{numbers[-1]} 까지의 총 합은 {res} 입니다.')
    #print(f'총 합은 {res} 입니다.')

# 홀수 짝수 구분
# numbers = list(range(1,21))

# for item in numbers:
#     if item % 2 == 0:  #짝수
#         print(f'{item}은 짝수')

# numbers = list(range(1,21))

# for item in numbers:
#     if item % 2 != 0:  #홀수
#         print(f'{item}은 홀수')


# 13이상이면 탈출(break) 또는 계속(continue)
numbers = list(range(1,21)) #1~20까지

# for item in numbers:
#     if item >= 13:
#         break
#     if item % 2 != 0:  #홀수
#         print(f'{item}은 홀수') #1 3 5 7 9 11


# for item in numbers:
#     if item == 15:
#         continue
#     if item % 2 != 0:  #홀수
#         print(f'{item}은 홀수') #1 3 5 7 9 11 13 17 19


# 구구단 만들기
# print('구구단 프로그램')
# for i in range(2, 10): #2~9까지
#     # if i == 8 :
#     #     break  # 7단까지만계산됨
#     print(' ')
#     print(f'{i}단 시작')    
#     for j in range(1, 10): #1~9까지
#         # print(i*j) #2 4 6 8 10 ... 9 18 ...81 구구단의 합만나옴
#         print(f'{i} x {j} = {i*j:2d}', end='   ') #2d 결과값 나오는 숫자가 두자리로 표현됨
#     print(f'{i}단 끝')


# Inline FOR 문
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result) #[3, 6, 9, 12]

# 기존 FOR 문
t = []
for i in a:
    t.append(i*3)
print(t)


