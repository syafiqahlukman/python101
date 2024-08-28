# Define a function to add two numbers

def add_numbers(a, b): # a function named add_numbers that takes two parameters, a and b.
    result = a + b #adds the two parameters and stores the result in the variable result
    return result


sum_result = add_numbers(3, 5)
#This line calls the add_numbers function with the arguments 3 and 5.
#The function executes and returns the sum, which is 8.
#The returned value is stored in the variable sum_result.

# Print the result
print("The sum of 3 and 5 is:", sum_result)