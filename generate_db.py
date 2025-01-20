import sqlite3
import random
from datetime import datetime, timedelta

# Sample data for random generation
first_names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "James", "Lisa", "Robert", "Linda", "Michael", "Karen", "William", "Jessica", "Richard", "Patricia", "Charles", "Jennifer", "Joseph", "Barbara"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
car_makes = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi", "Volkswagen", "Nissan", "Chevrolet", "Kia", "Hyundai", "Subaru", "Mazda", "Lexus", "Jeep", "Dodge", "Ram", "Chrysler", "Buick", "Cadillac"]
car_models = ["Civic", "Corolla", "Focus", "3 Series", "A4", "Golf", "Altima", "Camry", "Accord", "Mustang", "Escape", "Explorer", "CR-V", "RAV4", "Impala", "Malibu", "Equinox", "Tahoe", "Wrangler", "Cherokee"]
user_types = ["student", "staff", "visitor", "faculty", "contractor", "guest", "alumni", "administrator"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
car_makes = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi", "Volkswagen", "Nissan"]
car_models = ["Civic", "Corolla", "Focus", "3 Series", "A4", "Golf", "Altima", "Camry"]
user_types = ["student", "staff", "visitor"]

def generate_reg():
    """Generate a random UK-style registration number"""
    letters = ''.join(random.choices('ABCDEFGHJKLMNOPRSTUVWXYZ', k=2))
    numbers = str(random.randint(10, 99))
    end_letters = ''.join(random.choices('ABCDEFGHJKLMNOPRSTUVWXYZ', k=3))
    return f"{letters}{numbers} {end_letters}"

# Create database connection
conn = sqlite3.connect('car-park.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE permits (
    permit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    valid_from DATE,
    valid_until DATE
)
''')

cursor.execute('''
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration TEXT NOT NULL UNIQUE,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    user_type TEXT NOT NULL,
    permit_id INTEGER,
    FOREIGN KEY (permit_id) REFERENCES permits (permit_id)
)
''')

# Generate and insert sample data
for i in range(200):
    # Create permit
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    valid_from = datetime.now() - timedelta(days=random.randint(0, 30))
    valid_until = valid_from + timedelta(days=random.randint(30, 365))
    
    cursor.execute('''
    INSERT INTO permits (name, valid_from, valid_until)
    VALUES (?, ?, ?)
    ''', (name, valid_from.date(), valid_until.date()))
    
    permit_id = cursor.lastrowid
    
    # Create vehicle
    make = random.choice(car_makes)
    model = random.choice(car_models)
    registration = generate_reg()
    user_type = random.choice(user_types)
    
    cursor.execute('''
    INSERT INTO vehicles (registration, make, model, user_type, permit_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (registration, make, model, user_type, permit_id))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully with sample data!")
