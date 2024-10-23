def life_in_weeks(age):
    # Define total years, days, weeks, and months until 90 years
    total_years = 90

    # Calculate time left
    years_left = total_years - age
    days_left = years_left * 365
    weeks_left = years_left * 52
    months_left = years_left * 12

    # Output the result using f-strings
    message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
    print(message)


# Example usage
current_age = int(input("What is your current age? "))
life_in_weeks(current_age)
