# ORACLE DATA
# CX_ORACLE 설치 : pip install cx_oracle

# 오라클 연동 -- 터미널에 복붙해주면됨
from sqlite3 import DatabaseError
import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', 1521, service_name = 'orcl')
# dsn = data source name
# 접속주소 : makedsn('호스트주소', 포트번호, service_name = 'orcl')

conn = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')
# conn = connection


cur = conn.cursor()
# cur = cursor
# 실행결과 데이터를 담을 메모리 객체

# DB접속이 성공하면 Connection 부터 cursor() 메서드를 호출하여 객체를 가져옴



try:
    for row in cur.execute('SELECT * FROM emp'):
        print(row)

    # cur.execute('SELECT COUNT(*), FROM emp')
    # result = cur.fetchone()
    # print(result)

except cx_Oracle.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 23번라인 확인요 : {e}')
finally:

    cur.close() # 커서 받고
    conn.close() # 접속 닫아야함, 순서도 그대로