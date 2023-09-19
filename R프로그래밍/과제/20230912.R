rm(list=ls())

3+8
4*8
(90+80+35)/3

9/2
9%%2

3^4
3**4

log10(10)
factorial(3)

sample(10)
1:100
3/5

sin(pi/6)

sample(1:45, 5)

x=3
y=2
  
x+y
#alt + - = " <- "이긴 하지만 주로 "="사용

x <- 7
y <- 5
z <- "hello"

a = 'hi'

print(a)
a

x = 10
mid_score = 90
final_score = 80
avg_score = (mid_score + final_score)/2

score = 1
Score = 2
sCore = 3

final_score = 100

rm(list=ls())

name = "sojeong"
x = 100
a = TRUE
b = FALSE
c = T
D = F

x > 0


b = 5
a = "ttt"

class(b)
class(a)
c = T
class(c)

is.numeric(b)
is.character(a)

a = c("hello",2,3,4,5,6,7,10,100)
a
b = c(T,F,F,F,T,F,T)

rm(list=ls())

a = c(1,2,3)
b = c("a","b")
c = c(a,b)
c
d = c(1:100)
d = 1:100
y = c(1,2,3,90:100)
y

a = seq(from = 0, to = 100, by = 2)
a
b = seq(0,100,2)
b
?seq

b = 5:100
c = seq(0,100,length.out = 4)
c
d = seq(0,100)

name = c("taewan","tom"," jane")
a = rep(name,each = 10,length.out = 50)
a

?rep

rm(list=ls())

b= rep(c(1,5),c(3,2))
b

score = c(100,90,80)
score[2]
score[c(1,3)]

scores = c(100,90,80)
names(scores) = c("taewan","tom","jane")

score = c("taewan"=100,"tom"=90,"jane"=80)

a = 3
a = 10
b = c(1,2,3,4,5)

a = seq(1,9,2)
a
b = 2*a
b

x = c(9,4,100,0,88,23)
x
sum(x)
mean(x)
median(x)
sort(x,decreasing = F)
sort(x,decreasing = T)
sort(x,T)

a = 10
b = a > 5
a
b

c = 10
a == c
a != c
b = 1

(a > b) && (a==b)
(a > b) && (a!=b)

d = seq(1,9,2)
d
d >= 5
d[d >= 5]

#################################################
d > 5
sum(d > 5)

# d에서 5보다 큰 값을 전부 더하라.
sum(d[d>5])
# d에서 ()안의 조건을 만족하면 1,
# 만족하지 못하면 0, 그리고 그 숫자를 다 더하라.
sum(d>5)
#################################################

