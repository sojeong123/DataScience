# homework1
# <1번>
# 'airquality.csv' 파일을 읽어오기
airquality_data <- read.csv("airquality.csv")

# Ozone 값이 40 이상인 데이터 필터링
ozone40_data <- airquality_data[airquality_data$Ozone >= 40,]

# 'ozone40.csv' 파일로 저장
write.csv(ozone40_data, "ozone40.csv", row.names = FALSE)

# <참고> 파일 위치를 알고싶다면 실행
getwd()

# <2번>
# <1>
# 데이터 프레임 생성
People <- data.frame(
  name = c("Olivia", "Sophia", "John", "Luna"),
  age = c(18, 23, 22, 30),
  gender = c("F", "F", "M", "F"),
  height = c(162, 158, 160, 177),
  student = c(TRUE, FALSE, TRUE, TRUE)
)

# 평균 나이 계산
mean_age <- mean(People$age)

# 평균 키 계산
mean_height <- mean(People$height)

# 결과 출력
cat("평균 나이:", mean_age, "세\n")
cat("평균 키:", mean_height, "cm\n")

# <2>
# 성별별 인원 수 구하기
gender_count <- table(People$gender)

# 결과 출력
print(gender_count)

# <3번>
# <1>
# swiss 데이터셋 불러오기 (이미 불러온 경우 생략)
data(swiss)

# Catholic이 80% 이상인 주들을 선택
selected_data <- swiss[swiss$Catholic >= 80, ]

# 선택된 주들의 남성의 농업인 비율 출력
cat("Catholic이 80% 이상인 주들의 남성의 농업인 비율:\n")
cat(selected_data$Agriculture)

# <2>
# swiss 데이터셋 불러오기
data(swiss)

# Examination이 20% 미만이고 Agriculture이 50% 미만인 주 선택
selected_data <- swiss[swiss$Examination < 20 & swiss$Agriculture < 50, c("Fertility", "Examination", "Agriculture")]

# 결과 출력
print(selected_data)

# <4번>
# 정답 설정
answer <- 25

# 반복문 시작
while(TRUE) {
  # 숫자 입력 받기
  number <- as.numeric(readline("숫자를 입력해주세요: "))
 
   # 정답 확인
  if(number < answer) {
    print("up!")
  } else if(number > answer) {
    print("down!")
  } else {
    print("정답!")
    break  # 반복문 종료
  }
}