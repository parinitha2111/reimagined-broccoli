#write a program to print random numbers 
import random
while True:
	a=input("enter 'r' to roll the dice and 'q' to quit")
	if(a=='r'):
		print(random.randint(1,6))
	elif(a=='q'):
		print("BYE!")
		break
	else:
		print("give either 'r' or 'q'")