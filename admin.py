import random

print("Menu options:\n 1.Add a guest\n 2.Add a room \n 3.Add a booking\n 4.view bookings\n 5.Quit\n 6.view log file")
res=int(input(" "))
with open("admin.txt","a")as fo:
	if res == 1:
		def first():
			name=input("enter a guest name:")
			print(name)
			
			for i in range(2):
				a="01234567890"
				passl = 4		
				b = "".join(random.sample(a,passl))

			print("%s id %s has been added"%(name,b))
			fo.write(name)
			fo.write(" id")
			fo.write(b)
			fo.write(" has been added")
			fo.write("\n")

			yes=int(input("add new (1) or exit (5):"))
			if yes==1:
				first()
			else:
				print("exit")
		first()

	if res == 2:
		def second():
			room=int(input("enter a room number:"))
			cap=int(input("enter a capacity:"))
			if cap<=2:
				yes=int(input("add new(1) or exit(5)"))
				if yes==1:
					second()
				else:
					print("exit")
			else:
				print("capacity exits")
			fo.write("room number is ")
			fo.write(str(room))
			fo.write("\n")
			fo.write("capacity is ")
			fo.write(str(cap))
		second()
	if res == 3:
		def third():
			room=int(input("enter a room no:"))
			gue=int(input("enter a number of guests:"))
			fo.write("\n")
			fo.write("booking room number is:-")
			fo.write(str(room))
			fo.write("\n")
			fo.write("number of guests:-")
			fo.write(str(gue))
			fo.write("\n")
			if gue==1:
				id1=int(input("enter a id for guest1:"))
				checkin=int(input("enter a checkin date:"))
				checkout=int(input("enter a checkout date:"))
				fo.write("id of guest1:-")
				fo.write(str(id1))
				fo.write("\n")
				fo.write("checkin date:-")
				fo.write(str(checkin))
				fo.write("\n")
				fo.write("checkout date:-")
				fo.write(str(checkout))
				fo.write("\n")


			if gue==2:
				id1=int(input("enter a id for guest1:"))
				id2=int(input("enter a id for guest2:"))
				checkin=int(input("enter a checkin date:"))
				checkout=int(input("enter a checkout date:"))
				fo.write("id of guest1:-")
				fo.write(str(id1))
				fo.write("\n")
				fo.write("id of guest2:-")
				fo.write(str(id2))
				fo.write("\n")
				fo.write("checkin date:-")
				fo.write(str(checkin))
				fo.write("\n")
				fo.write("checkout date:-")
				fo.write(str(checkout))
				fo.write("\n")

				print("booking is done thanks!")
				yes=int(input("add new (1) or exit (5):"))
				if yes==1:
					third()
				else:
					print("exit")

			else:
				# print("capacity exceeded!")
				print("booking is failed!")
				fo.write("booking is failed!")
				fo.write("\n")

		third()


	if res==4:
		print("1.as per room\n2.as for name\n3.as for id")
		check=int(input(""))
		if check==1:
			print("view bookings as for room number")
			rm=int(input(" "))
			print(rm)
			# if rm in room:
			# 	print(gue)
			# print("")
		if check==2:
			print("view bookings as for name ")
			rm=input("")
			print(rm)
		if check==3:
			print("view bookings as for id")
			rm=int(input(""))
			print(rm)


	if res == 5:
		print("exits!\n")


	if res == 6:
		with open("admin.txt","r") as f1:
			read=f1.readlines()
			for i in read:
				print(i)
			print(read)



