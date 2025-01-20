import sqlite3
import random
import os
from datetime import datetime

# Sample data
first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Sarah', 'Karen', 'Lisa', 'Emma', 'Olivia', 'Ava', 'Isabella']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']
car_makes = ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Nissan', 'Hyundai', 'Kia', 'Mazda', 'Volvo', 'Subaru', 'Peugeot', 'Renault']
car_models = {
    'Toyota': ['Corolla', 'Camry', 'RAV4', 'Yaris'],
    'Honda': ['Civic', 'Accord', 'CR-V', 'Jazz'],
    'Ford': ['Fiesta', 'Focus', 'Mondeo', 'Kuga'],
    'BMW': ['3 Series', '5 Series', 'X3', 'X5'],
    'Mercedes': ['A-Class', 'C-Class', 'E-Class', 'GLC'],
    'Audi': ['A3', 'A4', 'Q3', 'Q5'],
    'Volkswagen': ['Golf', 'Polo', 'Passat', 'Tiguan'],
    'Nissan': ['Qashqai', 'Juke', 'Leaf', 'Micra'],
    'Hyundai': ['i20', 'i30', 'Tucson', 'Kona'],
    'Kia': ['Ceed', 'Sportage', 'Rio', 'Picanto'],
    'Mazda': ['3', '6', 'CX-5', 'MX-5'],
    'Volvo': ['V40', 'V60', 'XC40', 'XC60'],
    'Subaru': ['Impreza', 'Forester', 'Outback', 'XV'],
    'Peugeot': ['208', '308', '3008', '5008'],
    'Renault': ['Clio', 'Megane', 'Captur', 'Kadjar']
}

def generate_registration():
    letters = ''.join(random.choices('ABCDEFGHJKLMNOPRSTUVWXYZ', k=2))
    numbers = str(random.randint(10, 99))
    letters_end = ''.join(random.choices('ABCDEFGHJKLMNOPRSTUVWXYZ', k=3))
    return f"{letters}{numbers} {letters_end}"

def populate_database():
    db_path = os.path.join(os.path.dirname(__file__), 'car_park.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM permits")
    cursor.execute("DELETE FROM vehicles")

    # Generate 250 records
    for _ in range(250):
        # Generate person details
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        # Generate vehicle details
        make = random.choice(car_makes)
        model = random.choice(car_models[make])
        registration = generate_registration()

        # Determine permit type (60% students, 30% staff, 10% visitors)
        permit_type = random.choices([2, 1, 3], weights=[60, 30, 10])[0]

        try:
            # Insert vehicle
            cursor.execute("""
                INSERT INTO vehicles (make, model, registration)
                VALUES (?, ?, ?)
            """, (make, model, registration))
            vehicle_id = cursor.lastrowid

            # Insert permit
            cursor.execute("""
                INSERT INTO permits (name, vehicle_id, permit_type)
                VALUES (?, ?, ?)
            """, (name, vehicle_id, permit_type))

        except sqlite3.IntegrityError:
            # Skip if registration number already exists
            continue

    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_database()
    print("Database populated with test data successfully")
