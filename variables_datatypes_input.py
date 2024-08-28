#  Prompts user to enter their name and email and stores it in the respective variable.
customer_name = input("Enter customer name: ")
customer_email = input("Enter customer email: ")



item_name = input("Enter item name: ") # Prompts user to enter the item's name and stores it in the variable.
item_price = float(input("Enter price of one item: "))  #  prompts user to enter, converts the input to float, and stores it in variable.
item_quantity = int(input("Enter quantity of items: "))  # prompts user to enter, converts the input to integer, and stores it in variable.

# total_cost is the variable. this variable stores the total cost by multiplying the price by the quantity
total_cost = item_price * item_quantity

# Generate the invoice using f-string so can embedding the variables directly within the string using curly braces {}.
invoice = f"""
Invoice
-------
Customer Name: {customer_name}
Customer Email: {customer_email}

Item: {item_name}
Price per Item: ${item_price:.2f}
Quantity: {item_quantity}

Total Cost: ${total_cost:.2f}
"""

# Print the invoice
print(invoice)