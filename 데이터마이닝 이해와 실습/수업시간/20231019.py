from pandas import Series

# 7주차 9페이지
'''
a = [100, 90, 80]
c = ['국어', '영어', '수학']

b = Series(a)
b = Series(a,c)
b = Series (data=a, index=c)

print(b)
'''

# 인덱스값을 만들지 않아도, key값이 자동으로 인덱스가 된다.
'''
x = {'국어': 100, '영어': 90, '수학': 80}
y = Series(x)

print(y)
'''

# 7주차 11페이지
# 다음 데이터를 pandas Series 객체로 생성하자.
# index는 국어, 수학, 영어
# values는 100, 90, 85
'''
a = [100, 90, 85]
c = ['국어', '수학', '영어']
b = Series(a, c)
print(b)
'''

# 7주차 12페이지
'''
x = {'국어': 100, '영어': 90, '수학': 80}
y = Series(x)

print(y.iloc[1])
print(y.loc['영어'])
print(y[1])
'''

'''
a = [1, 2, 3]
b = Series(a)
print(b)
'''

# 7주차 15페이지
'''
x = {'국어': 100, '영어': 90, '수학': 80, '미술': 100}
y = Series(x)

# print(y.iloc[1])
# print(y.loc['영어'])
# print(y[1])

print(y.iloc[[0, 2]])
print(y.loc[['국어', '수학']])

print(y.iloc[1:4])
print(y.loc['영어':'미술'])     # loc는 마지막 인덱스도 포함한다.
'''

# 7주차 18페이지 Pass 안나옴

# 7주차 19 ~ 20페이지
# 1
'''
x = {'국어': 100, '영어': 90, '수학': 80, '미술': 100}
y = Series(x)

y.loc['국어'] = 70      # 
y.iloc[0] = 60

y.loc['과학'] = 99      # 새로운 인덱스를 추가하면, 새로운 인덱스가 생성된다.
y.iloc[4] = 98          # 아예 없는 인덱스는 추가후, 수정이 가능하다.

# y.drop('미술')
y.drop('미술', inplace = True)

print(y)
'''

# 2
'''
a = [1,2,3]
b = ['A', 'B', 'C']
s = Series(a, b)

s1 = s.drop('A')
'''

# 7주차 26페이지
'''
# index가 같은 A끼리만 계산이 된다.
a = Series([10, 20, 30], ['A', 'B', 'C'])
b = Series([0, 40, 100], ['A', 'D', 'E'])
c = a -b

print(c)
'''

# 7주차 28페이지
'''
s = Series([1, 2, 3, 4, 5])
cond = s > 3

print(type(cond))
print(cond)         # True, False로 출력된다.
print(s[cond])      # True인 값만 출력된다.
'''

# 7주차 29페이지
# a와 b의 차이가 4초과인 경우의 b의 값을 출력하자.
'''
a = Series([30, 14, 24, 50, 12])
b = Series([0, 9, 22, 46, 13])

cond = abs(a - b)       # 교수 답안
print(b[cond > 4])

# cond = a - b > 4      # 내 답안
# print(b[cond])
'''

# 7주차 30페이지
'''
a = Series([30, 14, 24, 50, 12])
b = Series([0, 9, 22, np.nan, 13])

print(b.isna())
print(sum(b.isna()))
'''

# 7주차 31 ~ 33페이지
# unique()함수는 중복되는 값 제거
# 실제로 데이터가 많을 때, 많이 쓰임.
'''
data = ['라일락', '코스모스', '코스모스', '장미', '코스모스', '장미’]
series_data = Series(data)

print(series_data.unique())
print(series_data.value_counts())
print(series_data.isin(['코스모스']))
'''

# 7주차 34페이지 쯤 어딘가에 있음.
# 페이지는 걍 참고만 하자.
# 표를 데이터프레임 통째로 읽어온다.
# 시험 범위 아님. 즉, 안 나온다.
'''
df = pd.read_csv('korean-idol.csv')
print(df)
'''

# 7주차 34 ~ 36페이지
from pandas import DataFrame
# DataFrame 생성하는 3가지 방법중에서
# 하나만 기억해도 된다.

# 1
'''
data = {
    '나이' : [20,21,24],
    '성별' : ['여','남','여'],
    '학교':['A','B','C']
}

name = ['김지연','이태형','전지희']
df = DataFrame(data=data, index=name)
print(df)
'''

# 2
'''
data = [
    [20, '여', 'A'],
    [21, '남', 'B'],
    [24, '여', 'C']
]
index = ['김지연','이태형','전지희']
columns = ['나이', '성별', '학교']
df = DataFrame(data=data, index=index, columns=columns)
print(df)
'''

# 3
'''
a = [
    {'나이':20, '성별':'여','학교':'A'},
    {'나이':21, '성별':'남','학교':'B'},
    {'나이':24, '성별':'여','학교':'C'}
]
name = ['김지연','이태형','전지희']
df = DataFrame(data=a, index=name)
print(df)
'''


a = [
    {'나이':20, '성별':'여','학교':'A'},
    {'나이':21, '성별':'남','학교':'B'},
    {'나이':24, '성별':'여','학교':'C'}
]
name = ['김지연','이태형','전지희']
df = DataFrame(data=a, index=name)

# 7주차 37 ~ 39페이지
# 무조건 행부터 입력, 그 후에 열을 입력한다.
'''
print(df.iloc[1,2])
print(df.loc['이태형', '학교'])

print(df[['나이', '학교']])         # 데이터프레임이다.
'''

# 7주차 43페이지
'''
print(df.iloc[[1,2], [1,2]])
print(df.loc[['이태형', '전지희'], ['성별', '학교']])
'''

# 7주차 45페이지
'''
df.rename(columns={'나이':'age','성별':'gender','학교':'school'}, inplace=True)
print(df)
'''

# 7주차 46페이지
# 바로 drop을 하면, 원본이 손상이 된다.
# 그러므로 copy를 한 후에 그것을 drop을 해야한다.
'''
df2=df.copy()
df2.drop('이태형', inplace=True)
print(df2)
'''

# 46까지가 시험범위다.