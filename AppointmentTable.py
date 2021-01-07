import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="gayatri",
  password="gayatri123",
  database="myhospitaldatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE AppointmentSummary (DocId int, PatientId int, ApptDateTime datetime)")
print("Appointment table created successfully")