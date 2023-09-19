#데이터마이닝의 이해와 실습
"""
number = input("숫자를 입력해 주세요.")

#print(number+2)        //오류 발생

number = int(input("숫자를 입력해 주세요."))

if number < 0 :
    print("양의 정수를 입력해주세요: ")
else :
    if nubmer %2 == 0: print("짝수")
#elif number %2 == 0: print("짝수")         가 더 좋은 코드임.
    else : print("홀수")
"""

#Page 4
"""
score = int(input("점수 : "))

if score >= 90 : print("A")
elif score >= 80 : print("B")
elif score >= 70 : print("C")
elif score >= 60 : print("D")
else : print("F")
"""

#Page 5
"""
age = int(input("고객님의 나이를 입력해 주세요. : "))

if age >= 60 : print("고객님의 연령대는 60대 이상 입니다.")
elif age >= 50 : print("고객님의 연령대는 50대 이상 입니다.")
elif age >= 40 : print("고객님의 연령대는 40대 이상 입니다.")
elif age >= 30 : print("고객님의 연령대는 30대 이상 입니다.")
elif age >= 20 : print("고객님의 연령대는 20대 이상 입니다.")
elif age >= 10 : print("고객님의 연령대는 10대 이상 입니다.")
"""


#Page 6
"""
#백준 1330번 문제
A = int(input("A를 입력하세요. : "))
B = int(input("B를 입력하세요. : "))

if A > B : print(">")
elif A < B : print("<")
else : print("=")
"""


#Page 7
#백준 14681번 문제
"""
x = int(input("x를 입력하세요. : "))
y = int(input("y를 입력하세요. : "))

if x > 0 and y > 0 : print("Quadrant 1")
elif x < 0 and y > 0 : print("Quadrant 2")
elif x < 0 and y < 0 : print("Quadrant 3")
elif x > 0 and y < 0 : print("Quadrant 4")
else : print("-1")
"""

#교수 답안
"""
def Quadrant(x=0, y=0):         #입력을 안할 경우를 대비하여 초기값 0으로 정의
    if x > 0 and y > 0 : print("Quadrant 1")
    elif x < 0 and y > 0 : print("Quadrant 2")
    elif x < 0 and y < 0 : print("Quadrant 3")
    elif x > 0 and y < 0 : print("Quadrant 4")
    else : print("-1")

x = int(input("x를 입력하세요. : "))
y = int(input("y를 입력하세요. : "))
"""


#Page 9
"""
sum = 0 

for i in range(1,11):
    sum += i

print(sum)
"""


#Page 10 (Page 17 참고)

"""
#예시
name = "김태완"

for i in name :
    print(i)
"""

"""
#답안
sum = 0

for i in str(3**79)         #3의 79승을 문자열(str)로 취급함.
    sum * = int(i)          #문자열로 취급한 것을 다시 숫자형(int)으로 바꿈.
print(sum)
"""

#Page 11!
"""
for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d", i, j, i*j)
"""

#Page 12
"""
number = 33             #number을 입력받지 않고, 33으로 고정
count = 0               #박수 수

for i in range(1, number) :
    for j in range(i, 3) :
        if i%3 == 0:            #str이라서 나누기 불가능
print(count)
"""

#교수 답안
"""
number = 33             #number을 입력받지 않고, 33으로 고정
count = 0               #박수 수

for i in range(1, number+1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            count += 1
print(count)
"""

#Page 12 (그림 그리기)
# *별표 그리기
#for문
"""
for i in range(5):
    print("*"*10)
"""

#while문
"""
i = 1
while i < 6 :
    print("*"*10)
    i+=1
"""

#숫자 역피라미드 그리기
#for문
"""
for i in range(6, 0, -1)
    print((str(i) + " ") * i)
"""

#while문!


#Page 12
"""
guess = int(input("숫자를 입력하세요. : "))
answer = 25

while answer != guess :
    if guess > answer : print("DOWN!")
    elif guess < answer : print("UP!")
    guess = int(input("숫자를 입력하세요. : "))

print("정답!")
"""

#Page 13
#오답 코드
"""
i = 1

while i <= 30:
    if i % 2  == 0 or i % 3 == 0 :
        continue            //무한반복에 빠짐.
    else:
        print(i)
        i += 1          
"""


#정답 코드
"""
i = 1

while i <= 30:
    if i % 2  == 0 or i % 3 == 0 :
        i += 1                  //while문은 수동으로 증가시켜줘야함.
        continue
    else:
        print(i)
        i += 1          
"""