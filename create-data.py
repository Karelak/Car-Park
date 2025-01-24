# CREATE TABLE "CarInfo" (
# 	"RegNumber"	TEXT,
# 	"PersonID"	INTEGER,
# 	"Make"	TEXT,
# 	"Model"	TEXT,
# 	PRIMARY KEY("PersonID"),
# 	FOREIGN KEY("PersonID") REFERENCES "People"("PersonID") ON DELETE CASCADE
# );
# CREATE TABLE "People" (
# 	"PersonID"	INTEGER,
# 	"FirstName"	TEXT NOT NULL,
# 	"LastName"	TEXT NOT NULL,
# 	"PhoneNumber"	TEXT,
# 	"Email"	TEXT UNIQUE,
# 	"Role"	TEXT NOT NULL CHECK("Role" IN ('STAFF', 'STUDENT', 'VISITOR')),
# 	PRIMARY KEY("PersonID")
# );
# CREATE TABLE Permits (
#     PersonID INTEGER PRIMARY KEY,  -- PersonID is the unique identifier for the permit here
#     RegNumber TEXT,
#     DateIssued DATE NOT NULL,
#     DateExpiry DATE NOT NULL,
#     FOREIGN KEY (PersonID) REFERENCES People(PersonID) ON DELETE CASCADE,
#     FOREIGN KEY (RegNumber) REFERENCES CarInfo(RegNumber) ON DELETE CASCADE
# )

import sqlite3
import faker
import random

class DataGenerator:
    def __init__(self):
        self.faker = faker.Faker('en_GB')  # Set British English locale
        self.conn = sqlite3.connect('carpark.db')
        self.cursor = self.conn.cursor()
        self._create_tables()  # Add this line
        
    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS People (
                PersonID INTEGER PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                PhoneNumber TEXT,
                Email TEXT UNIQUE,
                Role TEXT NOT NULL CHECK(Role IN ('STAFF', 'STUDENT', 'VISITOR'))
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CarInfo (
                RegNumber TEXT,
                PersonID INTEGER,
                Make TEXT,
                Model TEXT,
                PRIMARY KEY(PersonID),
                FOREIGN KEY(PersonID) REFERENCES People(PersonID) ON DELETE CASCADE
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Permits (
                PersonID INTEGER PRIMARY KEY,
                RegNumber TEXT,
                DateIssued DATE NOT NULL,
                DateExpiry DATE NOT NULL,
                FOREIGN KEY (PersonID) REFERENCES People(PersonID) ON DELETE CASCADE,
                FOREIGN KEY (RegNumber) REFERENCES CarInfo(RegNumber) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()
        
    def generate_data(self, num_records):
        # Generate People first
        people_ids = self._generate_people(num_records)
        # Generate CarInfo with reference to people
        self._generate_car_info(people_ids)
        # Generate Permits
        self._generate_permits(people_ids)
        self.conn.commit()
        
    def _generate_people(self, num_records):
        people_ids = []
        roles = ['STAFF', 'STUDENT', 'VISITOR']
        email_domains = {
            'STAFF': 'staff.university.ac.uk',
            'STUDENT': 'student.university.ac.uk',
            'VISITOR': 'gmail.com,yahoo.co.uk,outlook.com,btinternet.com'.split(',')
        }
        used_emails = set()
        
        for _ in range(num_records):
            first_name = self.faker.first_name().upper()
            last_name = self.faker.last_name().upper()
            role = random.choice(roles)
            
            # Generate base email
            if role in ['STAFF', 'STUDENT']:
                base_email = f"{first_name[0]}.{last_name}"
                domain = email_domains[role]
            else:
                email_domain = random.choice(email_domains[role])
                base_email = f"{first_name.lower()}{last_name[0].lower()}"
                domain = email_domain

            # Try different numbers until we find a unique email
            email = None
            suffix = ''
            counter = 1
            
            while email is None or email in used_emails:
                if counter > 1:
                    suffix = str(counter)
                email = f"{base_email}{suffix}@{domain}".upper()
                counter += 1
            
            used_emails.add(email)
            
            person = (
                first_name,
                last_name,
                self.faker.phone_number(),
                email,
                role
            )
            self.cursor.execute('''
                INSERT INTO People (FirstName, LastName, PhoneNumber, Email, Role)
                VALUES (?, ?, ?, ?, ?)
            ''', person)
            people_ids.append(self.cursor.lastrowid)
        return people_ids
    
    def _generate_car_info(self, people_ids):
        car_models = {
            'TOYOTA': ['COROLLA', 'YARIS', 'RAV4', 'PRIUS', 'CAMRY', 'AYGO', 'CHR'],
            'HONDA': ['CIVIC', 'JAZZ', 'CRV', 'HRV', 'ACCORD'],
            'FORD': ['FOCUS', 'FIESTA', 'PUMA', 'KUGA', 'MONDEO', 'ECOSPORT'],
            'BMW': ['320I', '520D', 'X3', 'X5', 'M3', 'M5', '118I', '420D'],
            'MERCEDES': ['A180', 'C200', 'E350', 'GLA', 'CLA', 'GLC', 'S500'],
            'AUDI': ['A3', 'A4', 'A6', 'Q3', 'Q5', 'TT', 'RS6'],
            'VOLKSWAGEN': ['GOLF', 'POLO', 'TIGUAN', 'PASSAT', 'TCROSS', 'ID3'],
            'VAUXHALL': ['CORSA', 'ASTRA', 'INSIGNIA', 'MOKKA', 'CROSSLAND'],
            'LAND ROVER': ['DEFENDER', 'DISCOVERY', 'EVOQUE', 'VELAR', 'SPORT']
        }

        for person_id in people_ids:
            make = random.choice(list(car_models.keys()))
            uk_plate = f"{self.faker.random_letter()}{self.faker.random_letter()}{str(random.randint(10, 99))} {self.faker.random_letter()}{self.faker.random_letter()}{self.faker.random_letter()}".upper()
            
            car = (
                uk_plate,
                person_id,
                make,
                random.choice(car_models[make])
            )
            self.cursor.execute('''
                INSERT INTO CarInfo (RegNumber, PersonID, Make, Model)
                VALUES (?, ?, ?, ?)
            ''', car)
    
    def _generate_permits(self, people_ids):
        for person_id in people_ids:
            date_issued = self.faker.date_between(start_date='-1y', end_date='today')
            date_expiry = self.faker.date_between(start_date='today', end_date='+2y')
            
            # Get the RegNumber for this person
            self.cursor.execute('SELECT RegNumber FROM CarInfo WHERE PersonID = ?', (person_id,))
            reg_number = self.cursor.fetchone()[0]
            
            permit = (
                person_id,
                reg_number,
                date_issued,
                date_expiry
            )
            self.cursor.execute('''
                INSERT INTO Permits (PersonID, RegNumber, DateIssued, DateExpiry)
                VALUES (?, ?, ?, ?)
            ''', permit)
    
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    generator = DataGenerator()
    generator.generate_data(10000)
    generator.close()
