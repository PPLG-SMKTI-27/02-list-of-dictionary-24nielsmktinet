#dictionary

student1 = {"nama":"faisal""asal":"samarinda"}
student2 = {"nama":"pahwi","asal":"samarinda"}        
student3 = {"nama":"fuad","asal":"samarinda"}   

#list of dictionary
student = [student1,student2,student3]
print(student)

# hitung jumlah nilai keetiga siswa tersebut, gunakan perulangan

sum = 0
for i in range (len(student)):
     sum = sum + student[i]["nilai"]
     print ("total nilai semua siswa adalah ",sum)

     # nilai rata-rata adalah jumlah semua nilai di bagi dengan banyaknya data

     ratarata = sum / len(student)
     print("nilai rata-rata siswa adalah,ratarata,ratarata")
            
 
 
 
 
 
 
