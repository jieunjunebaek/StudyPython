# 리스트 연산

arr = list(range(5))
print(arr)  #rkqt : [0, 1, 2, 3, 4]

arr = list(range(1,6))
print(arr)  #rkqt : [1, 2, 3, 4, 5] / 원하는값-1까지 17까지 하고싶음 range(1,18) 해야함

arr = list(range(2,101,2))  #2부터 100까지 2씩 증가(짝수)
print(arr)

print(arr[0]+arr[5])  #rkqt : 14 = 첫번째 인덱스(2)랑 다섯번째 인덱스(12) 합


# 이중 리스트 - 이차원 배열 에서는 다음과 같은 연산도 가능합니다.
arr2 = [1, 2, ['Hi', 'My', 'friend']]
print(arr2[0])  #rkqt : 1
print(arr2[2])  #rkqt :  ['Hi', 'My', 'friend']

print(arr2[-1][1])  #rkqt : My
print(arr2[-1][1][1])  #rkqt : y

arr3 = list(range(1,4))
print(arr3)  #rkqt : [1, 2, 3]
print(arr3*3)  #rkqt : [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트 함수
print('---리스트 내장함수')
del(arr3[1])
print(arr3)  #rkqt : [1, 3] / 인덱스 순서로 지움

arr3.remove(1)
print(arr3)  #rkqt : [3] / 1을 지운거임

# 리스트 삭제
arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)  #값을 찾아서 삭제
print(arr4)  #rkqt : [4, 2, 6, 9, 12, 16, 7, 1, 3, 5] / 최초의 3만 지워짐 

del(arr4[8])  #리스트 인덱스로 삭제
print(arr4)  #rkqt : [4, 2, 6, 9, 12, 16, 7, 1, 5] / 인덱스로 삭제 3이 다 없어짐


arr4.sort()
print(arr4)  #rkqt : [1, 2, 4, 5, 6, 7, 9, 12, 16] / 순서대로 정렬해줌
arr4.reverse()
print(arr4)  #rkqt : [16, 12, 9, 7, 6, 5, 4, 2, 1] / 내림차순 정렬

arr4.insert(2,10)  #rkqt : [16, 12, 10, 9, 7, 6, 5, 4, 2, 1] / 두번째자리(0.1.2)에 10을 넣어줌
print(arr4)

arr4[0] = 108
print(arr4)


tup1 = tuple(range(1,6))  #rkqt : (1, 2, 3, 4, 5) 리스트랑 괄호가 다름
#tup1[0] = 99 #TypeError: 'tuple' object does not support item assignment
#튜플은 리스트와 유사하지만 앞서 말한바와 같이 들어있는 요소를 변경할 수 없습니다(추가X, 삭제X, 수정X)
print(tup1)


# 딕셔너리 연산
## 딕셔너리는 새로운 키와 값의 쌍을 추가할때 아래와 같이 합니다.
dic1 = {1: 'a'}
dic1[2] = 'b'
print(dic1)  #rkqt : {1: 'a', 2: 'b'}

dic1['name'] = 'Hugo'
print(dic1)  #rkqt : {1: 'a', 2: 'b', 'name': 'Hugo'}


## 딕셔너리의 요소를 삭제하는 방법입니다.
del dic1['name']
print(dic1)  #rkqt : {1: 'a', 2: 'b'}

print(dic1.keys())  #rkqt : dict_keys([1, 2])
print(dic1.values())  #rkqt : dict_values(['a', 'b'])
print(dic1.items())  #rkqt : dict_items([(1, 'a'), (2, 'b')])

# 리스트를 튜플로 변환
print(arr4)  #rkqt : [108, 12, 10, 9, 7, 6, 5, 4, 2, 1]

tup2 = tuple(arr4)  #rkqt : (108, 12, 10, 9, 7, 6, 5, 4, 2, 1) / 값 수정안되어용
print(tup2)

arr4.sort()
print(arr4)  #rkqt : [1, 2, 4, 5, 6, 7, 9, 10, 12, 108]

print(tup1)  #rkqt : (1, 2, 3, 4, 5)
arr5 = list(tup1)  #rkqt : [1, 2, 3, 4, 5]
print(arr5)

arr5.append(6)
print(arr5)  #rkqt : [1, 2, 3, 4, 5, 6]
tup1 = tuple(arr5)
print(tup1)  #rkqt : (1, 2, 3, 4, 5, 6) >>>>>>>>>>>>> 6 추가한 리스트 -- 튜플로 변경


