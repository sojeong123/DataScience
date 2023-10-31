rm(list=ls())

a = 10

if(a>5)
{
  print(a)
  print('hi')
  print(a)
  print(a+1)
  cat (a, 'hi\n')
}else{       #C언어처럼 아랫줄에 작성하면 error가 난다.
  print(a)
}

# 1 (옳은 코드)
score = 88
if(score>= 90){
  grade = 'A'
}else if (score>=80){
  grade = 'B'
}else if (score>=70){
  grade = 'C'
}else{
  grade = 'F'
}
grade

# 2 (틀린 코드)
# 위의 코드 부터 빠져나가도록 작성
# 시험 문제에서는 60, 70, 80순으로 제시하지만
# 본인이 코드 작성시에는 주의해서 80, 70, 60순으로
# 작성할 것!
if(score>=60){
  grade = 'C'
}else if(score>=70){
  grade = 'B'
}else if(score>90){
  grade = 'A'
}


a = 10

if(a>=8){
  print(a)
}else{
  print('hi')
}

# 2 (7주차 5페이지 참고)
# 답은 같으나 비효율적인 코드
if(a>=8){
  print(a)
}if(a<=8){
  print('hi')
}


a = 10
b = 20
if(a>b){
  c = a
}else{
  c = b
}
c
print(c)

c = ifelse(a>b, a, b)
# a>b이면 a출력, 아니면 b출력
# 하지만
# c = ifelse(a>b, a = c, b = c)
# 라고 입력하면 안됨.

a = c(3, -1, 5)

for(x in a){
  cat(x,'\n')
}
# cat은 자동 줄바꿈 안하므로
# 끝에 \n 쓰기


for(i in 3:5){
  print('x')
  print(i)
}


# 7주차 12쪽 참고
for(i in 1:9){
  cat('2*', i, '=', 2*i, '\n')
}
# 2개이상 출력시에는 print 절대 안됨!
# 꼭 cat사용.
# cat 부분을 네모빈칸으로 제시하고
# 빈칸안에 들어갈 내용을 고르는
# 오지선다 문제가 있음.
# 조건문과 반복문을 합쳐서 문제 냄(많음).

for(i in 1:10){
  if(i %% 2 ==1){
    print(i)
  }
}
# 홀수만 출력

for(i in 1:10){
  if(i %% 2 ==0){
    cat(i,'')
  }
}
# 2 4 6 8 10이 가로로 쭉 있으면,
# cat사용한 것으로 눈치를 채야함.



# 1부터 100까지 더함 (반복)
sum = 0
for(i in 1:100){
  sum = sum + i
}
sum


# 7주차 16페이지
View (iris)

norow <- nrow(iris)
mylabel <- c( )
for(i in 1:norow) {
  if (iris$Petal.Length[i] <= 1.6) {
    mylabel[i] <- ‘L’
  } else if (iris$Petal.Length[i] >= 5.1) {
    mylabel[i] <- ‘H’
  } else {
    mylabel[i] <- ‘M’
  }
}
length(mylabel)

a = data.frame(iris$Petal.Length, mylabel)
View(a)


# for문 버전
for(i in 1:5){
  print(i)
}

# whie문 버전
i = 1
while(i<=5){
  print(i)
  i = i+1
}


################################################
# for문 버전
sum = 0
for(i in 1:10){
  sum = sum + i
}
sum

# while문 버전
sum = 0
i = 1
while(i<=10){
  i = i + 1
  sum = sum + 1

}
sum
# 어딘가 잘못 작성한듯
# 확인 필요함.
################################################

# 7주차 21페이지 참고
for(i in 3:9){
  print(i)
  if(i>6){
    break
  }
}
# break 만나면 끝남.

i = 1
for(i in 1:10){
  if(i%%2 == 1){
    next
  }
  print(i)
}



i = 1
for(i in 1:10){
  if(i%%2 == 1){
    i = i + 1
    next
  }
  print(i)
  i = i + 1
}
# <i = i + 1>의 위치와 
# next의 위치 꼭 알기. 시험에 나옴.
# <i = i + 1>를 2번 다 써줘야함 (중요).
# for문보다 while문이 더 까다로움.


# Page 24
# 문제 답안

# 1번
for(i in 1:100){
  if(i%%3==0)
    print(i)
}

# 2번
# 약수는 24에서 i를 나눠야 함.
for(i in 1:24){
  if(24%%i==0){
    print(i)
  }
}

# 24와 30의 최대 공약수
for(i in 1:24){
  if(24%%i==0 && 30%%i==0){
    print(i)
  }
}

# 3번
num = 0
sum = 0
for(i in 1:100){
  if(i%%3==0){
    num = num + 1   ##조건을 만족시킬 때마다 더함.
    sum = sum + i
  }
}
cat(num, sum)

# 4번
i = 1
k = 1
while(i<=5){
  k = k*i
  i = i + 1
}
print(k)

# 5번
# for문
i = 1
for(i in 1:9){
  cat(i,'X7=', i*7, '\n')
}

# while문
i = 1
while(1<=9){
  
}

# 6번
# for문
i = 1
for(i in 1:100){
  if(i%%4==0){
    print('*')
  }else{
    print(i)
  }
  i = i+1
}

# while문
i = 1
while(i<100){
  if(i%%4==0){
    print('*')
  }else{
    print(i)
  }
  i = i+1
}

# 7번
n <- nrow(airquality)
m <- 0
for(i in 1:n){
  if (airquality$Temp[i] >= 90){
    cat(airquality$Month[i], airquality$Day[i],'\n')
    m <- m+1
  }
}
print(m)