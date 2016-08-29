#!/usr/bin/env python
#Guru Data Log Script
#Written by OLANO TEAH BLOH
#Accel Liberia IDSR Form

import sys

class User:
	print ('')
	print ("============================================================================================")
	print ("Welcome to IDSR CASE FORM", "Welcome to IDSR CASE FORM", "Welcome to IDSR FORM")
	print ("============================================================================================")
	IDSR_ID = 0
	Country_Code = 0
	Health_Facility_Code = 0
	Patient_Unique_ID = 0
	Reporting_Health_Facility = ""
	Reporting_District = ""
	Reporting_County = ""
	Name_Of_Patient = ""
	Date_Of_Birth = 0
	Age_DOB_Unknown = 0
	Community_Of_Residence = ""
	District_Of_Residence = ""
	Sex = ""
	Locating_Information = ""
	Date_Onset = 0
	Date_Seen = 0

	def display(self):
		print ('')
		print ('User Information:')
		print ('User IDSR_ID:',self.IDSR_ID)
		print ('User Country_Code:',self.Country_Code)
		print ('User Health_Facility_Code:',self.Health_Facility_Code)
		print ('User Patient_Unique_ID:',self.Patient_Unique_ID)
		print ('User Reporting_Health_Facility:',self.Reporting_Health_Facility)
		print ('User Reporting_District:',self.Reporting_District)
		print ('User Reporting_County:',self.Reporting_County)
		print ('User Name_Of_Patient:',self.Name_Of_Patient)
		print ('User Date_Of_Birth:',self.Date_Of_Birth)
		print ('User Age_DOB_Unknown:',self.Age_DOB_Unknown)
		print ('User Community_Of_Residence:',self.Community_Of_Residence)
		print ('User District_Of_Residence:',self.District_Of_Residence)
		print ('User Sex:',self.Sex)
		print ('User Locating_Information:',self.Locating_Information)
		print ('User Date_Onset:',self.Date_Onset)
		print ('User Date_Seen:',self.Date_Seen)

	def loadFromInput(self):
		self.IDSR_ID = float(input('Enter the IDSR ID: '))
		self.Country_Code = float(input('Enter the Country Code: '))
		self.Health_Facility_Code = float(input('Enter the Facility Code: '))
		self.Patient_Unique_ID = float(input('Enter the Patient ID: '))
		self.Reporting_Health_Facility = input('Which facility is reporting this case?: ')
		self.Reporting_District = input('Which district is reporting this case?: ')
		self.Reporting_County = input('Which county is this case from?: ')
		self.Name_Of_Patient = input('What is the name of the patient?: ')
		self.Date_Of_Birth = input('What is the patient date of birth?: ')
		self.Age_DOB_Unknown = float(input('What is the age, if the date of birth is unknown?: '))
		self.Community_Of_Residence = input('Which community the patient resides?: ')
		self.District_Of_Residence = input('What is the patient present address?: ')
		self.Sex = input('What is the gender of the patient (male or female?: ')
		self.Locating_Information = input('Please provide details description of the patient present location: ')
		self.Date_Onset = input('When did the patient got sick?: ')
		self.Date_Seen = input('When did you received the form?: ')

	def save(self):
		f = open('user.info','w')
		f.write(str(self.IDSR_ID) + '\n')
		f.write(str(self.Country_Code) + '\n')
		f.write(str(self.Health_Facility_Code) + '\n')
		f.write(str(self.Patient_Unique_ID) + '\n')
		f.write(self.Reporting_Health_Facility + '\n')
		f.write(self.Reporting_District + '\n')
		f.write(self.Reporting_County + '\n')
		f.write(self.Name_Of_Patient + '\n')
		f.write(self.Date_Of_Birth + '\n')
		f.write(str(self.Age_DOB_Unknown) + '\n')
		f.write(self.Community_Of_Residence + '\n')
		f.write(self.District_Of_Residence + '\n')
		f.write(self.Sex + '\n')
		f.write(self.Locating_Information + '\n')
		f.write(self.Date_Onset + '\n')
		f.write(self.Date_Seen + '\n')
		f.close()

	def loadFromFile(self):
		f = open('user.info', 'r')
		self.IDSR_ID = float(f.readline())
		self.Country_Code = float(f.readline())
		self.Health_Facility_Code = float(f.readline())
		self.Reporting_Health_Facility = f.readline().rstrip()
		self.Reporting_District = f.readline().rstrip()
		self.Reporting_County = f.readline().rstrip()
		self.Name_Of_Patient = f.readline().rstrip()
		self.Date_Of_Birth = float(f.readline())
		self.Age_DOB_Unknown = f.readline().rstrip()
		self.Community_Of_Residence = f.readline().rstrip()
		self.District_Of_Residence = f.readline().rstrip()
		self.Sex = f.readline().rstrip()
		self.Locating_Information = f.readline().rstrip()
		self.Date_Onset = f.readline().rstrip()
		self.Date_Seen = f.readline().rstrip()

theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
	theUser = User()
	theUser.loadFromFile()
else:
	theUser = User()
	theUser.loadFromInput()
	theUser.save()

theUser.display()