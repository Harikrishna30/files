# python has 3 control state ments 
# pass: it can be used in conditionaln stmts loos functions 
# break: it is exit the loop in a condition when the condition is true
# continue: it is exits the the loop at a condition if the the condition is true and  return backs the loop after the condititon is exititue

# collections:-it is derived data types it stores multible values
# it has five collections:-

# 1.list
# 2.tuples
# 3.sets
# 4.Ranges
# 5.Dictionaries


# lists: it can be index,sliced,concatenated,iterator
# it has heterogeneous
# these are order 1 one n values
# lists are mutible datatypes
# it store multible values



# listsyntax

# <listname>=[<ele>,<ele2>,etc]

# stack vs queue 

# ->stack is LIFO
# ->queue is FIFO



bal=2000
pin = int(input('Please Enter You 4 Digit Pin: '))
if pin == (1234):
	print("1.savings")
	print("2.current")
	print("3.pin change")
	print("4.balance Enq")
	print("5.update ur account")
	val=int(input("enter correct option:"))
	if val==1:
		money=int(input("enter amount to withdraw:"))
		print("collect your cash:%d"%(money))
	elif val==2:
		money=int(input("enter current account money to withdraw:"))
		print("collect your cash:%d"%(money))

	elif val==3:
		oldpin=int(input("enter your old pin:"))
		newpin=int(input("enter your new pin:"))
		conpin=int(input("Re-enter your new pin:"))
		print("your pin is change")
	elif val==4:
		print("your balance is: %d"%(bal))
	elif val==5:
		print("1.update ur pin")
		print("2.update ur contact")
		print("3.update ur profile")

else:
	print("enter valid pin")

