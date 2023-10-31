# 데이터마이닝의 이해와 실습 과제
# 1
# "name.txt"파일에는 우리반 학생 n명의 출석번호와 이름이,
# "midterm.txt"파일에는 4개의 교과목 이름과 함께 출석번호 순서로 각 교과목 점수가 적혀 있습니다.
# 각 교과목의 점수는 0~100 사이의 값을 가지며, 다음을 구해보자.
# 공동 1등이 있는 경우 모두 1등으로 인정한다.

# name.txt
# 1 Wade
# 2 Dave
# 3 Seth
# 4 Ivan
# 5 Riley
# 6 Gilbert
# 7 Jorge
# 8 Dan
# 9 Brian
# 10 Roberto
# 11 Ramon
# 12 Miles
# ...

# midterm.txt
# Korean / Mathmatics / English / Art
# 30,67,71,90
# 82,84,41,73
# 39,54,40,94
# 38,55,40,40
# 33,68,96,33
# 73,83,93,33
# ...

# 1-1
# 해당 데이터를 활용하여 4개 교과목 평균점수 기준 1등 학생의 이름을 구해보자.
# write your code
# 방법 1
# name.txt 파일을 읽어서 name 리스트에 이름을 저장한다.
"""
name = []
with open('name.txt', 'r') as f:
    for line in f:
        name.append(line.split()[1])

score = []
with open('midterm.txt', 'r') as f:
    for line in f:
        score.append(line.split(','))
score = score[1:]
score = list(map(list, zip(*score)))
score = list(map(lambda x: list(map(int, x)), score))

avg = list(map(lambda x: sum(x)/len(x), score))
max_score = max(avg)
max_index = avg.index(max_score)
print(name[max_index])
"""
# 방법 2
# name.txt 파일을 읽어서 name 리스트에 이름을 저장한다.
"""
import numpy as np
name = []
with open('name.txt', 'r') as f:
    for line in f:
        name.append(line.split()[1])

score = []
with open('midterm.txt', 'r') as f:
    for line in f:
        score.append(line.split(','))
score = score[1:]
score = list(map(list, zip(*score)))
score = list(map(lambda x: list(map(int, x)), score))

avg = list(map(lambda x: sum(x)/len(x), score))
max_score = max(avg)
max_index = avg.index(max_score)
print(name[max_index])
"""

# 1-2
# 4개의 교과목 별 1등 학생의 이름을 아래의 형식으로 "top.txt"에 출력해보자.
# 아래의 그림의 이름은 임의로 적혀 있으므로, 실제 1등 학생의 이름은 다를 수 있습니다.
# top.txt
# Korean: Paul
# Mathmatics: Joe
# English: Douglas
# Art : Alexis

# 방법 1
"""
# name.txt 파일을 읽어서 name 리스트에 이름을 저장한다.
name = []
with open('name.txt', 'r') as f:
    for line in f:
        name.append(line.split()[1])

# midterm.txt 파일을 읽어서 score 리스트에 점수를 저장한다.
score = []
with open('midterm.txt', 'r') as f:
    for line in f:
        score.append(line.split(','))
score = score[1:]
score = list(map(list, zip(*score)))
score = list(map(lambda x: list(map(int, x)), score))

# 각 과목별 평균점수를 구한다.
avg = list(map(lambda x: sum(x)/len(x), score))
max_score = max(avg)
max_index = avg.index(max_score)

# 각 과목별 1등 학생의 이름을 구한다.
subject = ['Korean', 'Mathmatics', 'English', 'Art']
top = []
for i in range(4):
    top.append(name[score[i].index(max(score[i]))])
with open('top.txt', 'w') as f:
    for i in range(4):
        f.write(subject[i] + ': ' + top[i] + '\n')
"""

# 방법 2
"""
# name.txt 파일을 읽어서 name 리스트에 이름을 저장한다.
name = []
with open('name.txt', 'r') as f:
    for line in f:
        name.append(line.split()[1])

# midterm.txt 파일을 읽어서 score 리스트에 점수를 저장한다.
score = []
with open('midterm.txt', 'r') as f:
    for line in f:
        score.append(line.split(','))
score = score[1:]
score = list(map(list, zip(*score)))
score = list(map(lambda x: list(map(int, x)), score))

# 각 과목별 평균점수를 구한다.
avg = list(map(lambda x: sum(x)/len(x), score))
max_score = max(avg)
max_index = avg.index(max_score)

# 각 과목별 1등 학생의 이름을 구한다.
subject = ['Korean', 'Mathmatics', 'English', 'Art']
top = []
for i in range(4):
    top.append(name[score[i].index(max(score[i]))])
with open('top.txt', 'w') as f:
    for i in range(4):
        f.write(subject[i] + ': ' + top[i] + '\n')
"""

# 파일 생성 및 저장
"""
# 파일 생성
f = open('test.txt', 'w')
f.close()

# 파일 저장
f = open('test.txt', 'w')
f.write('Hello World!')
f.close()

# 파일 읽기
f = open('test.txt', 'r')
print(f.read())
f.close()
"""
