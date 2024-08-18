import psycopg2
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def load_dbconfig(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

dbconfig = load_dbconfig("../../config/db.json")

conn = psycopg2.connect(
    database = dbconfig["database"]["name"],
    user = dbconfig["database"]["user"],
    password = dbconfig["database"]["password"],
    host = dbconfig["database"]["host"],
    port = dbconfig["database"]["port"]
    )

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tripDetails(
    uid SERIAL PRIMARY KEY,
    origin VARCHAR(50),
    destination VARCHAR(50),
    start_date DATE,
    end_date DATE,
    noofppl INT,
    budget FLOAT,
    pref VARCHAR(100),
    helpp VARCHAR(100),
    itinerary JSONB);
    """)


uid = input("Enter User ID: ")
origin = input("Enter city of departure: ")
destination = input("Enter city of arrival: ")
start_date = input("Enter date of departure: (DD/MM/YYYY) :")
end_date = input("Enter date of return: (DD/MM/YYYY) :")
noofppl = input("Enter number of travelers: ")
budget = input("Enter budget: ")
pref = input("Describe your preferred activities during vacation: ")
helpp = input("Enter the kind of help you need with booking(s) :")

detail_list = [uid, origin, destination, start_date, end_date, noofppl, budget, pref, helpp]


sql = "INSERT INTO tripDetails(uid, origin, destination, start_date, end_date, noofppl, budget, pref, helpp) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s, %s);"
cur.execute(sql, detail_list)

conn.commit()
cur.close()
conn.close()
