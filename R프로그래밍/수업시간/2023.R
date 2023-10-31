rm(list=ls())
a = 3

print(a)


cat("안녕하세요")
cat("저는")

a = 1
b = 2
cat("a")
cat("b")

cat('a의 값은', a, '입니다.','그리고 b의 값은', b, '입니다')

age = c(28, 17, 35, 46, 23, 67, 30, 50)
young = min(age)

age
print(age)
cat(age)

old = max(age)
old
print(old)
cat(old)


a = dlgInput('숫자 하나 입력하시오.')$res
is.numeric(a)
is.character(a)

a = as.numeric(a)
a+1
print(a+1)
as.matrix(b)
as.data.frame(b)




id = dlgInput('이름을 입력하시오.')$res
id





install.packages('svDialogs’)
library(svDialogs)

height = dlgInput('키 입력(cm)')$res
weight = dlgInput('몸무게 입력(kg)')$res

height = as.numeric(height)
weight = as.numeric(weight)

height = height/100






getwd()
setwd()


data = read.csv('airquality.csv')
data = read.csv('airquality.csv', header = T)
?read.csv
View (data)
name = c('tony', 'alex')
age = c(30, 20)
data = data.frame(name, age)

View(data)
write.csv(data, '20231010.csv', row.names = F)

x = subset(iris, Species == 'setosa')
View(x)
View(iris)
write.csv(x, 'myiris.csv', row.names = F)
View(x)

install.packages('xlsx')
remove.packages('xlsx')
library(xlsx)
rm(list=ls())


data = read.xlsx()

write.csv(data, '20231010')




rm(list=ls())

a = read.table('read_tab.txt', fileEncoding("CP949"))
View(a)


View(airquality)
a = subset(airquality, Temp >= 60)
View(a)
View(airquality)

write.table(a, '')