### 데이터 마이닝의 이해와 실습 ###
## 2주차
# 예시 1
# 나이를 입력받아 10대 이하, 10대, 20대, 30대, 40대, 50대, 60대 이상 중 하나를 출력해보자.
# 실행 예시
# 고객님의 나이를 입력해주세요: 22
# "고객님의 연령대는 20대 입니다."
# 고객님의 나이를 입력해주세요: 41
# "고객님의 연령대는 40대 입니다."
# 고객님의 나이를 입력해주세요: 79
# "고객님의 연령대는 60대 이상 입니다."
"""
age = int(input("고객님의 나이를 입력해주세요: "))
if age <= 10:
    print("고객님의 연령대는 10대 이하 입니다.")
elif age <= 20:
    print("고객님의 연령대는 10대 입니다.")
elif age <= 30:
    print("고객님의 연령대는 20대 입니다.")
elif age <= 40:
    print("고객님의 연령대는 30대 입니다.")
elif age <= 50:
    print("고객님의 연령대는 40대 입니다.")
elif age <= 60:
    print("고객님의 연령대는 50대 입니다.")
else:
    print("고객님의 연령대는 60대 이상 입니다.")
"""

# 예시 2
# 두 정수 a,b를 입력 받아 아래와 같이 출력해보자.
# a가 b보다 크면 ">"를 출력한다.
# a가 b보다 작으면 "<"를 출력한다.
# a와 b가 같으면 "="를 출력한다.
"""
a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")
"""

# 예시 3  
# 두 실수 x,y를 입력 받아 어느 사분면에 속하는지 함수를 만들어 보자.
# 실행 예시
# x를 입력하세요: 12
# y를 입력하세요: 5
# Quadrant 1
# x를 입력하세요: -12
# y를 입력하세요: 5
# Quadrant 2
# x를 입력하세요: -12
# y를 입력하세요: -5
# Quadrant 3
# x를 입력하세요: 12
# y를 입력하세요: -5
# Quadrant 4
# x를 입력하세요: 0
# y를 입력하세요: 0
# -1
"""
def Quadrant(x=0, y=0):
    if x > 0 and y > 0:
        print("Quadrant 1")
    elif x < 0 and y > 0:
        print("Quadrant 2")
    elif x < 0 and y < 0:
        print("Quadrant 3")
    elif x > 0 and y < 0:
        print("Quadrant 4")
    else:
        print("-1")

x = int(input("x를 입력하세요: "))
y = int(input("y를 입력하세요: "))
Quadrant(x, y)
"""
# 교수 답안
"""
x = int(input("x를 입력하세요: "))
y = int(input("y를 입력하세요: "))

if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x > 0 and y < 0:
    print("Quadrant 4")
else:
    print("-1")
"""

# 예시 4
# 리스트 안에 특정 숫자가 몇개 포함되어 있는지 찾는 함수를 만들어 보자.
"""
def how_many(a,b):
    count = 0
    for i in a:
        if i == b:
            count += 1
    return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(how_many(x,3))
print(how_many(x,2))
"""

# 예시 5
# 리스트 안에 특정 숫자보다 큰 숫자가 몇개 포함되어 있는지 찾는 함수를 만들어 보자.
"""
def bigger_than(a,b):
    count = 0
    for i in a:
        if i > b:
            count += 1
    return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(bigger_than(x,3))
print(bigger_than(x,2))
"""

# 예시 6
# X대학 M교수님은 프로그래밍 수업을 맡고 있다.
# 교실에는 학생이 20명이 있는데,
# 학생 명부에는 각 학생별로 1번부터 20번까지 출석번호가 붙어 있다.
# 교수님이 내준 과제를 17명이 제출했는데, 제출 안 한 학생 3명의 출석번호를 구해보자.
"""
student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

def not_submit(a):
    for i in range(1,21):
        if i not in a:
            print(i)

not_submit(student)
"""

# 교수 답안
"""
student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

for i in range(1,21):
    if i not in student:
        print(i)
"""

## 3주차
# 문제
# 값을 하나 입력 받아 별이 있는 그림을 출력해보자
# 실행 예시
# num = 1
# *
# num = 2
# **
# **
# num = 3
# ***
# ***
# ***
"""
def star(number):
    for i in range(number):
        print("*" * number)

num = int(input("0보다 큰 숫자 입력: "))
star(num)
"""

## 4주차
# 문제
# 7명의 이름이 저장된 리스트(name)에서 길이가 4인 이름만 "name.txt"파일에 써보자.
"""
f = open("name.txt", "w")
name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn'] 

for i in name:
    if len(i) == 4:
        f.write(i + "\n")

f.close()
"""

# 예시
# main.py, func1.py, func2.py가 있다.
"""
# main.py
from func1 import check_number
from func2 import find_next
f1.check_number("010-1234-5678")
print(find_next(4))

# func1.py
def check_number (string):

# func2.py
def find_next (x):
"""
# 루트 폴대 내 main.py와 "option"이라는 이름의 폴더에 있는 두 python파일이 그림과 같이 있을 때,
# main.py(1)에 들어갈 코드와 main.py를 실행했을 때 출력 결과를 구해보자.
"""
# main.py
import option.func1 as f1
print(f1.find_prev(2))

# main.py - 교수 답안
import option.func3
print(option.func3.find_prev(2))

# __init__.py
print("datascience")

# func3.py
def find_prev(x):
    return x-1
"""

## 5주차
# 예제 1
# 배열에 저장한 모든 값에 1씩 더해서 배열로 출력
# 실행 예시
# [2,5,1,17,21] -> [3,6,2,18,22]

# 방법 1
"""
a = [2,5,1,17,21]
result = []
for i in a:
    result.append(i+1)
print(result)
"""
# 방법 2
"""
import numpy as np

a = np.array([2,5,1,17,21])
result = (a + 1).tolist()

print(result)
"""

# 예제 2
# numpy를 사용해 1차원 배열을 2차원 배열로 변경
# 실행 예시
# [1, 3, 5, 7, 8, 11]
# [[1, 3, 5], [7, 8, 11]]
"""
import numpy as np
a = np.array([1, 3, 5, 7, 8, 11])
b = a.reshape(2,3)

print(b)
"""

# 예제 4
# numpy를 사용하여 아래의 사칙연산을 수행하라.
# 10 + 30 = ?
# 40 - 93 = ?
# 55 * 71 = ?
# 250 / 25 = ?

# 방법 1
"""
import numpy as np

a = np.array([1, 3, 5, 7, 8, 11]),

print(a)
print(a + 1)
print(a - 1)
print(a * 2)
print(a / 2)
"""
# 방법 2
"""
import numpy as np

res1 = np.add(10, 30)
res2 = np.subtract(40, 93)
res3 = np.multiply(55, 71)
res4 = np.divide(250, 25)

print(res1, res2, res3, res4)
"""

# 예제 5
# 랜덤 값이 있는 10 * 10 배열을 만들고 최소값과 최대값을 찾기
"""
import numpy as np
a = np.random.random((10,10))

min_a = a.min()
max_a = a.max()

print(a)
print(min_a, max_a)
"""

# 예제 6
# linspace()함수를 이용하여 sin 0부터 sin pi사이의 값 11개를 다음과 같이 출력해보자.
# 실행 예시
# [0.00000000e+00 3.09016994e-01 5.87785252e-01 8.09016994e-01
# 9.51056516e-01 1.00000000e+00 9.51056516e-01 8.09016994e-01
# 5.87785252e-01 3.09016994e-01 1.22464680e-16]
"""
import numpy as np

values = np.linspace(0, np.pi, 11)
x = np.sin(values)
print(x)
"""

# 예제 7
# 아래 점수를 보고 다음을 구해보자
# - 각 교과목의 총점
# - 각 교과목의 평균
# - 가장 잘 본 교과목의 평균
#       midexam   finalexam   homework
# Python    90        92          37
# R         85        88          91
# Math      94        91          84
"""
import numpy as np

scores = np.array([[90, 92, 37], [85, 88, 91], [94, 91, 84]])

print(scores.sum(axis=1))
print(scores.mean(axis=1))
print(scores.mean(axis=0).max())
"""

# 예제 8
# 총 30일의 매출이 적혀있는 "sales"list중에서 40000원 이상의 매출을 달성하지 못한 날과 그 매출을 구해보자.
"""
import numpy as np
import random

sales = [86623, 33030, 2541, 3620, 6930, 1380, 38117]

n_sales = np.array(sales)

# 매출을 달성하지 못한날
filter = n_sales < 40000

# 매출을 달성하지 못한 날의 매출액
bad_sales = n_sales[filter]

print(bad_sales)
"""

# 예제 9
# numpy에서 txt파일을 읽는 함수는 loadtxt이다. 평균을 구해보자.
"""
import numpy as np
data = np.loadtxt('data.txt', delimiter = ',')
print(data.mean())
"""

# 예제 10
# numpy에서 txt파일을 읽는 함수는 loadtxt이다. 평균을 구해보자.
"""
data = np.loadtxt('data2.txt')
average = np.mean(data)
print(average)
"""

## 7주차
# Series 연산 예제
# a와 b의 차이가 4 초과인 경우의 b의 값을 출력해보자.
"""
from pandas import Series

a = Series([30, 14, 24, 50, 12])
b = Series([0, 9, 22, 46, 13])

cond = abs(a - b)
print(b[cond > 4])

# 교수 답안
diff = abs(a - b)
cond = diff > 4
print(b[cond])
"""

# Homework
# 1
# "homework.txt"파일에는 다수의 학생이름과 점수가 적혀있습니다.
# 이름은 모두 영문자로 되어 있으며, 점수는 0~100사이의 값을 가집니다.
# 실행 결과
# number.txt
# 1. Alex : 90
# 2. Emma : 85
# 3. Smith : 94
# 4. Jane : 85
# 5. Ava : 88
# 6. Charlotte : 91
# 7. Evelyn : 91
# 8. Olivia : 84
# 9. Mia : 84
# 10. Amelia : 84

# 1-1
# 해당 데이터를 활용하여 모든 학생의 평균 점수를 구해보자.
"""
f = open("homework.txt", "r")
data = f.readlines()
f.close()

sum = 0
for i in data:
    score = i.split(":")[1]
    sum += int(score)
print(sum / len(data))
"""

# 1-2
# 이 중에서 이름의 길이가 5 이상인 사람에 대해,
# 아래와 같이 보이도록 "len5.txt"파일을 만들어보자.
# 실행 결과
# len5.txt
# 1 : Smith
# 2 : Charlotte
# 3 : Evelyn
# 4 : Olivia
# 5 : Amelia
"""
f = open("homework.txt", "r")
data = f.readlines()
f.close()

f = open("len5.txt", "w")
for i in data:
    name = i.split(":")[0]
    score = i.split(":")[1]
    if len(name) >= 5:
        f.write(name + "\n")
f.close()
"""