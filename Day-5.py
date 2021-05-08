
n=int(input("enter the number: "))
for a in range(0,n):
	if(a%5==0 and a%7==0):
		print(a)


num=5
sum=0
for i in range(1,num+1):
	a='2'*i
	a=int(a)
	sum += a
print(sum)	



n=int(input("Enter the number: "))
fac=1
while n>0:
	fac=fac*n
	n -= 1
print(fac)	
	 
 

st="python language is best programming language"
for i in range(len(st)):
	end_value='-'
	if st[i] == ' ' or i == len(st)-1:
		end_value=' '
	if i%2 == 0:
		print(st[i].upper(),end=end_value)
	else:
		print(st[i],end=end_value)
print()		
				
 
 
   
