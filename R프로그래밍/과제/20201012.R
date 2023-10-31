# R프로그래밍(02)
# 2023. 10. 31(화)
# 20201012 컴퓨터학과 임소정
# homework1

# <1번>
airquality_data <- read.csv("airquality.csv")
ozone40_data <- airquality_data[airquality_data$Ozone >= 40,]
write.csv(ozone40_data, "ozone40.csv", row.names = FALSE)
getwd()

# <2번>
# <1>
People <- data.frame(
  name = c("Olivia", "Sophia", "John", "Luna"),
  age = c(18, 23, 22, 30),
  gender = c("F", "F", "M", "F"),
  height = c(162, 158, 160, 177),
  student = c(TRUE, FALSE, TRUE, TRUE)
)
mean_age <- mean(People$age)
mean_height <- mean(People$height)
cat("평균 나이:", mean_age, "세\n")
cat("평균 키:", mean_height, "cm\n")
# <2>
gender_count <- table(People$gender)
print(gender_count)

# <3번>
# <1>
data(swiss)
selected_data <- swiss[swiss$Catholic >= 80, ]
cat(selected_data$Agriculture)
# <2>
data(swiss)
selected_data <- swiss[swiss$Examination < 20 & swiss$Agriculture < 50, c("Fertility", "Examination", "Agriculture")]
print(selected_data)

# <4번>
answer <- 25

while(TRUE) {
  number <- as.numeric(readline("숫자를 입력해주세요: "))
  
  if(number < answer) {
    print("up!")
  } else if(number > answer) {
    print("down!")
  } else {
    print("정답!")
    break
  }
}