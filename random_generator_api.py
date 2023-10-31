import requests
import random
from datetime import datetime, timedelta

def get_random_name():
    """Fetch a random first and last name from the Random User Generator API."""
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    user = data["results"][0]
    
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    
    return first_name, last_name

def random_email(first_name, last_name):
    """Generate a random email address."""
    # List of example domains for the email
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    
    # Construct a random email
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(10,99)}@{random.choice(domains)}"
    return email

def random_dob(min_age=18, max_age=70):
    """Generate a random date of birth within a given age range."""
    current_year = datetime.now().year
    birth_year = random.randint(current_year - max_age, current_year - min_age)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)  # Keeping it 28 to avoid issues with February
    return f"{birth_year}-{birth_month:02}-{birth_day:02}"

def generate_random_values():
    """Generate a set of random user details."""
    first_name, last_name = get_random_name()
    email = random_email(first_name, last_name)
    dob = random_dob()
    return first_name, last_name, email, dob

# Running the function and printing the result
if __name__ == '__main__':
    print(generate_random_values())
