import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="gayatri",
  password="gayatri123",
  database="myhospitalmangementdb"
)

mycursor = mydb.cursor()


if mydb.is_connected():
    print("Database opened successfully")
else:
    print("Error opening database")


drop_table = "DROP TABLE IF EXISTS menu"
mycursor.execute(drop_table)
mycursor.execute("CREATE TABLE PatientInfoTable (Patient_No INT AUTO_INCREMENT PRIMARY KEY, Patient_Name VARCHAR(255),Patient_Age int,Patient_City VARCHAR(255), Patient_Covid_Report VARCHAR(255))")
print("Patient table created successfully")
