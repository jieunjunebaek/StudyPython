# IF구문 - 흐름제어
#name = '니니'

#if name == '미미' or name == '다다':

#name = ['미미', '다다', '나나', '히히'] #리스트/튜플 If구문에 노상관

name = ('미미', '다다', '나나', '히히')

if '히히' in name:
    print('의사를 만나러 갑니다.') # : 다음의 문장은 Tab으로 들여쓰기를 맞춰줘야 합니다. 이를 indent 들여쓰기 라고 부르는데 이를 맞춰주지 않으면 역시 실행되지 않습니다.
    print('의사선생님께 인사를합니다')
elif name == '다원':
    print('주사실로 간다.')
else:
    print('호출할때까지 대기합니다')

x = 2
if x !=10:
    pass
else:
    pass


