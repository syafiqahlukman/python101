# Define variables for item prices. Data types of these variables is float (number with decimal point)
price_apple = 0.5  
price_banana = 0.3 
price_orange = 0.7 

# Define variables for item quantities. Data type of these variables is integer (a whole number)
quantity_apple = 4 
quantity_banana = 6  
quantity_orange = 3  

# Calculate the total cost for each item. Data type of these variables is float
total_cost_apple = price_apple * quantity_apple
total_cost_banana = price_banana * quantity_banana
total_cost_orange = price_orange * quantity_orange

# Calculate the overall total cost
total_cost = total_cost_apple + total_cost_banana + total_cost_orange

# Print the results
print("Cost of apples: $ {:.2f}".format(total_cost_apple))
print("Cost of bananas: $ {:.2f}".format(total_cost_banana))
print("Cost of oranges: $ {:.2f}".format(total_cost_orange))
print("Total cost: $ {:.2f}".format(total_cost))