# variables and datatypes
# first method
# L=["digital","lync","hyd","gachibowli"]
# a="lync"
# if a in L:
# 	print("present")
# else:
# 	print("not present")
# # second method
# print(a in L)
# bit wise ope
# a=45
# b=65
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~b)
# print(a>>b)
# print(b<<a)
# q3
# Z=65.33
# import math
# print(int(Z))
# print(complex(Z))
# print(math.sqrt(Z))
# q5
# a=15
# b=2
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# condition stmt
# n=int(input("enter total marks:"))
# if n>=90:
# 	print("%d A grade very good"%(n))
# elif n>=60:
# 	print("%d B grade good"%(n))
# elif n>=40:
# 	print("%d C grade poor"%(n))
# else:
# 	print("%d fail"%(n))


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


# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# c=int(input("enter c number:"))
# if a>b&a>c:
# 	print("%d a is big"%(a))
# elif b>c:
# 	print("%d b is big"%(b))
# else:
# 	print("%d c is big"%(c))

# strings tasks

# stmt="pythonbestforbeginners"
# print(stmt[1:23:2])

# print(stmt[::-1])
# st=split("")


def cal_bill_am(food_type,quality_ord,dis_in_kms):
	bill_amount=0
	if food_type=="V" and quality_ord >= 1 and dis_in_kms >= 0:
		if dis_in_kms >= 0 and dis_in_kms <= 3:
			bill_amount = 120 * quality_ord
		elif dis_in_kms > 3 and dis_in_kms <= 6:
			bill_amount = (120 * quality_ord) + 3
		if dis_in_kms>=6:
			print("N/A")

		else:
			bill_amount=(120 * quality_ord) + 6

	elif food_type=="N" and quality_ord >= 1 and dis_in_kms >= 0:
		if dis_in_kms >= 0 and dis_in_kms <= 3:
			bill_amount = 150 * quality_ord

		elif dis_in_kms > 3 and dis_in_kms <= 6:
			bill_amount = (150 * quality_ord) + 3
		if dis_in_kms>=6:
			print("N/A")
		else:
			bill_amount=(150 * quality_ord) + 6
	else:
		bill_amount= -1
	return bill_amount

bill=cal_bill_am("V",1,7)
print(bill)
