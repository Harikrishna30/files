import random
import password as f
def write(name):
	file = open("demo.txt","a")
	pas=f.new
	file.write(name)
	file.write("\n")
	file.write(str(pas))
	file.write("\n")
	print(pas)
def read():
	usr=input("enter a name:")
	file=open("demo.txt","r")
	fo1=file.readlines()
	lis=[]
	for line in fo1:
		lis.append(line.rstrip())
	if usr in lis:
		print("user already exits")
		return 0
	else:
		write(usr)
		return 1
read()