# My Car 타고 집에 가고 싶다,,

from P02Vehicle import car

if __name__ == '__main__':
    mycar= car('98하 5678', '흰색')
    # mycar.차량번호 = '98하 5678'
    # mycar.색상 = '흰색'
    mycar.연료 = '경유'
    mycar.__제조사 = '기이아'  # 이쪽시트에서 넣은 자료로 입력이됨
    mycar.출고년도 = 1999
    mycar.기어단수 = 7
    
    print(mycar.__제조사)
    
    mycar.전진한다(2)
    print(mycar)
    print(mycar. 기어단수)
    mycar.제조사확인()  #여기서는 또 현대나옴 - Vehicle 시트에 현대 def 수식을 만들어줬기때문에
    print('------------헛소리--------------') 
    mycar.후진한다()
    

