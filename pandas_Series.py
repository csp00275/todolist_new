from pandas import Series

kakao = Series([92600, 92400, 92100, 94300, 92300])
# print(kakao)

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
# print(kakao2['2016-02-19'])



for date in kakao2.index:
#     print(date)
for ending_price in kakao2.values:
#     print(ending_price)


# pandas Series는 인덱싱이 같은 애들끼리 덧셈이 됨. (리스트과 같이 저장하는데 딕셔너리처럼 바인딩이 되어있는게 특징)
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print(merge)