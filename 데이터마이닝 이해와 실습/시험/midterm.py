##### 2023-2학기 데이터마이닝이해와실습 (데사B0002 중간고사) #####

# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 대리시험을 치르는 행위
# (2) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (3) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (4) 동일 장소 내에서 동일한 IP Address를 사용하는 행위
# (5) 중복 로그인(하나의 ID로 두 개 이상의 컴퓨터에서 동시접속)하는 행위
# (6) 마우스 커서가 시험 응시화면에서 이탈되는 경우
# (7) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

##### 대답 : 네
##### 학번 : 20201012
##### 이름 : 임소정

##### 1번 문제 ##### 완료
#num = int(input("*의 개수를 입력 :"))
"""
# for 문으로 구현
for i in range(num, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# while 문으로 구현
i = num
while i > 0:
    j = i
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i -= 1
"""

##### 2번 문제 #####

foods = {"떡볶이":"김밥", "자장면":"단무지","라면":"파김치","치킨":"맥주","삼겹살":"소주"}

## coding here ##

fw = open("foods.txt", "w")
for key, value in foods.items():
    fw.write(key + "+" + value + "\n")


fw.close()

##### 3번 문제 ##### 완료
"""
import numpy as np

def find_number(array, i, j, k):
    ## coding here ##
    array = array[i-1:j]
    array.sort()
    return array[k-1]

a = np.array([1, 5, 2, 6, 3, 7, 4])
print(find_number(a, 2, 5, 3))
"""

##### 4번 문제 #####

# n1 = int(input('첫 번째 숫자를 입력하세요.'))
# n2 = int(input('두 번째 숫자를 입력하세요.'))

## coding here ##
"""
sum = 0
for i in range(n1, n2+1):
    sum += i
print(n1, end="")
for i in range(n1+1, n2+1):
    print("+", i, end="")
print("=", sum)
"""

##### 5번 문제 ##### 완료
"""
def count_space(k):
    ## coding here ##
    count = 0
    for i in k:
        if i == ' ':
            count += 1
    return count

sentence = 'Python is powerful and interesting for me.'
num = count_space(sentence)
print('빈칸의 개수 : ', num)
"""

##### 6번 문제 #####
"""
from pandas import DataFrame
a = {'Age':[23,21,24,22], 'Grade':['A+','B-','A','B'], 'Major':['Art','Datascience','Music','History']}
b = ['Andy','Jane','Chris','Som']

## coding here ##
df = DataFrame(a,b)

## coding here ##
print(df.loc[['Andy','Som'],['Age','Major']])
"""

##### 7번 문제 #####
"""
## coding here ##

df2 = df.loc[['Andy','Jane','Som'],['Age','Grade','Major']]
print(df2)

## coding here ##
df3 = df.loc[['Andy','Jane','Som'],['Age','Major']]
df3['Major'][1] = '데이터사이언스'
print(df3)
"""