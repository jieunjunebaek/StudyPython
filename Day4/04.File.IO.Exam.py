# 파일입출력

# 파일출력
# f = open('newfile.txt', 'w')  #wirte = 출력
# f.close()  #탐색기에 새로운텍스트파일 생김+_+

# f = open('C:\Sources/Sample_Test1.txt', 'w') 
# f.close() 
# print('파일이 생성되었습니다.') 

# newfile.txt 파일입력(읽어보기
# f = open('newfile.txt', 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f.close()

# newfile.txt 파일입력(읽어보기) - FOR 문
# f = open('newfile.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     print(line)

# f.close()

f = open('newfile.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
f.close()