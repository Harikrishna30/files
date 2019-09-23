# task 1 conditional statements
# n=int(input("enter total marks:"))
# if n>=90:
# 	print("%d A grade very good"%(n))
# elif n>=60:
# 	print("%d B grade good"%(n))
# elif n>=40:
# 	print("%d C grade poor"%(n))
# else:
# 	print("%d fail"%(n))


# task 2 conditional statements

# n=int(input("enter a year:"))
# if n%4==0:
# 	 print("%d LEAP year"%(n))
	# if n%100==0:
	# 	print("%d LEAP year"%(n))
	# 	if n%400==0:
	# 		print("%d LEAP year"%(n))
	# 	else:
	# 		print("%d not LEAP year 400"%(n)) 
	# else:
	# 	print("%d not leap year 100"%(n))
# else:
# 	 print("%d not leap year 4 "%(n))


# task 3 conditional statements

# n=int(input("enter a number"))
# if n%2==0:
# 	print("%d even"%(n))
# else:
# 	print("%d odd"%(n))

# task 5 conditional statements
# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# c=int(input("enter c number:"))
# if a>b&a>c:
# 	print("%d a is big"%(a))
# elif b>c:
# 	print("%d b is big"%(b))
# else:
# 	print("%d c is big"%(c))

# string 1st task
# stmt="pythonbestforbeginners"
# print(stmt[1:23:2])

# # 2nd task string
# print(stmt[::-1])
# st=split("")

# loops tasks
# febinocci series
# a=0
# b=1
# n=int(input("enter the range:"))
# for i in range(0,n+1):
# 	print(a,end=" ")
# 	c=a+b
# 	a=b
# 	b=c

# prime number
# c=0
# n=int(input("enter a number:"))
# for i in range(1,n):
# 	if n%i==0:
# 		# print(i)
# 		c=c+1
# if c>2:
# 	print("not prime")
# else:
# 	print("prime")

# amstrong number

# n=int(input("enter a number:"))
# le=len(str(n))

# sum=0
# temp=n
# while temp>0:
# 	rem=temp%10
# 	sum+=rem**le
# 	temp=temp//10
# if n==sum:
# 	print(n,"is an amstrong")
# else:
# 	print(n,"is not amstrong")
# sum of digits

# n=int(input("enter a number:"))
# sum=0
# tem=n
# while tem!=0:
# 	rem=tem%10
# 	sum=sum+rem
# 	tem=tem/10
# print("sum of digit %d"%(sum))


# multibles of 9
# s=int(input("enter a starting value:"))
# e=int(input("enter a ending value:"))
# while s<e:
# 	if s%9==0
# 		print(s)
# 	s=s+1


# import mysql.connector

# mydb = mysql.connector.connect(host="localhost",user="hari",passwd="hari")
# mycursor = mydb.cursor()
# mycursor.execute("show databases")
# for i in mycursor:
# 	print(i)

# age=int(input("what is your age? "))
# age1=7*age
# print("if you were a dog, you'd be %d!!"%(age1))
# print('''o____
#  ||||''')

# print('ha '*4)
# print('ba' + 'na' *2)
# print("hello"+ '!'* 10)
# print("Here is a scarf:")
# print("~#"*10)
# print("#~"*10)
# print("Here is a wave:")
# print('/\ '*10)
# print(' \/'*10)



#!/bin/python3

# from random import randint

# player=input("rock(r),paper(p),scissors(s)?")
# if player =='r':
#   player='o'
# elif player=='p':
#   player='__'
# else:
#   player='<8'
# print(player,'vs',end=' ')
# chossen=randint(1,3)
# print(chossen)
# if chossen==1:
#   computer='r'
#   print('o')
# elif chossen==2:
#   computer='p'
#   print('__')
# else:
#   computer='s'
#   print('<8')
# # print(computer)
# if player==computer:
#   print('draw')
# elif player=='r' and computer=='s':
#   print("player win!")
  
# elif player=='r' and computer=='p':
#   print("computer win!")
  
# elif player=='p' and computer=='s':
#   print("player win!")
  
# elif player=='p' and computer=='r':
#   print("computer  win!")




# l=[[[[[[10]]]]]]







# 16-08-19
# functions 
#  pre defined 
#  user defined
#  based on parameters and return type we have four type of functions 
#  parameters		returntype
#  	0				0
#  	1				0
#  	0				1
#  	1				0
#  functions are object of class functions
#  function has 3 types
#  defin
#  implemention 
#  call

#  defin and implemtations are imp its only one type repted
#  call is an optional and it can be repted

#  definaton:
#  	defination has function name and inputs past to the functions
#  implementaion:
#  	has business logic on the inputs form the defination
# call:
# 	it triggers the function to get the output and pass the input to definaton 
# 	output
# syntax:
# 	def<functionname>():#defination
# 	<logic>#implemation
# <functionname>()#call1
# <functionname>()#call2

# for unimplemented functions used pass is used

# formal parameter
# actual parameter

#  4 kinds of parameter
#  positional/required
#  defalult
#  variable length
#  keywords
#  positional arguments / parameters
#   are the mandatery functions 
#   no of formal parameters should be equal to 
#   






# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://web.whatsapp.com/')

# name = input('Enter the name of user or group : ')
# msg = input('Enter your message : ')
# count = int(input('Enter the count : '))

# input('Enter anything after scanning QR code')

# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()

# msg_box = driver.find_element_by_class_name('_2S1VP')

# for i in range(count):
#     msg_box.send_keys(msg)
#     button = driver.find_element_by_class_name('_35EW6')
#     button.click()









# random module it is an internala imported module it is to be imported to component
# it is used to generate the suddo random numbers
# only used with numbers and collectons cant used with strings
# random function return the a random float value in bw the 0 to 1
# randint(): used to return the a rand integer bw the end points including the read points 
# randrange():randit and range both are same

# random in collections 
# shuffle() it returns the collection of the shuffle elements
# choice() it select the random value form the list
# sample(): it returns


# os paths
# isdir()
# isfile()


# os module 
# it is used for folders and sys paths




# def register():
#     username = input("Please input the first 2 letters of your first name and your birth year ")
#     password = input("Please input your desired password ")
#     file = open("accountfile.txt","w")
#     file.write(username)
#     file.write(" ")
#     file.write(password)
#     file.write("\n")
#     file.close()
#     if login():
#         print("You are now logged in...")
#     else:
#         print("You aren't logged in!")

# def login():
#     username = input("Please enter your username")
#     password = input("Please enter your password")  
#     for line in open("accountfile.txt","r").readlines(): # Read the lines
#         login_info = line.split() # Split on the space, and store the results in a list of two strings
#         print(login_info)
#         if username == login_info[0] and password == login_info[1]:
#             print("Correct credentials!")
#             return True
#     print("Incorrect credentials.")
#     return False
# register()



import random
def write(name):
	fo=open("demo.txt","a")
	fo.write(name)
	# file.write("\n")
	fo.write("---")
	for i in range(2):
		a="01234567890"
		passl = 4
		b = "".join(random.sample(a,passl))
		c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		passla = 4
		d = "".join(random.sample(c,passla))
		fo.write(b)
		fo.write(d)
	fo.write("\n")
def read():
	usr=input("enter a user name:")
	file=open("demo.txt","r")
	f1=file.readlines()
	if f1 is " ":
		write(usr)
	else:
		lis=[]
		for line in f1:			
			l1=line.split("---")
			lis.append(l1)
			# l2=l1[1]
			# l3=l1[0]
			print(lis)
			print(l1)
			if usr in lis[line]:
				print("user already exists")
				return 0
			else:
				write(usr)	
				return 1
read()