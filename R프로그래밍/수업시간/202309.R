View(a)
View(airquality)

write.table(a, 'yyy.txt', append = T)


rm(list=ls())

sink('alex.txt', append = F)
print("화요일")
sink()

a=1