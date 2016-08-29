#!/usr/bin/env python
#Guru Data Log Script
#Accel Liberia IDSR Form

import sys

class User:
	print ("Welcome to IDSR CASE FORM")
	IDSR_ID = 0
	Country_Code = 0
	Health_Facility_Code = 0
	Patient_Unique_ID = 0
	Reporting_Health_Facility = ""
	Reporting_District = ""
	Reporting_County = ""

	def display(self):
		print ('')
		print ('User Information:')
		print ('User MON_ID:',self.IDSR_ID)
		print ('User Country_Code:',self.Country_Code)
		print ('User Health_Facility_Code:',self.Health_Facility_Code)
		print ('User Patient_Unique_ID:',self.Patient_Unique_ID)
		print ('User Reporting_Health_Facility:',self.Reporting_Health_Facility)
		print ('User Reporting_District:',self.Reporting_District)
		print ('User Reporting_County:',self.Reporting_County)

	def loadFromInput(self):
		self.IDSR_ID = float(input('Enter the IDSR ID: '))
		self.Country_Code = float(input('Enter the Country Code: '))
		self.Health_Facility_Code = float(input('Enter the Facility Code: '))
		self.Patient_Unique_ID = float(input('Enter the Patient ID: '))
		self.Reporting_Health_Facility = input('Which facility is reporting this case?: ')
		self.Reporting_District = input('Which district is reporting this case?: ')
		self.Reporting_County = input('Which county is this case from?: ')

	def save(self):
		f = open('user.info','w')
		f.write(str(self.IDSR_ID) + '\n')
		f.write(str(self.Country_Code) + '\n')
		f.write(str(self.Health_Facility_Code) + '\n')
		f.write(str(self.Patient_Unique_ID) + '\n')
		f.write(self.Reporting_Health_Facility + '\n')
		f.write(self.Reporting_District + '\n')
		f.write(self.Reporting_County + '\n')
		f.close()

	def loadFromFile(self):
		f = open('user.info', 'r')
		self.IDSR_ID = float(f.readline())
		self.Country_Code = float(f.readline())
		self.Health_Facility_Code = float(f.readline())
		self.Reporting_Health_Facility = f.readline().rstrip()
		self.Reporting_District = f.readline().rstrip()
		self.Reporting_County = f.readline().rstrip()

theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
	theUser = User()
	theUser.loadFromFile()
else:
	theUser = User()
	theUser.loadFromInput()
	theUser.save()

theUser.display()