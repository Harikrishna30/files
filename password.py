# 16 digits password
import random 
l1 = [i for i in range(5)]
l2 = [chr(i) for i in range(97,107)] 
a=random.sample(l1,4)
b=random.sample(l2,4)
c=random.sample(l1,4)
d=random.sample(l2,4)
e= a+b+c+d
new =""
for i in e:
	new=new+str(i)
# print(new)

# same to to same  8 digits password 

# import random
# for i in range(2):
# 	a="01234567890"
# 	passl = 4
# 	b = "".join(random.sample(a,passl))
# 	c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 	passla = 4
# 	d = "".join(random.sample(c,passla))
# 	e=b+d
# 	new=""
# 	for i in e:
# 		new=new+str(i)
# print(new)