#write a program to print play snake and ladder
import random
c=0
while True:
	a=input("enter 'r' to roll the dice and 'q' to quit")
	if(a=='r'):
		print(random.randint(1,6))
	elif(a=='q'):
		print("BYE!")
		break
	else:
		print("give either 'r' or 'q'")