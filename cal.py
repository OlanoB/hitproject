#calculator
#recursion or recursive
print ("\n	INDEX\n""\n	C=1 for addition\n""\n	C=2 for substraction\n""\n C=3 for multiplication\n""\n C=4 for division\n""\n	C=5 for to find modulus\n""\nC=6 to find factorial\n")
C=input("Enter your choice here: ")
def add(x,y):
	c=x+y
	print (x,"+",y,"=",c)
def sub(x,y):
	c=x-y
	print (x,"-",y,"=",c)
def mul(x,y):
	c=x*y
	print (x,"*",y,"=",c)
def div(x,y):
	c=x/y
	print (x,"/",y,"=",c)
def mod(x,y):
	c=x%y
	print (x,"%",y,"=",c)
if C==6:
	def f(n):
		if n==1:
			print (n)
			return n
		else:
			print (n,"*",)
			return n*f(n-1)
	n=input("enter your no here: ")
	print (n)
if C==1:
	a=input("Enter your first no here: ")
	b=input("Enter your second no here: ")
	add(a,b)
elif C==2:
	a=input("Enter your first no here: ")
	b=input("Enter your second no here: ")
	sub(a,b)
elif C==3:
	a=input("Enter your first no here: ")
	b=input("Enter your second no here: ")
	mul(a,b)
elif C==4:
	a=input("Enter your first no here: ")
	b=input("Enter your second no here: ")	
	div(a,b)
elif C==5:
	a=input("Enter your first no here: ")
	b=input("Enter your second no here: ")
	mod(a,b)
