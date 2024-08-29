'''num1 = input("Enter a number: ")
num2 = input("Enter another number:")
result = num1 + num2
print(result)'''

#by default any input from user, python will treat it as string so thats why if we perform the operation above, we dont get the correct answer.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number:"))
result = num1 + num2
print(result)
