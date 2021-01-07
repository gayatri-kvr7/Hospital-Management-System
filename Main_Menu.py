import mysql.connector
import time
mydb = mysql.connector.connect(
  host="localhost",
  user="gayatri",
  password="gayatri123",
  database="myhospitaldatabase"
)

mycursor = mydb.cursor()



def InsertDoctor():
    name = input("Enter doctor name: ")
    specialisation = input("Enter doctor specialisation: ")

    sql = "INSERT INTO DoctorInfoTable (Doctor_Name, Doctor_Specialisation) VALUES (%s, %s)"
    val = (name, specialisation)
    mycursor.execute(sql, val)
    mydb.commit()
    print("." * 20, mycursor.rowcount, "doctor registered." + "." * 20)


def ViewDoctorDetails():
    doctorid=int(input("Enter Doctor Id to view details: "))

    sql=mycursor.execute("Select * from DoctorInfoTable where id=%s" %(doctorid))
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print("ID   NAME    SPECIALIZATION ")
    for x in myresult:
        print (x)
    flag=(len(myresult))
    if(flag==0):
        print("Doctor Unavailable")

def ViewDoctorSchedule():
    doctorid = int(input("Enter Doctor Id to view details: "))
    sql = mycursor.execute("Select DocId,PatientId,ApptDate from AppointmentSummary where DocId=%s" % (doctorid))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    flag = (len(myresult))
    if (flag == 0):
        print("-"*20+"No Appointments Booked for this Doctor "+"-"*20)
    else :
        print("DID PID  Date")
        for x in myresult :
            print(x)



def BookAppointment():
    print("Here is a list of all the doctors: ")
    time.sleep(0.3)
    print("ID   NAME     SPECIALIZATION")
    ViewDocTable()
    docid = int(input("Enter Doctor ID: "))
    appointtime = input("Enter desired appointment date and time(YYYY-MM-DD hh:mm:ss): ")
    value=appointtime
    sql = mycursor.execute("select count(*) from AppointmentSummary where (DocId='{}' and ApptDateTime='{}')".format(docid, value))
    myresult = mycursor.fetchone()
    value2 = myresult[0]
    if (value2 > 1):
        print("-"*15+"The doctor has been already booked for this time and date."+"-"*15)

    else:
        date1 = value.split()[0]
        sql2 = mycursor.execute("select count(*) from AppointmentSummary where (DocId='{}' and ApptDate='{}')".format(docid, date1))
        myresult2 = mycursor.fetchone()
        value3 = myresult2[0]
        print(value3)

        if (value3 > 4):
                print("-"*15+"The doctor has crossed the daily limit of 5 patients. Please try another date or another doctor."+"-"*15)

        else:
                value4= value3+1
                patientid = int(input("Enter Patient ID: "))
                sql2 = "INSERT INTO AppointmentSummary (DocId, PatientId, ApptDateTime) VALUES (%s, %s,%s)"
                val3 = (docid, patientid, appointtime)
                mycursor.execute(sql2, val3)
                mydb.commit()
                print(" " * 20 + "APPOINTMENT BOOKED" + " " * 20)
                print("*"*20+"DETAILS"+"*"*20)
                print(" DOCTOR's  ID               :  ",docid)
                print(" PATIENT's ID               :  ",patientid)
                print(" Appointment date and time  :",appointtime)
                print(" Appointment Number         :",value4)
                print("-"*80)


def InsertPatient():
    PatientName = input("Enter patient name: ")
    age = int(input("Enter Patient age : "))

    sql = "INSERT  INTO PatientInfoTable (Patient_Name, Patient_Age) VALUES (%s, %s)"
    val = (PatientName, age)
    mycursor.execute(sql, val)
    mydb.commit()
    print("." * 20, mycursor.rowcount, "patient registered." + "." * 20)


def ViewPatientDetails():
    patientid=int(input("Enter Patient Id to view details: "))
    sql=mycursor.execute("Select * from PatientInfoTable where id=%s" %(patientid))
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    print(" ID  Name   Age ")
    for x in myresult:
           print(x)
    flag=(len(myresult))
    if(flag==0):
        print("Patient Unavailable in the table")


def ViewDocTable():
    sql = mycursor.execute("Select * from DoctorInfoTable")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for num, i in enumerate(myresult):
        print(str(i[0]) + ".   " + i[1]  + "   " + str(i[2]))


def ViewPatientTable():
    sql = mycursor.execute("Select * from PatientInfoTable")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)



i=1

print("................................................"*100)
print("\t\t*****Welcome to Hospital Management System******")
time.sleep(0.3)
while (i==1):

  print("................................................"*100)
  print("\t\t   ***GET WELL HOSPITAL'S***")
  print("="*100)

  print("1. Administration Login")
  print("2. Patient Login")



  choice=int(input("Enter your choice: "))
  if (choice==1):

      b=int(input("==>Enter password:"))
      if(b==1234):
          time.sleep(0.3)
          print("Welcome, you have registered from the Administration")

          print("1. Add new doctor details")

          print("2. View existing doctor details")
          print("3. View existing doctor schedule ")
          print("4. View the list of Doctors ")
          choice2 = int(input("Enter your choice: "))
          if (choice2 == 1):
              InsertDoctor()
          elif (choice2 == 2):
              ViewDoctorDetails()
          elif (choice2 == 3):
              ViewDoctorSchedule()
          elif (choice2 == 4):
              ViewDocTable()

          else:
              print("Invalid Choice")
      else:
          print(":"*30+"WRONG PASSWORD"+":"*30)

  elif(choice==2):
    time.sleep(0.3)
    print("Welcome, you have registered as a patient")
    print("1. Register as a new patient")
    print("2. View details of an existing patient")
    print("3. Book an appointment")
    print("4. View Patient table")
    choice3=int(input("Enter your choice: "))
    if(choice3==1):
        InsertPatient()
    elif(choice3==2):
       ViewPatientDetails()
    elif(choice3==3):
        BookAppointment()
    elif(choice3==4):
        ViewPatientTable()
    else:
      print("Invalid choice")

  nextchoice=int(input("Press 0 to exit and 1 to continue."))
  i=nextchoice
