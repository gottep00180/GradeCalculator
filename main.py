#รับค่าคะแนนแต่ละวิชามา
d1 = int(input("english: "))
d2 = int(input("maths: "))
d3 = int(input("thai: "))
d4 = int(input("physics: "))
d5 = int(input("chemistry: "))
#หาค่าเฉลี่ย(Mean)
mean = (d1+d2+d3+d4+d5) / 5
#แสดงค่าคะแนนรายวิชา
#หมายเหตุ: หากยังไม่ถูกต้องลองตรวจสอบเว้นวรรคดู
print("English score ="+str(d4))
print("Maths score ="+str(d2))
print("Thai score ="+str(d3))
print("Physics score ="+str(d4))
print("Chemistry score ="+str(d5))
#แสดงค่าเฉลี่ย
print("Mean = "+str(mean))
#แสดงค่าในรูปแบบ %
#การนำไปหาร1เพื่อให้ได้ทศนิยม 1 ตำแหน่ง
#หมายเหตุ: หากยังไม่ถูกต้องลองตรวจสอบเว้นวรรคดู
print("English = "+str((d1/1))+"%")
print("Maths = "+str((d2/1))+"%")
print("Thai = "+str((d3/1))+"%")
print("Physics ="+str((d4/1))+"%")
print("Chemistry ="+str((d5/1))+"%")
