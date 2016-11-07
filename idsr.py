#!/usr/bin/env python
#Guru Data Log script
#Accel liberia IDSR Form
import sys

class User:
    print ("IDSR CASE ALERT FORM")
    IDSR_ID = 0
    Country_Code = 0
    Health_Facility_code = 0
    Patient_Unique_ID = 0
    Reporting_Health_Fac = ""
    Reporting_District = ""
    Reporting_County = ""
    Name_Of_Patient = ""
    Date_Of_Birth = ""
    Age_DOB_Unknow = 0
    Community_Of_Residence = ""
    District_Of_Residence = ""
    Sex = ""
    Locating_Information = ""
    Date_Of_Onset = 0
    Date_Seen = 0
    
    def display(self):
        print ('')
        print ('User Information:')
        print ('User IDSR_ID:',self.IDSR_ID)
        print ('User Country_Code:',self.Country_Code)
        print ('User Health_Facility_code:',self.Health_Facility_code)
        print ('User Patient_Unique_ID:',self.Patient_Unique_ID)
        print ('User Reporting_Health_Fac:',self.Reporting_Health_Fac)
        print ('User Reporting_District:',self.Reporting_District)
        print ('User Reporting_County:',self.Reporting_County)
        print ('User Name_Of_Patient:',self.Name_Of_Patient)
        print ('User Date_Of_Birth:',self.Date_Of_Birth)
        print ('User Age_DOB_Unknow:',self.Age_DOB_Unknow)
        print ('User Community_Of_Residence:',self.Community_Of_Residence)
        print ('User District_Of_Residence:',self.District_Of_Residence)
        print ('User Sex:',self.Sex)
        print ('User Locating_Information  :',self.Locating_Information)
        print ('User Date_Of_Onset:',self.Date_Of_Onset)
        print ('User Date_Seen:',self.Date_Seen)
    
    def loadFromInput(self):
        self.IDSR_ID = float(input('Enter the ID'))
        self.Country_Code = float(input('Enter the Country Code'))
        self.Health_Facility_code = float(input('Enter the health facility code'))
        self.Patient_Unique_ID = float(input('Enter Patient ID:'))
        self.Reporting_Health_Fac = input('Enter Reporting Health facility:')
        self.Reporting_District = input('Enter the district')
        self.Reporting_County = input('Enter the county')
        self.Name_Of_Patient = input('Name of Patient')
        self.Date_Of_Birth = float(input('Enter date of birth'))
        self.Age_DOB_Unknow = float(input('Enter the date of birth'))
        self.Community_Of_Residence = input('Enter the community')
        self.District_Of_Residence = input('Enter the district')
        self.Sex = input('Enter your sex (Male or Female)')
        self.Locating_Information = input('Enter the lcation')
        self.Date_Of_Onset = float(input('Enter the date of Onset:'))
        self.Date_Seen = float(input('Enter the date of seen:'))
    
    def save(self):
        f = open('user.info','w')
        f.write(str(self.IDSR_ID) + '\n')
        f.write(str(self.Country_Code) + '\n')
        f.write(str(self.Health_Facility_code) + '\n')
        f.write(str(self.Patient_Unique_ID) + '\n')
        f.write(self.Reporting_Health_Fac + '\n')
        f.write(self.Reporting_District + '\n')
        f.write(self.Reporting_County + '\n')
        f.write(self.Name_Of_Patient + '\n')
        f.write(str(self.Date_Of_Birth) + '\n')
        f.write(str(self.Age_DOB_Unknow) + '\n')
        f.write(self.Community_Of_Residence + '\n')
        f.write(self.District_Of_Residence + '\n')
        f.write(self.Sex + '\n')
        f.write(self.Locating_Information + '\n')
        f.write(str(self.Date_Of_Onset) + '\n')
        f.write(str(self.Date_Seen) + '\n')
        f.close()
        
    def loadFromFile(self):
    	f = open('user.info', 'r')
        self.IDSR_ID = float(f.readline())
        self.Country_Code = float(f.readline())
        self.Health_Facility_code = float(f.readline())
        self.Patient_Unique_ID = float(f.readline())
        self.Reporting_Health_Fac = f.readline().rstrip()
        self.Reporting_District = f.readline().rstrip()
        self.Reporting_County = f.readline().rstrip()
        self.Name_Of_Patient = f.readline().rstrip()
        self.Date_Of_Birth = float(f.readline())
        self.Age_DOB_Unknow = float(f.readline())
        self.Community_Of_Residence = f.readline().rstrip()
        self.District_Of_Residence = f.readline().rstrip()
        self.Sex = f.readline().rstrip()
        self.Locating_Information = f.readline().rstrip()
        self.Date_Of_Onset = float(f.readline())
        self.Date_Seen = float(f.readline())

        
theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
    theUser = User()
    theUser.loadFromFile()
else:
    theUser = User()
    theUser.loadFromInput()
    theUser.save()
    
theUser.display()