num1,num2,num3 =int(input("enter the number"))
if (num1 >= num2)&&(num1 >= num3):
   largest = num1
elif (num2 >= num1)&&(num2 >= num3):
   largest = num2
else:
   largest = num3
print(largest)
