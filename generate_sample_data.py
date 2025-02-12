from faker import Faker
import random
import sqlite3


fake = Faker("en_GB")

# Constants
ROLES = ["Staff", "Student", "Visitor"]
CAR_MAKES = [
    "Toyota",
    "Ford",
    "Volkswagen",
    "Honda",
    "BMW",
    "Audi",
    "Mercedes",
    "Nissan",
    "Hyundai",
    "Skoda",
    "Peugeot",
    "Renault",
    "Kia",
    "Volvo",
    "Mazda",
    "Porsche",
    "Land Rover",
    "Jaguar",
    "Mini",
    "Fiat",
    "Seat",
    "Citroen",
    "Vauxhall",
    "Dacia",
    "Tesla",
    "Lexus",
    "Jeep",
    "Suzuki",
    "Mitsubishi",
    "Alfa Romeo",
]

MODELS = {
    "Toyota": [
        "Corolla",
        "Yaris",
        "RAV4",
        "Prius",
        "C-HR",
        "Camry",
        "Aygo",
        "Land Cruiser",
    ],
    "Ford": [
        "Focus",
        "Fiesta",
        "Puma",
        "Kuga",
        "Mustang",
        "Ranger",
        "EcoSport",
        "Galaxy",
        "S-Max",
    ],
    "Volkswagen": [
        "Golf",
        "Polo",
        "Tiguan",
        "Passat",
        "T-Roc",
        "ID.3",
        "ID.4",
        "Arteon",
        "Up!",
    ],
    "Honda": ["Civic", "Jazz", "CR-V", "HR-V", "e", "NSX", "Insight", "E10"],
    "BMW": ["320i", "118i", "X3", "X1", "M3", "M4", "i4", "iX", "X5", "Z4", "420d"],
    "Audi": ["A3", "A4", "Q3", "Q5", "e-tron", "RS6", "TT", "R8", "Q8", "A1", "S3"],
    "Mercedes": [
        "A-Class",
        "C-Class",
        "GLA",
        "B-Class",
        "EQC",
        "AMG GT",
        "S-Class",
        "G-Class",
    ],
    "Nissan": ["Qashqai", "Juke", "Leaf", "Micra", "X-Trail", "GT-R", "370Z", "Ariya"],
    "Hyundai": ["i30", "Tucson", "Kona", "i20", "IONIQ", "Santa Fe", "i10", "Bayon"],
    "Skoda": [
        "Octavia",
        "Fabia",
        "Kamiq",
        "Karoq",
        "Superb",
        "Enyaq",
        "Scala",
        "Kodiaq",
    ],
    "Peugeot": ["208", "2008", "308", "3008", "5008", "e-208", "508", "Rifter"],
    "Renault": [
        "Clio",
        "Captur",
        "Megane",
        "Kadjar",
        "Zoe",
        "Arkana",
        "Scenic",
        "Twizy",
    ],
    "Kia": [
        "Ceed",
        "Sportage",
        "Rio",
        "Stonic",
        "e-Niro",
        "Soul",
        "Picanto",
        "Sorento",
    ],
    "Volvo": ["XC40", "XC60", "V40", "V60", "XC90", "S90", "C40", "S60"],
    "Mazda": ["3", "CX-30", "MX-5", "6", "CX-5", "2", "CX-3", "MX-30"],
    "Porsche": [
        "911",
        "Cayenne",
        "Macan",
        "Taycan",
        "Panamera",
        "718 Cayman",
        "718 Boxster",
    ],
    "Land Rover": [
        "Defender",
        "Discovery",
        "Range Rover",
        "Evoque",
        "Velar",
        "Discovery Sport",
    ],
    "Jaguar": ["F-Pace", "E-Pace", "I-Pace", "XE", "XF", "F-Type"],
    "Mini": [
        "Cooper",
        "Countryman",
        "Clubman",
        "Electric",
        "Convertible",
        "John Cooper Works",
    ],
    "Fiat": ["500", "Panda", "Tipo", "500X", "500L", "Spider"],
    "Seat": ["Leon", "Ibiza", "Arona", "Ateca", "Tarraco", "Mii"],
    "Citroen": ["C3", "C4", "C5", "Berlingo", "C3 Aircross", "C5 Aircross"],
    "Vauxhall": ["Corsa", "Astra", "Mokka", "Crossland", "Grandland", "Insignia"],
    "Dacia": ["Sandero", "Duster", "Logan", "Spring", "Jogger"],
    "Tesla": ["Model 3", "Model Y", "Model S", "Model X"],
    "Lexus": ["UX", "NX", "RX", "IS", "ES", "LC", "LS"],
    "Jeep": ["Renegade", "Compass", "Wrangler", "Cherokee", "Grand Cherokee"],
    "Suzuki": ["Swift", "Vitara", "Ignis", "S-Cross", "Jimny", "Swace"],
    "Mitsubishi": ["Outlander", "ASX", "Eclipse Cross", "L200", "Mirage"],
    "Alfa Romeo": ["Giulia", "Stelvio", "Tonale", "Giulietta"],
}


def generate_uk_plate():
    """Generate a realistic UK number plate"""
    letters1 = "".join(random.choices("ABCDEFGHJKLMNOPRSTUVWXY", k=2))
    numbers = str(random.randint(0, 99)).zfill(2)
    letters2 = "".join(random.choices("ABCDEFGHJKLMNOPRSTUVWXYZ", k=3))
    return f"{letters1}{numbers} {letters2}"


def get_user_input():
    while True:
        try:
            num_records = int(input("How many records would you like to generate? "))
            if num_records <= 0:
                print("Please enter a positive number")
                continue

            print(
                "\nEnter weights for each role (numbers between 0 and 1 that sum to 1):"
            )
            staff_weight = float(input("Staff weight (e.g., 0.3 for 30%): "))
            student_weight = float(input("Student weight (e.g., 0.5 for 50%): "))
            visitor_weight = float(input("Visitor weight (e.g., 0.2 for 20%): "))

            if not 0.99 <= staff_weight + student_weight + visitor_weight <= 1.01:
                print("Weights must sum to 1.0")
                continue

            return num_records, [staff_weight, student_weight, visitor_weight]
        except ValueError:
            print("Please enter valid numbers")


def main():
    # Get user input
    num_people, weights = get_user_input()

    # Create/connect to SQLite database
    conn = sqlite3.connect("carpark.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Carpark (
        registration TEXT NOT NULL UNIQUE,
        fname TEXT,
        lname TEXT,
        make TEXT,
        model TEXT,
        role TEXT,
        PRIMARY KEY (registration)
    )
    """)

    # Generate and insert data
    for _ in range(num_people):
        role = random.choices(ROLES, weights=weights)[0]
        first_name = fake.first_name()
        last_name = fake.last_name()
        make = random.choice(CAR_MAKES)
        model = random.choice(MODELS[make])
        reg = generate_uk_plate()

        try:
            cursor.execute(
                """
            INSERT INTO Carpark (registration, fname, lname, make, model, role)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
                (reg, first_name, last_name, make, model, role),
            )
        except sqlite3.IntegrityError:
            # In case of duplicate registration, try again
            continue

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Successfully generated {num_people} records in carpark.db")


if __name__ == "__main__":
    main()
