# CREATE TABLE "Carpark" (
#   "registration" TEXT NOT NULL UNIQUE,
#   "fname" TEXT,
#   "lname" TEXT,
#   "make" TEXT,
#   "model" TEXT,
#   "role" TEXT,
#   PRIMARY KEY ("registration")
# )

import sqlite3

conn = sqlite3.connect("carpark.db")


def usersearchdb(registration, fname, lname, make, model, role):
    sqlquery = """SELECT registration,fname,lname,make,model,role FROM Carpark WHERE registration=? AND fname=? AND lname=? AND make=? AND model=? AND role=? """
    args = (registration, fname, lname, make, model, role)
    cur = conn.execute(sqlquery, args)
    return cur.fetchall()


)
