#데이터마이닝의 이해와 실습
#2주차 강의자료

# Page 18

a = [3, 19, 20, 25]
"""
#for i in range(len(a)):
#    print(a[i])

#for i in a:
#    print(i)

res = 0
for i in a:
    if i % 2 == 1:
        res += i
print(res)
"""

# Page 19
"""
#교수 답안
score = [71, 55, 24, 73, 68, 90]

for i in score:
    cnt += 1
    if i > 70:
        print("%d번 학생 합격"%cnt)

#비효율적인 코드
#for i in range(len(score)):
#    if score[i] > 70:
#        print("%d번 학생 합격"%(i+1))
"""

# Page 20
"""
#교수 답안
value = [80, 75, 91, 47, 100, 5, 26]

sum = 0

for i in value:
    sum += i

average = sum / len(value)
print(average)
"""

# Page 21
"""
#교수 답안
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
b= ''

for i in a:
    if len(i) == 5:
        b += i + ' '

print(b)

# 예시
# a = "t" + "a" + "e"
# print(a)
"""

# Page 22
"""
#교수 답인(미완성 체크할 것)
answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = [‘hello’, 62, ‘umbrella’, 145]
B = [‘September’, 512.3, ‘coffee’, 39, ‘keyboard’, ‘notebook’, 0.5, ‘f12’]
C = [‘computer’, 568.2, 39, ‘aPple’, 111, ‘Dongduk’, ‘water’]
     
for i in A:
    if i in answer:
        print("O", end='')
    else
"""

# Page 23
"""
# 교수 답안
visit = ['영국', '일본', '미국', '프랑스', '폴란드', '칠레', '캐나다', '이탈리아']
wish = ['브라질', '독일', '캐나다', '호주', '영국']
result = []             # 빈 리스트 생성(중요)

for i in wish:
    if i in visit:
        result

print(result)
"""

# Page 24
"""
# 교수 답안
def how_many(a,b):
    cnt = 0
    for i in a:
        if i == b:
            cnt += 1
    return cnt

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(how_many(x,3))
print(how_many(x,5))
"""

# Page 25
"""
def bigger_than(a,b):
    cnt = 0
    for i in a:
        if i > b:
            cnt += 1
    return cnt
x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]

print(bigger_than(x,4))
print(bigger_than(x,5))
"""

# Page 26
"""
# 교수 답안
student = [12,18,3,20,14,51,9,10,11,6,2,17,16,4,15,8]

for i in range(1,21):
    if i not in student:
        print(i)
#        print(i, end=' ')               # 가로로 출력

print(len(student))
"""

# Page 27
"""
# 교수 답안 (미완성 체크할 것)
capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국": "런던", }

for i in capital:
    print(i, capital[i])

# 29페이지 참고
# 이것도 가능 1
# for i in caplital.keys():
#    print(i, caplital[i])

# 이것도 가능 2
# for k, v in caplistal.items():
#    print(k, v)
"""

# Page 28
"""
# 교수 답안

score = {'국어': 90, '영어': 95, '수학': 77, '과학': 68, '사회': 82}

sum = 0
average = 0.0

for i in score:
    sum += score[i]

average = sum / len(score)
print("전체 평균은 %.1f점입니다."%average)
"""

# Page 29
"""
sum = 0
a = str(3**79)

for i in a:
    sum += int(i)
"""

# Page 30
"""
string = "abcaaccbbbbbbacccc"

alphabet = ['a', 'b', 'c']
for i in string:
    if i not in alphabet:       #alphabet에 없으면 append하라.
        alphabet.append(i)

print(alphabet)
"""

# Page 32
"""
a = '1.txt'
#2.txt

b = a.replace('*', 'C://users/taewan/desktop/')
C://users/taewan/desktop/1.txt
"""

# Page 33
##split, replace
"""
a = '김태완/데이터사이언스/40/홍길동/경영학과/41/'
name = a.split('/')[-2]
print(name)
"""

##join 1
"""
score = {'국어': 90, '영어': 95, '수학': 77, '과학': 68, '사회': 82}

# 국어/영어/수학/과학/사회
name = '/'.join(score)

print(name)
"""

###join 2
"""
score = {'국어': 90, '영어': 95, '수학': 77, '과학': 68, '사회': 82}

# 국어/영어/수학/과학/사회
name = '/'.join(score)

a = ['a', 'b', 'c']
answer = ''.join(a)
print(answer)
"""

# Page 34
"""
# 교수 답안
sentence = 'school'
res = sentence[0] + sentence[-1]

print(res)
"""

# Page 35
"""
# 교수 답안
phone_number = '010-1234-5678'
modified_number = phone_number.replace('-', '')
print(modified_number)
"""

######################################################
#3주차 강의자료

# Page 6
"""
def taewan(a,b):
    res = a+b
    return

taewan(3,4)
"""

# Page 8
"""
# 강의자료 복붙
def hap(a,b,c=0):
    result = a+b+c

    return result

x1 = hap(1,2,3)
x2 = hap(4, 5)
# x2 = hap(b=4, c=5)        #매개변수 입력

print(x1, x2)
"""

# Page 10 중요
# Page 11 꼭 기억할 페이지
"""
# 강의자료 복붙
def hap(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

hap = 0
hap = plus(100,200,300,400)
print(hap)
"""

# Page 13 꼭 기억할 페이지

# Page 14

def star(number):

num = int(input("0보다 큰 숫자 입력:"))
star(num)