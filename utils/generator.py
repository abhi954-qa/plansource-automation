import random
from datetime import datetime, timedelta

def generate_random_ssn():
    return str(random.randint(100000000, 999999999))

def get_hire_date():
    return (datetime.today() - timedelta(days=2)).strftime('%m/%d/%Y')  # Format as MM/DD/YYYY
