from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker("en_GB")

# Constants
ROLES = ["Staff", "Student", "Visitor"]
ROLE_WEIGHTS = [0.3, 0.5, 0.2]  # 30% Staff, 50% Students, 20% Visitors
CAR_MAKES = ["Toyota", "Ford", "Volkswagen", "Honda", "BMW", "Audi", "Mercedes", 
             "Nissan", "Hyundai", "Skoda", "Peugeot", "Renault", "Kia", "Volvo"]
MODELS = {
    "Toyota": ["Corolla", "Yaris", "RAV4", "Prius"],
    "Ford": ["Focus", "Fiesta", "Puma", "Kuga"],
    "Volkswagen": ["Golf", "Polo", "Tiguan", "Passat"],
    "Honda": ["Civic", "Jazz", "CR-V", "HR-V"],
    "BMW": ["320i", "118i", "X3", "X1"],
    "Audi": ["A3", "A4", "Q3", "Q5"],
    "Mercedes": ["A-Class", "C-Class", "GLA", "B-Class"],
    "Nissan": ["Qashqai", "Juke", "Leaf", "Micra"],
    "Hyundai": ["i30", "Tucson", "Kona", "i20"],
    "Skoda": ["Octavia", "Fabia", "Kamiq", "Karoq"],
    "Peugeot": ["208", "2008", "308", "3008"],
    "Renault": ["Clio", "Captur", "Megane", "Kadjar"],
    "Kia": ["Ceed", "Sportage", "Rio", "Stonic"],
    "Volvo": ["XC40", "XC60", "V40", "V60"]
}

def generate_uk_plate():
    """Generate a realistic UK number plate"""
    letters1 = "".join(random.choices("ABCDEFGHJKLMNOPRSTUVWXY", k=2))
    numbers = str(random.randint(0, 99)).zfill(2)
    letters2 = "".join(random.choices("ABCDEFGHJKLMNOPRSTUVWXYZ", k=3))
    return f"{letters1}{numbers} {letters2}"

def generate_email(first_name, last_name, role, used_emails):
    """Generate unique university email based on role"""
    domain = "university.ac.uk"
    if role == "Student":
        domain = f"student.{domain}"
    elif role == "Visitor":
        domain = f"visitor.{domain}"
    
    base_email = f"{first_name[0].lower()}.{last_name.lower()}@{domain}"
    email = base_email
    counter = 1
    
    while email in used_emails:
        email = f"{first_name[0].lower()}.{last_name.lower()}{counter}@{domain}"
        counter += 1
    
    used_emails.add(email)
    return email

# Generate SQL file
num_people = 250
permit_percentage = 0.7  # 70% of people will have permits
used_emails = set()

with open("sample_data.sql", "w") as f:
    # Generate People
    f.write("-- People Data\n")
    people_data = []
    for i in range(1, num_people + 1):
        role = random.choices(ROLES, weights=ROLE_WEIGHTS)[0]
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = generate_email(first_name, last_name, role, used_emails)
        phone = fake.phone_number()
        
        f.write(f"""INSERT INTO People (PersonID, FirstName, LastName, PhoneNumber, Email, Role) 
                VALUES ({i}, "{first_name}", "{last_name}", "{phone}", "{email}", "{role}");
""")
        people_data.append((i, role))

    # Generate Car Info
    f.write("\n-- Car Information\n")
    car_data = []
    for person_id, _ in people_data:
        make = random.choice(CAR_MAKES)
        model = random.choice(MODELS[make])
        reg = generate_uk_plate()
        f.write(f"""INSERT INTO CarInfo (RegNumber, PersonID, Make, Model) 
                VALUES ("{reg}", {person_id}, "{make}", "{model}");
""")
        car_data.append((person_id, reg))

    # Generate Permits
    f.write("\n-- Permits\n")
    permit_people = random.sample(car_data, int(num_people * permit_percentage))
    
    for person_id, reg in permit_people:
        date_issued = fake.date_between(start_date="-1y", end_date="today")
        date_expiry = date_issued + timedelta(days=365)
        f.write(f"""INSERT INTO Permits (PersonID, RegNumber, DateIssued, DateExpiry) 
                VALUES ({person_id}, "{reg}", "{date_issued}", "{date_expiry}");
""")

print(f"Generated {num_people} records in sample_data.sql")
