#                            9-07-19
#-------------------------strings----------------------
tech="python and machine learning i am harikittu btech cse branch"
     # 0123456789012345678901234567890123456789012345678901234567890
# print(tech[10])
# print(tech[20])
# print(tech[-6])
# print(tech[-25])
# print(tech[18])
# ##print(tech[3])
# print(tech[22])
# print(tech[-10])
# print(tech[-23])
# print(tech[5])
#------------------------slicing------------------------
# print(tech[3:10])
# print(tech[1:4])
# print(tech[0:6])
# print(tech[11:18])
# print(tech[-16:-9])
# print(tech[-28:-21])
# #                           10-07-2019
##print(tech[1:3])
      
##print(tech[33:42])
##print(tech[49:52])
##

# str1="hari"
# str2="kittu"
# str3=str1 + str2
# print(str3)
stmt="python is an easy programming language"
##print(stmt[18:29])
# print(stmt[::-1])
# print(stmt[30:])
#----------------------concatination-------------------------
#joining of multiple strings
#typecasting type change

##name="hari"
##marks=70
##print(name +" "+"has secured"+" " +str(marks) +" " +"marks")
##print("%s has secured has %d marks"%(name,marks))
# tech="python"
# version=3.7
# year=2019
# print( "the version of %s is %d"%(tech,version))
# print( "the version of %s is %.1f in %d"%(tech,version,year))



#11-07-19
tech="Python and Machine Learning"
# print(tech)
# print(tech.lower())
# print(tech.upper())
# print(tech.title())
# print(tech.swapcase())
# print(tech.capitalize())


# # checking functions 

# print(tech.startswith("P"))
# print(tech.startswith("and"))


# print(tech.endswith("g"))
# n="10"
# print(n.isdigit())
# num="10a"
# print(num.isdigit())

# manipulative functions

# print(len(tech))
# print(tech.count("p"))
# print(tech.count("in"))
# print(tech.count("Python"))

stmt="python is an easy programming language"
# print(stmt.count("a"))

# print(stmt.count("a"))
# print(stmt.count("e"))
# print(stmt.count(" "))
# print(stmt.count("an"))
# print(stmt.count("and"))


# print(stmt.index("a"))
# print(stmt.index("is"))
# print(stmt.index("easy"))
# print(stmt.index("n"))
# print(stmt.index(" "))
# print(stmt.index(" ",7))
# print(stmt.index(" ",10))
# print(stmt.index(" ",13))
# print(stmt.index(" ",18))
# print(stmt.index(" ",))
# print(len(stmt))




# replace

# print(stmt.replace("python","java"))

# print(stmt.replace("p","j"))


# print(stmt.replace("a","__"))
#print(stmt.split("e"))

# print(stmt.replace("i","hari"))

					# 12-07-19


# print(stmt.split())
# print(stmt.split("an"))
# print(stmt.split("is"))
# # print(stmt.split("and"))
# words=stmt.split(" ")
# print("@".join(words))

stmt1="      python is an progmming     " 
# print(stmt1.strip()) 
# print(stmt1.strip(" p"))
# print(stmt1.lstrip(" p"))  
# print(stmt1.rstrip(" ing")) 


# membership operators

# print("an" in stmt1)
# print("is" not in stmt1)


# a = 2
# b = 330

 
# if a > b:
# 	print("A")
# else: 
# 	print("B")


# 13-07-19

# a=int(input("enter a number1:"))
# b=int(input("enter a number2:"))
# print(a+b)


# first task
# a=input("enter a name:")
# b=input("enter a company name:")
# c="@"
# d=".com"
# print(a+c+b+d)




# second task
# a=input("enter a stmt:")
# print(a)
# b=input("enter a char to search:")
# print(b)
# print(b in a)
# print(a.count(b))
 # third task

# a=input("enter a stmt:")
# print(a)
# b=input("enter an old word:")
# print(b)
# c=input("enter new word to replace:")
# # print(c)
# print(a.replace(b,c))



# conditional statements
# if else statement
# exp1
# a=10
# if a>1:
# 	print("hari")
# else:
# 	print("kittu")

# example2
# a=4
# if a>5:
# 	print("hello")
# elif a==10:
# 	print("hi")
# elif a>6:
# 	print("bye")
# else:
# 	print("none")

# exp3
# elif
# a=10
# b=20
# c=30
# if a>b:
# 	print("a is big")
# elif a>c:
# 	print("a is big")
# elif b>c:
# 	print("b is big")
# else:
# 	print("c is big")



# a=int(input("enter an input"))

# print(a)

# print(a**2)


# b=input("enter an input:")
# print(b)
# print(len(b))


# a=input("enter an input")
# print(a)
# if a.isdigit():
# 	b=int(a)
# 	print(b**2)
# else:
# 	print(len(a))



 # task for khan sir
# task one 
# a=int(input("enter a number"))
# print(a)
# if a%3==0 | a%5==0:
# 	print("%d is divisible by 3 and 5"%a)
# elif a%3==0:
# 	print("%d is multible of 3 only"%a)
# elif a%5==0:
# 	print("%d is multible of 5 only"%a)
# else:
# 	print("%d is not multible of 3 and 5"%a)

#task two

# hh=int(input("enter  hh:"))
# mm=int(input("enter mm:"))
# ss=int(input("enter ss:"))
# ff=input("enter am or pm:")
# print("%d:%d:%d %s"%(hh,mm,ss,ff))

# if ff=="am":
# 	print("%d:%d:%d"%(hh,mm,ss))
# else:
# 	print("%d:%d:%d"%(hh+12,mm,ss))
 	
# else:
# 	c=a.rstrip("pm")
# 	print(c)
# 	print(type(c))


# 15-07-19

# a=int(input("enter a number:"))
# print(a)
# if a%2==0:
# 	print("even")
# else:
# 	print("odd")
# a=input("enter a number:")
# if a.isdigit():
# 	a= int(a)
# 	if a%2==0:
# 		print("even")
# 	else:
# 		print("odd")
# else:
# 	print("enter only integer number")


# for i in range(10):
# 	print(i)

# for i in range(1,20,3):
# 	print(i)

# for i in range(50,100,5):
# 	print(i)

# for i in range(10,0,-1):
	# print(i)
# for i in range(100,50,-5):
# 	print(i)

# increment pattern
# n=int(input("enter a number:"))
# for i in range(1,n+1):
# 	print("*" * i)

# decrement pattern
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
# 	print("*" * i)

# increment number pattern
# n=int(input("enter a number:"))
# for i in range(1,n+1):
# 	print(str(i) *i)

# task1
# start=int(input("enter starting number:"))
# end=int(input("enter ending  number:"))
# if start>end:
# 	for i in range(start,end,-1):
# 		if i%2==0:
# 			print(str(i)+"is even")
# 		else:
# 			print(str(i)+"is odd")
# else:
# 	for i in range(start,end,1):
# 		if i%2==0:
# 			print(str(i)+"is even")
# 		else:
# 			print(str(i)+"is odd")
# task2
# def alp(n):

	# n=int(input("enter a number:"))
	# N=65
	# for i in range(1,n):
	# 	for j in range(0,i+1):
	# 		ch = chr(N)
	# 		print(ch, end="")
	# 		N=N+1s
	# 		print("\r")
# n=5
# alp(n)
# n=int(input("enter a number"))
# alp='A'
# for i in range(1,int(n)-'A'+1,1):
# 	for j in range(1,j<=i,1):
# 		print("alp")
# alp=alp+1


# def alphapat(n):
# 	num = 65
# 	for i in range(0, n): 
# 		for j in range(0, i+1): 
# 			ch = chr(num) 
# 			print(ch, end=" ") 
# 		num = num + 1
# 		print("\r") 
# n = 6
# alphapat(n) 


# n=int(input("enter a number"))
# num = 65
# for i in range(0, n): 
# 	for j in range(0, i+1): 
# 		ch = chr(num) 
# 		print(ch, end=" ") 
# 	num = num + 1
# 	print("\r") 

# new one task 
# for i in range(n):
# 	print((chr(97+i)+" ")*(i+1))

# 16-07-19
# string="abcdefg"
# n=5
# for i in range(n):
# 	print(string[i]*(i*1))

# 
# number programming
# n=int(input("enter a number:"))
# c=0
# for i in range(1,n):
# 	if n%i==0:
# 		print(i)
# 		c=c+1
# if c>2:
# 	print("composite")
# else:
# 	print("prime")

# prime and composite in the give range

# s=int(input("enter a starting index:"))
# e=int(input("enter a ending index:"))
# for j in range(s,e+1):
# 	c=0
# 	for i in range(1,j+1):
# 		if j%i==0:
# 			# print(i)
# 			c=c+1
# 	if c>2:
# 		print(str(i)+"composite with "+str(c)+"factors")
# 	else:
# 		print("prime")

# pattern in numbers 1 12 123 1234
# n=int(input("enter a range:"))
# for j in range(1,n+1):
# 	for i in range(1,j+1):
# 		print(i,end="")
# 	print()
# # output
# 1
# 12
# 123
# 1234
# 12345

# n=int(input("enter a range:"))

# for i in range(1,n+1):
# 	for j in range(ord("a"), ord("a")+i):
# 		print(chr(j),end="")
# 	print()


# output
# a
# ab
# abc
# abcd
# abcde


# n=int(input("enter a range:"))
# for j in range(n,0,-1):
# 	for i in range(1,j+1):
# 		print(i,end="")
# 	print()


# output
# 12345
# 1234
# 123
# 12
# 1

# n=int(input("enter a range"))
# for i in range(n,0,-1):
# 	# for j in range(1,i):
# 	print("*"*i)
# print()
# output
# *****
# ****
# ***
# **
# *

# n=int(input("enter a range"))
# for i in range(1,n+1):
# 	print(" "*(n-i) + "*" *i)

# output
#     *
#    **
#   ***
#  ****
# *****
# n=float(input("enter a number"))
# print(n)
# print(type(n))


# 19-07-19
# while loop
# a=1
# while a<10:
# 	print(a)
# 	a=a+1

# multibles of 3
# s=int(input("enter a starting value:"))
# e=int(input("enter a ending value:"))
# while s<e:
# 	if s%3==0:
# 		print(s)
# 	s=s+1

# a=10
# while a>0:
# 	print(a)
# 	a=a-1	
# count the number of occurence 

# stmt="python is an easy programming language"
# c= "n"
# count=stmt.count(c)
# ind=-1
# while count>0:
# 	ind=stmt.index(c,ind+1)
# 	print(ind)
# 	count=count-1

# task for table for khan
# n=int(input("enter a table:"))
# for i in range(1,11):
# 	print(n,"X",i,"=",n*i)


# n=int(input("enter a value:"))
# n=20
# l=len(str(n**3))
# for i in range(0,n+1):
# 	print("%s %s %s"%(str(i).zfill(l),str(i**2).zfill(l),str(i**3).zfill(l)))

# 22-07-19
stmt="python is easy"
# for i in stmt:
# 	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":

# 		print(i)

# vowels ="aeiou"
# for i in stmt:
# 	if i.lower() in vowels:
# 		print(i)
# for i in stmt:
# 	print(i , stmt.index(i))


# control statements
# pass 
# break
# continue

# pass
# a=1
# if a>5:
# 	pass
# else:
# 	print("a lt 5")


# for i in range(10):
# 	pass


# break

# for i in range (10):
# 	print(i)
# 	if i==5:
# 		break
# stmt ="python is easy "
# for i in stmt:
# 	if i=="n":
# 		break
# 	print(i)

# continue

# for i in range(10):
# 	if i==5:
# 		continue
# 	print(i)


# task for khan

# n=int(input("enter a value:"))
# m=int(input("enter an multible value:"))
# for i in range(1,n+1):
# 	if i%m==0:
# 		print(i)
# 		continue


# 23-07-19

# COLLECTIONS

# list
tech=["py","mysql",3.7,8,"pip",19,"java"]

# print(tech)
# slicing part
# print(tech[2:3])
# print(tech[:3])
# tech[3]=100
# print(tech)
# tech[4]="hyd"
# print(tech)
# tech[0]=200
# print(tech)

# tech[1:3]='aa','bb'
# print(tech)
# tech[4:]=100,200,300,00
# print(tech)

# clas task
# tech=[1,2,3,4,5,6,7,8,9,10]
# print(tech)
# index=int(input("enter a index value"))
# print(index)
# if len(tech)>index:
# 	new=input("enter a new element to replace")
# 	print(new)
# 	tech[index]=new
# 	print(tech)
# else:
# 	print("enter correct index")

# tech=["py","mysql",[3.7,[8,"oracle"],90,74,"pip"],19,["java",100],200,300]
# print(tech)
# print(tech[2][2])
# print(tech[1])
# print(tech[2][2])
# print(tech[2][1][1])
# print(tech[4][0])
# print(tech[4][1])
# print(tech[2][4])

# task for khan 
# ll=[[1,[4,[5,[6,7,8,9,[10]]]]]]

# print(ll[0][1][1][1][4][0])

# 24-07-19

tech=["py","mysql",3.7,8,"pip",19,"java",100,200,300]
# print(tech)
# del tech[3]
# print(tech)
# del tech[7:9]
# print(tech)

# for i in tech:
# 	print(i)


# tech.append("hyd")
# print(tech)
# tech.append(1000)
# print(tech)

# tech.insert(0,"hari")
# print(tech)
# tech.insert(2,"kittu")
# print(tech)
# # ask jaggu
# tech.insert(4,530)
# print(tech)

# del tech[tech.index("pip")]
# print(tech)


# tech.remove("py")
# print(tech)
# tech.remove(8)
# print(tech)

# class task khan 
# tech=["py","mysql",3.7,8,"pip",19,"java",100,200,300]
# print(tech)
# print("1.add")
# print("2.remove")
# add=int(input("enter an operation:"))
# if add<=2:
# 	if add==0:
# 		print("enter valid option")
# 	if add==1:
# 		element=input("enter an element:")
# 		tech.append(element)
# 		print(tech)
# 	elif add==2:
# 		element=input("enter an element:")
# 		if element.isdigit():
# 			# if element in tech:
# 			element=int(element)
# 			tech.remove(element)
# 			# else:
# 				# print(element,"element not found")
# 		print(tech)
# else:
# 	print("enter valid option")


# second task
# lst=[]
# n=int(input("enter an number:"))
# for i in range(1,n+1):
# 	ele=i*10
# 	lst.append(ele)
# 	print(lst)

# 3rd task
# lst=[]
# n=int(input("enter an number:"))
# for i in range(0,n+1):
# 	lst.append(chr(65+i))
# print(lst)

# 25-07-19

tech=["py","mysql",3.7,8,"pip",19,"java",100,200,300]
l1=[1,2,3,4,5,6,6,7,8,8,3,4,99,455,6,6,9,7,8,8]
# tech.extend(l1)
# print(tech)
# print(l1)

# l2=tech+l1
# print(l2)
# print(tech)
# print(l1)


# sort the list assinding
# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# decending sort
# l1.sort(reverse=True)
# print(l1)

# tech=["hi","kittu","cse","it","ece"]
# tech.sort()
# print(tech)
# tech.reverse()
# print(tech)

# class task
# reptitation delete
# l1=[1,1,4,2,6,6,3,3,4,445,6,8,9,0,0,1,44,55,66,7,77]

# print(l1)
# op=[]
# for i in l1:
# 	if i not in op:
# 		op.append(i)
# op.sort()
# print(op)
# task 2 class

# tech=["py","mysql",3.7,8,"pip",19,"java",100,200,300]
# ints=[]
# strs=[]
# fl=[]
# for i in tech:
# 	if  type(i) is int:
# 		ints.append(i)
# 	elif type(i) is float:
# 		fl.append(i)
# 	else:
# 		strs.append(i)
# print(ints)
# print(strs)
# print(fl)

# task 2 class
# stmt=input("enter a statements:")
# char=str(input("enter character:"))
# stmt2=[]
# for i in stmt:
# 	if ord(i)>ord(char):
# 		stmt2.append(i)
# stmt2.sort()
# print(stmt2)

# lst1=[10,20,40,30,40]

# lst2=[1,2,3,4]
# lst1=[]
# lst2=[]
# range1=int(input("enter range of lists"))
# for i in range(0,range1):
# 	a=int(input("enter first list:"))
# 	lst1.append(a)
# print(lst1)
# for i in range(0,range1):
# 	b=int(input("enter second list:"))
# 	lst2.append(b)
# print(lst2)
# res=[]
# for i in range(len(lst1)):
# 	res.append(lst1[i]+lst2[i])
# print("result list is:",res)

# lst=[]
# n=int(input("enter a length of list:"))
# for i in range(1,n+1):
# 	a=int(input("enter a list numbers:"))
# 	lst.append(a)
# print(lst)

# 31-07-19
# class tasks1
# lst=[]
# n=int(input("enter number:"))
# for i in range(n):
# 	lst.append(i)
# print(lst)

# class task2
# lst=[]
# n=int(input("enter a number:"))
# for i in range(n):
# 	if i%2==0:
# 		lst.append(i)
# print(lst)
# task3
# lst=[]
# n=int(input("enter a number:"))
# for i in range(n):
# 	lst.append(i**2)
# print(lst)
# task4
# lst=[]
# n=int(input("enter a number:"))
# for i in range(n+1):
# 	if i%2==0:
# 		lst.append(i**2)
# print(lst)

# list comprehensions

# n=int(input("enter a number:"))
# nums=[i for i in range(n+1)]
# print(nums)

# task5
# stmt=input("enter a statements:")
# char=str(input("enter character:"))
# stm=[i for i in stmt if ord(i)>ord(char)]
# print(stm)

# task6
# stmt=input("enter a statements:")
# words=[i for i in stmt.split() if len(i)>5]
# print(words)

# task7
# tech=["py","mysql",3.7,8,"pip",19,"java",100,200,300]
# index=[1,3,4,5,6,8,9]
# ans=[tech[i] for i in index]
# # for i in index:
# # 	ans.append(tech[i])
# print(ans)



# start=10#int(input("enter starting value:"))
# end=20 #int(input("enter ending value:"))
# prime=[]
# comp=[]
# c=0
# for i in range(start,end+1):
# 	for j in range(1,i+1):
# 		if i%j==0:
# 			#prime.append(i)
# 			c= c+1
# 	if c>2:
# 		prime.append(i)
# 	else:
# 		comp.append(i)
		
# print(prime,"composite")
# print(comp,"prime")

# prime=[x for x in range(10,20) for y in range(2,x) if x%x==0 and x%1==0 and x%y!=0]
# print(prime)

# list1=[]
# list2=[]
# c=0
# start=int(input("enter starting value:"))
# end=int(input("enter ending value:"))
# for num in range(start,end):
#     for i in range(2,num):
#         if num%i==0:
#         	c=c+1
#         	# list2.append(num)
#     if c>2:
#     	list1.append(num)
#     else:
#     	list2.append(num)
# print(list1)
# print(list2)

# 2-08-19
# ans=[]
# tech=["py","mysql",3.7,8,"pip",[19,"java"],100,200,300]
# for i in tech:
# 	if type(i) is list:
# 		for j in i:
# 			ans.append(j)
# 	else:
# 		ans.append(i)
# print(ans)

# stmt=input("enter a statement:")
# char=[]
# for i in stmt.split():
# 	char.append([j for j in i])
# print(char)
# l1=[0,1,2,3,4,5,6,7,8,9,10]
# s=0
# mul=1
# for i in range(len(l1)):
# 	if i%2==0:
# 		s=s+l1[i]
# 	else:
# 		mul=mul*l1[i]

# print(s)
# print(mul)

# tuples
# <tuplename>=(ele1,ele2,.....ele n)
# num=(12,15,14,1,'kittu','hk','ha',9,9,6,6)
# # print(num)
# # print(type(num))
# print(num[1:2])
# print(num[1:7])
# print(num[:9])

# fee=(10,20,30,40,50)
# print(fee)
# fee=list(fee)
# print(fee)
# fee=tuple(fee)
# print(fee)
# task its only for one depth 
# num=(10,[20,30,405],"py","mysql",8,("pip",34,4,5),4,65,(6,432),2,3)
# op=[]
# for i in num:
# 	if type(i) is int or type(i) is str:
# 		op.append(i)
# 	else:
# 		for j in i:
# 			op.append(j)

# op=tuple(op)

# print(op)
# task2 tuple

# output=[(10, 1), (20, 2), (30, 3), (40, 4), (50, 5)]

# fee=[10,20,30,40,50]
# nums=[1,2,3,4,5]
# op=[]
# if len(fee)==len(nums):
# 	a=[]
# 	for i in range(len(fee)):
# 		a.append(fee[i])
# 		a.append(nums[i])
# 		op.append(tuple(a))
# 		a.clear()
# else:
# 	print("list length not equal")
# print(op)
# print(a)
# op=[]
# stmt="python is an easy language"
# a=stmt.split()
# print(a)
# for i in range(a):
# 	op.append(a[i])
# print(op)

# palindrome 
# x = input("enter a string :")
# w = "" 
# for i in x: 
#     w = i + w 
# if (x==w): 
# 	print("YES") 
# elif(x!=w):
# 	print("not")

# tuple-->list modify --->list--->tuple
# tuple-->lists 	list() 
# list--->tuple 	tuple()


# from collections import Counter
# list = [1,2,3,4,1,2,6,7,3,8,1]
# cnt = Counter(list)
# print(cnt.most_common())

# 07-08-19

# nums={10:100,1:20,30:200,40:300}
# print(nums)
# print(type(nums))

tech={"python":3.7,"tech":"mysql","sql":10,"sqllite":"10g"}
# print(tech)
# print(tech["sql"])
# for i in tech.keys():
# 	print(i)


# for i in tech.values():
# 	print(i)

# for i in tech.items():
# 	print(i)
# tech={"python":3.7,"tech":"mysql","sql":10,"sqllite":"10g",10:"php"}

# <dictname>[<key>]=<new val>
# tech["sql"]="str"
# print(tech)
# tech["python"]=2.7	
# print(tech)


# tech[30]="php"
# print(tech)
# tak1
# num=int(input("enter a number:"))
# sq={}
# for i in range(1,num+1):
# 	sq[i]=i**2
# print(sq)
# output
# enter a statement:python is easy lanuage
# {'python': 6, 'is': 2, 'easy': 4, 'lanuage': 7}

# num=input("enter a statement:")
# sq={}
# for i in num.split():
# 	sq[i]=len(i)
# print(sq)
# print(a)
# enter a statement:python
# {'p': 'q', 'y': 'z', 't': 'u', 'h': 'i', 'o': 'p', 'n': 'o'}
# num=input("enter a statement:")
# sq={}
# for i in num:
# 	sq[i]=chr(ord(i)+1)
# print(sq)

# l1=[i for i in range(10)]
# l2=[i for i in range(10,20)]
# l3={}
# if len(l1)==len(l2):
# 	for i in range(len(l1)):
# 		l3[l1[i]]=l2[i]
# print(l3)
# a=zip(l1,l2)
# print(a)
# print(tuple(a))
# print(list(a))
# print(dict(a))

# l = "python is an easy language and ajhskajl shjOracle 11g/12c"
# output= []
# l = l.split()
# n = len(l)
# for i in range(0,n-1):
# 	a = []
# 	a.append(l[i])
# 	a.append(l[i+1])
# 	output.append(tuple(a))
# 	# a.clear()
# print(output)
# # print(a);7
# 8-8-19
# functions in dict
tech={'python': 6, 'is': 2, 'easy': 4, 'lanuage': 7}
# print(len(tech))
# tech.pop("easy")
# print(tech)
# tech.popitem()
# print(tech)
# tech.clear()
# print(tech)
nums={'p': 'q', 'y': 'z', 't': 'u', 'h': 'i', 'o': 'p', 'n': 'o'}
tech={'python': 6, 'is': 2, 'easy': 4, 'lanuage': 7}

# tech.update(nums)
# print(tech)

# dict comprehensions
# d={i:i**2 for i in range(10)}
# print(d)
# stmt="python is easy programming language"
# d={i:len(i) for i in stmt.split() if len(i)>4}
# print(d)

# sets
# syntax
# <setname>={<ele1>,<ele2>......<elen>}
# <setname>=set([<ele1>,<ele2>......<elen>])
# num={10,203,304,405,10,12,11,21,11,22}
# print(num)
# print(type(num))


# model 1 tasks1
# a={1:'a',2:'b'}
# for i in a.values():
# 	print(i)

# a=input("enter a statement:")
# for i in a:
# 	s=a.split(',')
# if a=="!@#$%^&":
# 	print(a)

# functions
# print(s)
# def hi():
# 	print("hi hello!!!")
# hi()
# def hi():
# 	print("hello")
# hi()
# def hello(name):
# 	print("hello "+ name)
# hello("hari")
# def avg(n1,n2,n3,n4,n5):
# 	n6=(n1+n2+n3+n4+n5)//5
# 	print(n6)
# n1=int(input("enter 1 number:"))
# n2=int(input("enter 2number:"))
# n3=int(input("enter 3 number:"))
# n4=int(input("enter 4 number:"))
# n5=int(input("enter 5 number:"))
# avg(n1,n2,n3,n4,n5)

# 19-08-19

# def addnums(num1,num2):
# 	add=num1+num2
# 	print(add)
# 	sub=add-num2
# 	print(sub)
# 	mul=num1*num2
# 	print(mul)
# 	div=mul//num2
# 	print(div)
# addnums(30,60)


# def add(num1,num2):
# 	add=num1+num2
# 	return add
# def sub(num1,num2):
# print("1.registered ")
# print("2.change password")
# opp=int(input("enter a option:"))
# dic={}
# if opp==1:
# 	def check(name):
# 		names=list(dic.keys())
# 	if name in names:
# 		return 1
# 	else:
# 		return 0

# 	def reg(name,password):
# 		if check(name)==0:
# 			dic[name]=password
# 			print(name+  "  has been registered")
# 		else:
# 			print("user alreay exists")
# else:

# 	def getpwd(name):
# 	if check(name)==1:
# 		print(dic[name])


# check("hari",1234)
# reg("hari2",215)
# reg("kittu",1235)
# getpwd("hari2")


# def makecake(flav="",wei="",shape=" "):
# 	print("flavor "+flav + "weight   " +str(wei)+ 	"shape   " +shape)
# 	print
# makecake("vannila",3,"square")
# makecake("vannila","square")
# makecake(3,"square")

# def avg(*args):
# 	print(args)
# 	print(type(args))
# avg(10,20)
# avg(10,20,30)

# def avg(*args):
# 	res=sum(args)//len(args)
# 	print(res)
# avg(10,20,30)

# def avg(a,b,*args):
# 	res=(a+b+sum(args))//(len(args)+2)
# 	print(res)
# avg(10,20,30)
# avg(10,20,30,40)
# avg(10,20)

# for i in range(4):
# 	for j in range(i+1):
# 		print("&*",end="")
# 	print()

# 22-08-19
# 23-08-19
# map()
# l1=[i for i in range(10)]
# print(l1)
# def square(n):
# 	return n**2
# op=map(square,l1)
# print(op)
# print(list(op))


# stmt="python is easy"
# def le(b):
# 	return len(b)
# mo=map(le,stmt.split())
# print(list(mo))

# sum of two lists
# l1=[10,20,30,40]
# l2=[1,2,3,4]
# print(list(map(lambda a,b:a+b,l1,l2)))

# filter()
# stmt="python is easy"
# print(list(filter(lambda i:len(i)>2,stmt.split())))



# 26-08-19
# file handiling

# with open("demo.txt","a")as fo:	
# 	fo.write(input("enter name:"))
# 	fo.write("    ---   ")
# 	fo.write(input("enter password:   "))
	# fo.write("\n")

# with open("demo.txt","r")as f1:
# 	read=f1.readlines()
# for i in read:
	# print(i)

# 27-08-19
# with open("demo.txt","r")as fo:
	# print(fo.read(4))
	# print(fo.readline())
	# print(fo.readlines(4))
	# print(fo.read())
	# print(fo.readline(3))
# stmt=input("enter a user name:")
# pas=input("enter a password:")
# with open("demo.txt","a")as fo:	
# 	fo.write(stmt)
# 	fo.write("    ---   ")
# 	fo.write(pas)
# 	fo.write("\n")


	# print(fo.readline())


# def writeonfile(a):
# 	pwd=input("enter a user password:")
# 	fo=open("demo.txt","a")
# 	fo.write(a)
# 	fo.write("-")
# 	fo.write(pwd)
# 	fo.write("\n")
# 	print(user+" "+pwd+"  user has registered sucessful.")
	
# def task():
# 	fo=open("demo.txt","r")
# 	userpwd=fo.readlines()
# 	user=input("enter user name:")
# 	# print(userpwd)
# 	user1=[]
# 	for i in userpwd:
# 		a=i.split("-")
# 		user1.append(a[0].rstrip)
# 	# user1.append(userpwd.split("-")[0])
# 		if user in user1:
# 			print("user already exits ")
# 			return 0
# 		else:
# 			print("add user name and password")
# 			writeonfile(user)
# 			return 1
# task()


# import random 
# print("1.chars\n2.numbers")
# n=int(input("enter ur choice:"))
# l=int(input("enter a length:"))
# if n==2:
# 	for i in range(l):
# 		print(random.randint(0,10))
# else:
# 	print(random.randint(10))




# import os
# print(os.name)
# print(os.getcwd())
# print(os.chidr("C:\Users\ROJA\Desktop"))# used to change dir
# print(os.listdir()) #list of all the dir 

# os.mkdir("hari")
# os.makedirs("d1/d2/d3")

# os.rmdir("hari")
# os.removedirs("d1/d2/d3")
# print(os.path.split("C:\\Users\\ROJA\\Desktop\\PERSIONAL")
# splitext()

# 04-09-19
# class company:
# 	cname="hari"
# 	cadd="hyd"
# 	emp_count=10
# 	def add(self,a,b):
# 		print(self)
# 		res=a+b
# 		print(res)
# emp1=company()
# emp2=company()
# print(emp1)
# emp1.add(100,200)
# emp2.add(20,30)


# class company:
# 	cname="hari"
# 	cadd="hyd"
# 	emp_count=10
# 	def __init__(self,name,role):
# 		print("hello"+name)
# 	def printer(self):
# 		print("name of the emp is "+name)
# 		print("role of the emp is "+role)
# 		company.emp_count=company.emp_count + 1
# 		print(company.emp_count)
# 		print("company name is "+company.cname)
# 		print

# emp1.company("hari","pd")
# emp2=company("kitty","hk")
# emp1.printer()


# class car:
# 	curr_speed=0
# 	def __init__(self,name,model):
# 		self.name=name
# 		self.model=model

# 	def start(self,sspeed):
# 		self.curr_speed=sspeed
# 	def acc(self,aspeed):
# 		self.curr_speed=self.curr_speed + aspeed
# 	def brake(self,bspeed):
# 		self.curr_speed=self.curr_speed - bspeed
# 	def stop(self):
# 		self.curr_speed=0

# 	def printer(self):
# 		print("car name is "+self.name)
# 		print("car model is "+str(self.model))
# 		print("car speeed is "+str(self.curr_speed))

# c1=car("hari",2369)
# c1.start(30)
# c1.stop()
# c1.acc(60)
# c1.brake(40)
# c1.printer()

# with open("demo.txt","a")as fo:
# 	fo.write(input("enter a user name:"))


# import random
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8
# p =  "".join(random.sample(s,passlen ))
# print (p)
# import random
# with open("demo.txt","a")as fo:
# 		usr=input("enter user name:")
# 		fo.write(usr)
# 		fo.write("---")
# 		for i in range(2):
# 			a="01234567890"
# 			passl = 4
# 			b = "".join(random.sample(a,passl))
# 			c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 			passla = 4
# 			d = "".join(random.sample(c,passla))
# 			fo.write(b)
# 			fo.write(d)
# 		fo.write("\n")
# 		with open("demo.txt","r")as ff:
# 			for line in ff:
# 				f1=line.split("---")
# 				# print(f1)
# 				f2=f1[1]
# 				print(f2)
# 				# f3=f1[0]
# 				# if usr in f3:
# 				# 	print("user already exits!!")
# 			# print(f2)


# class fun:
# 	# print("function")
# 	def fun():
# 		print("hari")
# 	def _fun1():
# 		print("function1")
# 	def __fun2():
# 		print("function2")
# f1=fun
# print(f1._fun__fun2())



# 11-09-19

# def revrange(n):
# 	i=n
# 	while i < n+1:
# 		yield i**2
# 		i=i-1
# 		if i==0:
# 			break

# for i in revrange(20):
# 	print(i)

# 13-09-19


# print("N/A")


