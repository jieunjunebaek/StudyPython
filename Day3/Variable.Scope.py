# 함수와 변수의 라이프 스코프

# 함수를 사용할 때 변수는 어디에나 지정할 수 있습니다만 모든 변수가 사용될 수 있는 범위가 있습니다. 
# 이를 뜻할 때 지역변수, 전역변수라고 부르는데요. 함수와 같이 구성되면서 나오는 문제입니다.


a = 10  #전역변수

def vartest(a):  #함수선언//매개변수이면서 지역변수, 이 세줄에서만 쓰임
    a = a + 1 
    return a

a = vartest(a) 
print(a)



