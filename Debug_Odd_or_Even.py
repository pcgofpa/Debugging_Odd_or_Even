# Code as initially sent for debugging
#number = int(input("Which number do you want to check?"))
#if number % 2 = 0:                     this line has the error. ['=': equals, '==': comparison]
#  print("This is an even number.")
#else:
#  print("This is an odd number.")

number = int(input("Which number do you want to check? "))

if number % 2 == 0:     # with this line corrected to number % 2 == 0 it is comparing if the remainder of number/2 is equal to 0.
  print("This is an even number.")
else:
  print("This is an odd number.")