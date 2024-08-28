# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even
is_even = (number % 2 == 0)

# Print whether the number is even or odd
if is_even:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")