# Ctrl K Ctrl S : 단축키 바로가기

# 객체 지향 Person 클래스


# a = 10

# if a == 9:
#     print('a')
# else:
#     pass

class Person:
    name = '무명이'  #아직이름이없
    age = 0
    height = 0
    gender =''
    feetsize = 250
    bloodtype = ''

#생성자

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('Person이 생성되었습니다')

    def 소개한다(self):
        greeting = f'''안녕하세요. 저는 {self.name} 입니다.
        {self.gender}구요. {self.age}살 입니다.'''
        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다.')


if __name__ == '__main__':
    # p=Person()  #p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p))  #id값

    # p2 = Person()  #객체생성
    # print(type(p2))
    # print(id(p2))

    ji = Person('자응',100)  # == __init__(self, name, age):
    # ji.name = '지응'
    # ji.age = 100
    ji.bloodtype = 'RH+ O'
    ji.feetsize = 300
    ji.gender = 'female'
    ji.height = 190

    # yoo = Person()
    # yoo.name = '유제니'
    # yoo.feetsize = '230'

    ji.소개한다()
    ji.먹는다('본죽')
    ji.일한다('핫식스')


