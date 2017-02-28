"""print "============= IF ELIF ==============="

print "Giai phuong trinh bac 2"

print "Nhap vao he so a: "
a = input()
print "Nhap vao he so b: "
b = input()
print "Nhap vao he so c: "
c = input()
deta = b*b - 4*a*c
if(deta < 0):
	print "Phuong trinh vo nghiem"
elif(deta == 0):
	print "Phuong trinh co nghiem kep: "
else:
	print ("Phuong trinh co nghiem kep") """
	
print "================== While else =================="

count = 0
while(count < 10):
	print "Lan thu: ", count
	count = count + 1
else:
	print "End while: ", count

print "================= FOR ========================"

for letter in 'LeDucTrung':
	print letter
arr = ['chuoi', 'tao', 'nho', 'cam']
for qua in arr:
	print "Ban thich trai: ", qua

print "Lap qua index cua day"

for index in range(len(arr)):
	print "Ban thich: ",arr[index]
	
print "So nguyen to"

for num in range(10,20):  #de lap tu 10 toi 20
   for i in range(2,num): #de lap tren cac thua so cua mot so
      if num%i == 0:      #de xac dinh thua so dau tien
         j=num/i          #de uoc luong thua so thu hai
         print '%d la bang %d * %d' % (num,i,j)
         break #de di chuyen toi so tiep theo, la vong FOR dau tien
   else:                  # else la mot phan cua vong lap
      print num, 'la so nguyen to'
	  
	  
# break, continue, pass. pass: (if(a=0) pass)-> khong cho khoi lenh thuc thi khi a = 0.
print "================ PASS ====================="
for letter in 'Python': 
   if letter == 'h':
      pass
      print 'Day la khoi pass'
   print 'Chu cai hien tai :', letter

print "Good bye!"