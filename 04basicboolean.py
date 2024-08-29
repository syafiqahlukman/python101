'''
A boolean is a type of value that can only be True or False. Think of it like a light switch that can either be ON (True) or OFF (False).

A boolean expression is a statement that evaluates to either True or False. For example:

5 > 3 is a boolean expression that evaluates to True because 5 is greater than 3.
2 == 2 is a boolean expression that evaluates to True because 2 is equal to 2.
4 < 1 is a boolean expression that evaluates to False because 4 is not less than 1.
'''

# Get a number from the user
number = int(input("Enter a number: "))
#input() function in Python always returns the user input as a string, so thats why we need to convert to integer

# Check if the number is even
is_even = (number % 2 == 0)
#We use the modulus operator(%) to find the remainder when number is divided by 2.
#If the remainder is 0 (number % 2 == 0), then the number is even.
#This expression evaluates to True if the number is even and False if it is odd.
#We store the result in the variable is_even.



# Print whether the number is even or odd
if is_even:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# We use an if statement to check the value of is_even.
#If is_even is True, we print that the number is even.
#If is_even is False, we print that the number is odd.