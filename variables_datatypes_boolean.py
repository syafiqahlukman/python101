# Get employee details from user input
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

# Get performance rating and years of service from user input
performance_rating = float(input("Enter performance rating (0.0 - 5.0): "))  # Convert input to float
years_of_service = int(input("Enter years of service: "))  # Convert input to integer

# Define bonus criteria
minimum_rating_for_bonus = 4.0  # Minimum performance rating to be eligible for bonus
minimum_years_for_bonus = 5  # Minimum years of service to be eligible for bonus
bonus_amount = 1000  # Fixed bonus amount in dollars

# Determine bonus eligibility
is_eligible_for_bonus = performance_rating >= minimum_rating_for_bonus and years_of_service >= minimum_years_for_bonus

# Calculate bonus
if is_eligible_for_bonus:
    bonus = bonus_amount
else:
    bonus = 0

# Generate the bonus report
bonus_report = f"""
Bonus Report
------------
Employee Name: {employee_name}
Employee ID: {employee_id}

Performance Rating: {performance_rating}
Years of Service: {years_of_service}

Eligible for Bonus: {is_eligible_for_bonus}
Bonus Amount: RM{bonus:.2f}
"""

# Print the bonus report
print(bonus_report)