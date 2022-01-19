# 입력 테스트
# a = input()
# print(f'입력값은 {a}')

# number = input('수를 입력하세요 :')
# number = int(number)  #수가  str으로 나와서 숫자로 바꿔줘야함
# print(number)  

# number = int(input('수를 입력하세요 :'))
# print(number*20)  #5-7라인이랑 같은값나옴

# number = input('수를 입력하세요 :')
# print(int(number)*20)  #9-10라인이랑 같은값나옴


# Escape Character 탈출문자(특수문자)
print('Life is short. you need Python.')
print('Life is short.\nyou need Python.')
print('Life is short.\ryou need Python.')  # \r 문자 날려버림, 값: you need Python.
print('Life is short.\tyou need Python.')  # \t tab
print('Life is \"short\". you need \'Python\'.')  # \'문자\' or \"문자\" Life is "short". you need 'Python'.
print('Life is short.\byou need Python')  # \b 백스페이스 값: Life is shortyou need Python
