'''Welcome to my project 
	this is a simple calculator that has two modes
	Mode 1 --------> Scientific Calculator
	Mode 2 --------> Progmaming Calculator
	The scientific calculator do a simple mathematical operations like addtion, subtraction, division and multiplication functions
	The programing calculator converts from a decimal into hex or binary number
'''

print("--------------------------------------")
print("Welcome to My Calculator")
print("--------------------------------------")
print("Press 1 to Use Scientific Calculator")
print("Press 2 to Use Progmaming Calculator")
print("Press e to exit")
choice= str (input())
while choice != "e":

	if choice == "1": 
		print("--------------------------------------")
		print("Please enter number 1")
		Number1= int (input())
		print("Please enter number 2")
		Number2= int (input())
		print("Please select the operation")
		operation= str (input())
		
		if operation == "+":
			print("--------------------------------------")
			print(Number1,"+",Number2,"=",Number1+Number2)
			print("--------------------------------------")	
			print("Successful Operation")
			
		elif operation == "-":
			print("--------------------------------------")
			print(Number1,"-",Number2,"=",Number1-Number2)
			print("--------------------------------------")	
			print("Successful Operation")
			
		elif operation == "*":
			print("--------------------------------------")
			print(Number1,"*",Number2,"=",Number1*Number2)
			print("--------------------------------------")	
			print("Successful Operation")
			
		elif operation == "/":
			while Number2 == 0:
				print("Division over zero is not allowable please enter number 2 again")
				Number2= int (input())
			print("--------------------------------------")
			print(Number1,"/",Number2,"=",float(Number1/Number2))
			print("--------------------------------------")	
			print("Successful Operation")
			
	
	
	elif choice == "2":
		print("--------------------------------------")
		print("Please enter a number")
		Number1=int (input())
		print("Choose H for HEX represintation")
		print("Choose B for binary represintation")
		Sc_choice = str (input())
		if Sc_choice == "H" or Sc_choice == "h":
			print("The HEX represintation of",Number1,"is", hex(Number1))
			print("--------------------------------------")	
			print("Successful Operation")

		elif Sc_choice == "B" or Sc_choice == "b":
			print("The Binary represintation of",Number1,"is", bin(Number1))
			print("--------------------------------------")	
			print("Successful Operation")
		
		else:
			print("wrong operation")
	
	
	else:
		print("wrong choice")
		
	
	
	print("--------------------------------------")		
	print("Press 1 to Use Standard Calculator")
	print("Press 2 to Use Scientific Calculator")
	print("Press e to exit")
	choice= str (input())
print("Thanks For Using My Calculator")