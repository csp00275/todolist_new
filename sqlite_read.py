import sqlite3

con = sqlite3.connect('C:\jh/todolist.db')
cursor = con.cursor()


# row 단위로 데이터 읽기
print("-----row 단위로 데이터 읽기------")
cursor.execute("SELECT * FROM kakao")
one = cursor.fetchone(); print(one) # 첫번째줄
one = cursor.fetchone(); print(one) # 두번째줄
one = cursor.fetchone(); print(one) # 세번째줄

# 모든 row를 다 읽기
print("-----모든 row를 다 읽기-----")
cursor.execute("SELECT * FROM kakao") # 앞서 선택한 테이블에서 모든데이터를 읽어서 새로 SELECT 구문 실행
all = cursor.fetchall(); print(all) # 전체를 불러옴

# 리턴 값을 변수로 바인딩 해둔 후 해당 변수를 통해 데이터에 접근
print("-----바인딩 한 변수를 통해 읽기-----")
cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
print(kakao[0][0])
print(kakao[0][1])
print(kakao[1][2])