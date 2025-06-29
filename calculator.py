a=int(input("Enter a value of a ="))
b=int(input("Enter a value of b ="))
operation=input("Enter the operation to be performed( + - * / ** ) =")

if operation == "+":
  sum =a+b
  print("The sum of a and b is ",sum)

elif operation =="-":
  subtract =a-b
  print("The subtraction of a and b is ",subtract)

elif operation =="*":
  multiplication=a*b
  print("The multiplication of a and b is",multiplication)

elif operation =="**":
  exponential=a**b
  print("The exponential of a and b is",exponential)

elif operation =="/":
  division=a/b
  print("The division of a and b is",division)

else:
  print("Invalid operation")

