# 중첩 IF
X = 6
if X > 0:
    print('양수')
    if X > 9:
        print('10보다 큰 수')
    else:
        print('10보다 작은 수')
elif X == 0 :
    print(0)
else:
    print('음수')
