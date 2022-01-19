# 파일쓰기
from cgitb import text


# f = open('writefile.txt', 'w', encoding = 'utf-8')

# f.write('저는 한국사람입니다. \n')

# texts = ['저는 한국사람\n', '저는 미국사람\n']
# f.writelines(texts)
# f.close


# 내용추가하기
# f = open('writefile.txt', 'a', encoding = 'utf-8')

# f.write('내용추가')
# f.close


f = open('writefile.txt', 'r', encoding = 'utf-8')

for line in f:
    print(line)
f.close