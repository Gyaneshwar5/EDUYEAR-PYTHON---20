
a=[2,1,5,13,15,22,46,26,27]
even,odd=0,0
for i in a:
	if i%2==0:
		even+=1
	else:
		odd+=1
print(even)
print(odd)			
		


a=[2,1,5,13,15,22,46,26,27]
a.sort()
print(a[-1])
print(a[0])



list=[]
n=int(input("Enter the number: "))
for i in range(1,n+1):
	ele=int(input("enter :"))
	list.append(ele)
print(list)
list.sort()	
print(list[-1])
print(list[0])
	



a=input()
b=a[::-1]
if a==b:
	print("pallindrime")
else:
	print("no")	



n=int(input())
l=list(map(int,input().strip().split(' ')))
print("Palindrome numbers are:")
for i in l:
    num=str(i)
    if("".join(reversed(num))==num):
        print(i)
	
	

	
