import sqlite3


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("carpark.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        try:
            self.cursor.execute("BEGIN")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS people (
                peopleid INTEGER PRIMARY KEY AUTOINCREMENT,
                fname VARCHAR(50) NOT NULL,
                lname VARCHAR(50) NOT NULL,
                role VARCHAR(10) CHECK(role IN ('STUDENT', 'VISITOR', 'STAFF')) NOT NULL
            )""")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS carinfo (
                carid INTEGER PRIMARY KEY AUTOINCREMENT,
                make VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL,
                reg VARCHAR(20) UNIQUE NOT NULL
            )""")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS permits (
                permitsid INTEGER PRIMARY KEY AUTOINCREMENT,
                peopleid INTEGER NOT NULL,
                carid INTEGER NOT NULL,
                dateissued DATE NOT NULL,
                dateexpiry DATE NOT NULL,
                FOREIGN KEY (peopleid) REFERENCES people(peopleid) ON DELETE CASCADE,
                FOREIGN KEY (carid) REFERENCES carinfo(carid) ON DELETE CASCADE
            )""")
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Database error: {str(e)}")

    def insertintotable(
        self, fname, lname, role, make, model, reg, dateissued, dateexpiry
    ):
        try:
            self.cursor.execute("BEGIN")

            # Insert person
            self.cursor.execute(
                "INSERT INTO people (fname, lname, role) VALUES (?, ?, ?)",
                (fname.upper(), lname.upper(), role.upper()),
            )
            person_id = self.cursor.lastrowid

            # Insert car
            self.cursor.execute(
                "INSERT INTO carinfo (make, model, reg) VALUES (?, ?, ?)",
                (make.upper(), model.upper(), reg.upper()),
            )
            car_id = self.cursor.lastrowid

            # Insert permit
            self.cursor.execute(
                "INSERT INTO permits (peopleid, carid, dateissued, dateexpiry) VALUES (?, ?, ?, ?)",
                (person_id, car_id, dateissued, dateexpiry),
            )

            self.conn.commit()
            return person_id
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Database error: {str(e)}")


class DBViewer:
    def __init__(self):
        self.conn = sqlite3.connect("carpark.db")
        self.cursor = self.conn.cursor()

    # the user will have a pyqt interface where they can input what they want to search for and the data will be filled out in a table, however the data they input can be partial

    def search(
        self, fname=None, lname=None, role=None, make=None, model=None, reg=None
    ):
        # Start with base query joining all tables
        query = """
        SELECT p.peopleid, p.fname, p.lname, p.role, 
               c.make, c.model, c.reg, 
               pm.dateissued, pm.dateexpiry
        FROM people p
        LEFT JOIN permits pm ON p.peopleid = pm.peopleid
        LEFT JOIN carinfo c ON pm.carid = c.carid
        WHERE 1=1
        """
        params = []

        # Add conditions for each non-empty parameter
        if fname:
            query += " AND UPPER(p.fname) LIKE UPPER(?)"
            params.append(f"%{fname}%")
        if lname:
            query += " AND UPPER(p.lname) LIKE UPPER(?)"
            params.append(f"%{lname}%")
        if role:
            query += " AND UPPER(p.role) = UPPER(?)"
            params.append(role)
        if make:
            query += " AND UPPER(c.make) LIKE UPPER(?)"
            params.append(f"%{make}%")
        if model:
            query += " AND UPPER(c.model) LIKE UPPER(?)"
            params.append(f"%{model}%")
        if reg:
            query += " AND UPPER(c.reg) LIKE UPPER(?)"
            params.append(f"%{reg}%")

        self.cursor.execute(query, params)
        return self.cursor.fetchall()
