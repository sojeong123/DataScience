"""
import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from keras import Sequential, Input
from keras.layers import Dense


df = pd.read_csv("C:/Users/Administrator/Desktop/1/Github/DataScience/인공신경망과 딥러닝 심화/수업시간/pima-indians-diabetes3.csv")

df = pd.read_csv("C:/Users/Administrator/Desktop/1/Github/DataScience/인공신경망과 딥러닝 심화/수업시간/pima-indians-diabetes3.csv")
head = df.head()

df.info()

df.describe()

# DataFrame(데이터프레임)   <- 2차원의 표 형태
# Series(시리즈) <- 1차원의 벡터 형태

# df. 매서드 이름()
df.head(3)

df.tail(3)

df. info()

df.describe()

df.columns
list(df.columns)

df['diabetes']

df['diabetes'].value_counts()
# 0: 정상인
# 1: 당뇨병을 걸린 사람
# class imbalance problem (클래스 불균형 문제)

df.corr()

# 히트맵 (Heat Map)
pit.figure()
sns.heatmap(df.corr(), annot=True, cmap='Reds')
pit.show()
list(df.columns)

x = df[df.columns[:8]]
y = df[df.columns[8]]

print (x)
print (y)

"""

import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from keras import Sequential, Input
from keras.layers import Dense


df = pd.read_csv("C:/Users/Administrator/Desktop/1/Github/DataScience/인공신경망과 딥러닝 심화/수업시간/pima-indians-diabetes3.csv")
"""
model = Sequential()
model. add(Input(shape = (8,)))     # 입력층 (Input Layer)
model. add(Dense(12, activation = "relu"))     # 은닉층 (Hidden Layer)
model. add(Dense(8, activation = "relu"))     # 은닉층 (Hidden Layer)
model. add(Dense(1, activation="sigmoid"))     # 출력층 (Output Layer)

model.summary()
"""
"""
model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

model.fit(x, y, epochs=100, batch_size=5, verbose=1)

# class imbalance (클래스 불균형) : 768 -> 2:1
"""
"""
pit.figure()
pit.scatter(df['plasma'], df['diabetes'])
pit.xlabel("plasma")
pit.ylabel("diabetes")
pit.show()
"""

pit.hist(x = [df['plasma'][df['diabetes']==1],  # 당뇨병 환자
              df['plasma'][df['diabetes']==0]], # 정상인
              histtype = 'barstacked')
pit.legend()
pit.grid(True)
pit.xlabel("plasma")        # 공복 상태의 혈당 수치
pit.ylabel("counts")
pit.show()