import random
from datetime import datetime, timedelta

# Predefined lists of popular first and last names for our mock generator
first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris"]

def random_name(list_of_names):
    return random.choice(list_of_names)

def random_email(first_name, last_name):
    # List of example domains for the email
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    
    # Construct a random email
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(10,99)}@{random.choice(domains)}"
    return email

def random_dob(min_age=18, max_age=70):
    # Generate a random date of birth between the min_age and max_age
    current_year = datetime.now().year
    birth_year = random.randint(current_year - max_age, current_year - min_age)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)  # Keeping it 28 to avoid issues with February
    return f"{birth_year}-{birth_month:02}-{birth_day:02}"

def generate_random_values():
    first_name = random_name(first_names)
    last_name = random_name(last_names)
    email = random_email(first_name, last_name)
    dob = random_dob()
    return first_name, last_name, email, dob

# Running the function and printing the result
if __name__ == '__main__':
    print(generate_random_values())
