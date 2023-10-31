rm(list=ls())

a = c(1,3,5)
length(a)
b = 30:90
b[61]
length(b)

a = list(1,"a",T)
a[[3]]
a[[2]]
a[[1]]
a[2]


b = c(90,80,100)
b
names(b) = c("math","english","korean")
b
b[2]
b['english']

a
names(a) = c('j','k','l')

a = list(j=1,k=)

y = list("datascience","taewan",40)
y
names(y) = c("major","name","age")
y
y$age
x = list("major"="datascience","name"="taewan","age"=40)
x


b
x = list(name="taewan",score=b)
x
#x = list(  ,  )로
#나오면 빈칸 유추할 수 있어야 함.

x = c("A","B","A","AB","O","O")
y = factor(x)
y
y[6]
y[7] = "B"
y[8] = "C"
####################
summary(y)
levels(y)
####################

rm(list=ls())


##############################
#2주차 강의자료
#38페이지

#예시 1
d = c(100:200)
d[50]

#1점짜리 답안
d[c(1,11,21,31,41,51,61,71,81,91,101)]
#만점짜리 답안
#1부터 101까지 10씩 건너뛰기
d[seq(1,101,10)]

#
d[20]
d[c(1:20)]
#만점짜리 답안
d[1:20]


#예시 2
d = c(100:200)

length(d)
mean(d)


#d = 110
#sum(d<110)


#예제 3
x = 1:20
x
y = x[c(3,6,9,12,15,18)]
y=x[seq(3,18,3)]
y
sort(y)   #오름차순

mean(x[seq(3,18,3)])

mean(x[-seq(3,18,3)])


#예시 4
sort(y,decreasing = TRUE)
sort(y,T)
sort(y,TRUE)

y = sort(y,T)

a = c(1,6,3,8)
a
a = sort(a)
a
#sort(a)랑 a=sort(a)랑은 다른것임.


#예시 5

#예시 6
ages = c(58,20,85)
names = c("Tony", "Ahn", "Nick")
ages
names
x = list(ages,names)
x
names(x)= c("numbers","names")
x


#예시 7
x = c(1,6,8,11)
x
z = list(2*x,x/2)
z
names(z) = c("x*2","x/2")
z

#예시 8
gender = c(rep("male", 5), rep("female",10))
gender
gender_fac = factor(gender)
gender_fac
summary(gender_fac)
gender_fac[16]="male"
gender_fac
gender

?state.x77
x = c(1,2,3)
x
View(state.x77)
View(iris)


############################################
#3주차 강의자료
x = matrix(1:20,nrow=4,ncol=5)
x
View(x)
#3행 2열 = 7 이다.
x[4,5]

?matrix
y = matrix(data = 1:20,4,5)
y

z = matrix(1:18,3)
#행 개수가 3이라 당연히 6열로 출력.
z

z = matrix(1:18,ncol=3)
z

z = matrix(1:18,ncol=3, byrow = T)
z


# 매트릭스 만드는 방법
# 1
a = matrix(1:20,2,byrow=T)
a
View(a)

b = matrix(1:18,ncol=3,byrow=T)
b

c = matrix(0,3,4)
c

d = matrix("taewan",2,1)
d

x = matrix(c(168.4,174.6,169.5,181.4))
x



rm(list=ls())



a = matrix(1:20,4,5)
nrow(a)
dim(a)[1]

ncol(a)
dim(a)[2]
length(a)


x = 1:3
y = 4:6
z = cbind(x,y)
z
a = rbind(x,y)
a

rm(list=ls())


cbind(1:3, 4:6, matrix(7:12,3,2))

rbind(matrix(1:6),2,3),
matrix(7:12)2,3)

#3주차 강의자료 10페이지
x = matrix(1:20,4,byrow =T)
x = matrix(1:51,4,byrow)
x[3,4]
x
colnames(x)=c("나이","몸무게","a","b","c")
x[,"몸무게"]
rownames(x) = c("김태완","김태형","강충합","홍길동")
x("홍길동",)


#rownames, colnames, cbind, rbind 복습
