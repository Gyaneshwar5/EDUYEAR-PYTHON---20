
li=['a','e','i','o','u']
string=str(input("Enter the string: "))
for i in string:
	if i in li:
		print(string.index(i))


string= str(input("enter the string: "))
words=string.split()
a=reversed(words)
print(" ".join(a))


li=[1,2,3,4,5,2,3,6,2,4]
a=[]
for i in li:
	if i not in a:
		a.append(i)
print(a)	
