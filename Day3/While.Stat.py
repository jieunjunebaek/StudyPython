# While 문
#조건문이 True 인 동안 계속해서 수행문장을 반복적으로 수행하게 됩니다.
#너무 좋은 예제라 참조해 왔습니다. 열번 찍어 안 넘어가는 나무 없다를 while 문으로 구현해보겠습니다.
hit = 0

# while hit < 100: #이 값이 참인 동안
#     hit += 1 #같은말:hit=hit+1

#     print(f'나무를 {hit:2d}번 찍었습니다')
#     if hit == 100:
#         print('나무가 넘어갑니다')
#         break

# print('나무찍기를 마칩니다')

# For 문
for hit in range(0,100):
    if hit > 9:
        break
    print(f'나무를 {hit+1}번 찍습니다.')



