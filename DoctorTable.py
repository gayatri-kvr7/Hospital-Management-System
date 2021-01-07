import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="gayatri",
  password="gayatri123",
  database="myhospitaldatabase"
)

mycursor = mydb.cursor()


if mydb.is_connected():
    print("Database opened successfully")
else:
    print("Error opening database")



mycursor.execute("CREATE TABLE DoctorInfoTable (id INT AUTO_INCREMENT PRIMARY KEY, Doctor_Name VARCHAR(255),Doctor_Specialisation VARCHAR(255))")
print("Doctor table created successfully")