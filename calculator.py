#this is a simple calculator asks user for input performing basic operations

def calculator():
 num1= float(input("Please enter a number: "))
 print("======================================")
 num2= float(input(" please enter a number: "))
 operator= input(" Pleae choose an operation: +, -، *، / ")
 #verifying operation  
 if operator == "+":
  print(f"the result of the operation is: {num1 + num2}")
 elif operator == "-":
  print(f" the result of the operation is: {num1 - num2}")
 elif operator == "*":
  print(f" the result of the operation is: {num1*num2}")
 elif operator == "/":
  if num2!= 0:
   print(f"the result is: {num1/num2}")
  else:
   print("cannot divide by 0")
 else:
  print("invalid operation")

calculator()
