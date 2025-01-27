import random
from datetime import datetime, timedelta
from dbmanager import DBManager

# UK-specific data
UK_FIRST_NAMES = [
    # Male names
    "James",
    "Oliver",
    "Harry",
    "Jack",
    "George",
    "William",
    "Henry",
    "Thomas",
    "Charlie",
    "Oscar",
    "Leo",
    "Edward",
    "Alexander",
    "Noah",
    "Ethan",
    "Daniel",
    "Mohammed",
    "David",
    "Michael",
    "Joseph",
    "Robert",
    "John",
    "Christopher",
    # Female names
    "Emma",
    "Olivia",
    "Sophie",
    "Emily",
    "Lucy",
    "Alice",
    "Charlotte",
    "Grace",
    "Sophia",
    "Isabella",
    "Ava",
    "Lily",
    "Mia",
    "Ella",
    "Amelia",
    "Jessica",
    "Sarah",
    "Elizabeth",
    "Victoria",
    "Eleanor",
    "Florence",
    "Evie",
    "Isabelle",
]

UK_LAST_NAMES = [
    "Smith",
    "Jones",
    "Williams",
    "Brown",
    "Taylor",
    "Davies",
    "Evans",
    "Wilson",
    "Thomas",
    "Roberts",
    "Johnson",
    "Lewis",
    "Walker",
    "Robinson",
    "Wood",
    "Thompson",
    "White",
    "Watson",
    "Jackson",
    "Wright",
    "Green",
    "Harris",
    "Cooper",
    "King",
    "Lee",
    "Martin",
    "Clarke",
    "James",
    "Morgan",
    "Hughes",
    "Edwards",
    "Hill",
    "Moore",
    "Clark",
    "Harrison",
    "Scott",
    "Young",
    "Morris",
    "Hall",
    "Ward",
    "Turner",
    "Carter",
    "Phillips",
    "Mitchell",
    "Patel",
    "Adams",
    "Campbell",
]

UK_CAR_MAKES = [
    # Common UK manufacturers and popular imports
    "Ford",
    "Vauxhall",
    "Volkswagen",
    "BMW",
    "Audi",
    "Mercedes",
    "Toyota",
    "Nissan",
    "Honda",
    "Peugeot",
    "Renault",
    "Land Rover",
    "Mini",
    "Kia",
    "Hyundai",
    "Volvo",
    "Mazda",
    "Skoda",
    "Seat",
    "Fiat",
    "Jaguar",
    "Citroen",
]

# Expanded models for each make
CAR_MODELS = {
    "Ford": [
        "Fiesta",
        "Focus",
        "Kuga",
        "Puma",
        "Mondeo",
        "EcoSport",
        "Mustang",
        "Galaxy",
        "S-Max",
    ],
    "Vauxhall": [
        "Corsa",
        "Astra",
        "Insignia",
        "Mokka",
        "Crossland",
        "Grandland",
        "Combo Life",
        "Vivaro",
    ],
    "Volkswagen": [
        "Golf",
        "Polo",
        "Tiguan",
        "Passat",
        "T-Roc",
        "T-Cross",
        "ID.3",
        "ID.4",
        "Arteon",
    ],
    "BMW": [
        "1 Series",
        "2 Series",
        "3 Series",
        "4 Series",
        "5 Series",
        "X1",
        "X2",
        "X3",
        "X5",
        "i3",
        "i4",
    ],
    "Audi": ["A1", "A3", "A4", "A5", "A6", "Q2", "Q3", "Q5", "e-tron", "TT"],
    "Mercedes": [
        "A-Class",
        "B-Class",
        "C-Class",
        "E-Class",
        "GLA",
        "GLB",
        "GLC",
        "CLA",
        "EQA",
        "EQC",
    ],
    "Toyota": [
        "Yaris",
        "Corolla",
        "RAV4",
        "Aygo",
        "C-HR",
        "Prius",
        "Camry",
        "Land Cruiser",
    ],
    "Nissan": ["Qashqai", "Juke", "Micra", "Leaf", "X-Trail", "Ariya", "Note"],
    "Honda": ["Civic", "CR-V", "Jazz", "HR-V", "e", "NSX"],
    "Peugeot": ["208", "2008", "308", "3008", "5008", "e-208", "e-2008"],
    "Renault": ["Clio", "Captur", "Megane", "Kadjar", "Zoe", "Arkana"],
    "Land Rover": [
        "Discovery",
        "Discovery Sport",
        "Range Rover",
        "Range Rover Sport",
        "Evoque",
        "Defender",
        "Velar",
    ],
    "Mini": ["Cooper", "Countryman", "Clubman", "Electric", "Convertible", "5-Door"],
    "Kia": ["Picanto", "Rio", "Ceed", "Sportage", "Niro", "e-Niro", "Soul", "Stinger"],
    "Hyundai": ["i10", "i20", "i30", "Tucson", "Kona", "IONIQ", "Santa Fe"],
    "Volvo": ["XC40", "XC60", "XC90", "V60", "V90", "S60", "S90"],
    "Mazda": ["2", "3", "6", "CX-30", "CX-5", "MX-5"],
    "Skoda": ["Fabia", "Octavia", "Superb", "Kamiq", "Karoq", "Kodiaq", "Enyaq"],
    "Seat": ["Ibiza", "Leon", "Arona", "Ateca", "Tarraco", "Mii"],
    "Fiat": ["500", "Panda", "Tipo", "500X", "500L"],
    "Jaguar": ["XE", "XF", "F-PACE", "E-PACE", "I-PACE", "F-TYPE"],
    "Citroen": ["C1", "C3", "C4", "C5", "Berlingo", "e-C4"],
}


def generate_uk_reg():
    """Generate a random UK registration number in the format AB12 CDE"""
    # Current format since 2001: two letters, two numbers, three letters
    # First letters: Area code (not using I, Q or Z)
    area_codes = [
        "BA",
        "BL",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "BV",
        "BW",
        "BY",
        "CA",
        "CB",
        "CC",
        "CD",
        "CE",
        "CF",
        "CG",
        "CH",
        "CK",
        "CL",
    ]
    year_codes = [f"{str(y).zfill(2)}" for y in range(1, 99)]  # 01-99
    # Last letters: Random (not using I or Q)
    allowed_letters = "ABCDEFGHJKLMNOPRSTUVWXYZ"

    first_letters = random.choice(area_codes)
    numbers = random.choice(year_codes)
    last_letters = "".join(random.choices(allowed_letters, k=3))

    return f"{first_letters}{numbers} {last_letters}"


def get_permit_dates(role):
    """Generate realistic issue and expiry dates based on role"""
    today = datetime.now()

    # Different date ranges based on role
    if role == "STAFF":
        # Staff permits: 1-3 year duration, can start up to 3 years ago
        days_ago = random.randint(0, 1095)  # Up to 3 years ago
        duration = random.randint(365, 1095)  # 1-3 years
    elif role == "STUDENT":
        # Student permits: 1 year duration, typically align with academic year
        academic_year_start = datetime(today.year, 9, 1)  # September 1st
        if today.month >= 9:
            academic_year_start = academic_year_start
        else:
            academic_year_start = academic_year_start.replace(year=today.year - 1)
        days_ago = (today - academic_year_start).days
        duration = 365  # 1 year
    else:  # VISITOR
        # Visitor permits: 1-30 days, recent or future dates
        days_ago = random.randint(-30, 30)  # Can be future dates
        duration = random.randint(1, 30)  # 1-30 days

    issue_date = today - timedelta(days=days_ago)
    expiry_date = issue_date + timedelta(days=duration)

    return issue_date.strftime("%Y-%m-%d"), expiry_date.strftime("%Y-%m-%d")


def generate_record():
    """Generate a single random record with role-appropriate permits"""
    fname = random.choice(UK_FIRST_NAMES)
    lname = random.choice(UK_LAST_NAMES)
    role = random.choice(["STUDENT", "STAFF", "VISITOR"])
    make = random.choice(UK_CAR_MAKES)
    model = random.choice(CAR_MODELS[make])
    reg = generate_uk_reg()
    date_issued, date_expiry = get_permit_dates(role)

    return fname, lname, role, make, model, reg, date_issued, date_expiry


def main():
    db = DBManager()
    db.create_table()

    print("Random UK Car Park Data Generator")
    print("-" * 30)
    print("This will generate records with the following permit rules:")
    print("- Staff: 1-3 year permits")
    print("- Students: 1 year permits aligned with academic year")
    print("- Visitors: 1-30 day permits")
    print("-" * 30)

    while True:
        try:
            count = int(input("How many records would you like to generate? "))
            if count < 1:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number")

    # Add role distribution option
    print("\nWould you like to specify the distribution of roles?")
    print("1. Equal distribution")
    print("2. Realistic distribution (60% students, 30% staff, 10% visitors)")
    print("3. Custom distribution")

    choice = input("Enter choice (1-3): ")

    if choice == "3":
        print("\nEnter percentages (should sum to 100):")
        student_pct = int(input("Student %: "))
        staff_pct = int(input("Staff %: "))
        visitor_pct = int(input("Visitor %: "))
        if student_pct + staff_pct + visitor_pct != 100:
            print("Percentages don't sum to 100, using equal distribution")
            choice = "1"
    elif choice == "2":
        student_pct, staff_pct, visitor_pct = 60, 30, 10
    else:
        student_pct = staff_pct = visitor_pct = 33

    print(f"\nGenerating {count} records...")

    # Calculate counts for each role
    student_count = int(count * student_pct / 100)
    staff_count = int(count * staff_pct / 100)
    visitor_count = count - student_count - staff_count

    # Generate records for each role
    for role, role_count in [
        ("STUDENT", student_count),
        ("STAFF", staff_count),
        ("VISITOR", visitor_count),
    ]:
        for i in range(role_count):
            try:
                fname = random.choice(UK_FIRST_NAMES)
                lname = random.choice(UK_LAST_NAMES)
                make = random.choice(UK_CAR_MAKES)
                model = random.choice(CAR_MODELS[make])
                reg = generate_uk_reg()
                date_issued, date_expiry = get_permit_dates(role)

                record = (
                    fname,
                    lname,
                    role,
                    make,
                    model,
                    reg,
                    date_issued,
                    date_expiry,
                )
                db.insertintotable(*record)
                print(f"Generated {role:7} record: {fname} {lname} - {reg}")
            except Exception as e:
                print(f"Error generating record: {str(e)}")

    print("\nData generation complete!")


if __name__ == "__main__":
    main()
