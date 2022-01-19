# Random 함수
import random

print(random.choice(range(1,7)))  #주사위

# Lottery
numbers = list(range(1,46))
# print(numbers)
lottery = []  #list()

for i in range(6):  #6번반복한다는 뜻(0 1 2 3 4 5)
    lottery.append(random.choice(numbers))

print(lottery)  #중복수가 나올 수 있음

