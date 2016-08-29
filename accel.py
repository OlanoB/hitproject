#!/usr/bin/env python
#Guru Data Log script
#Accel liberia IDSR Form
import sys

class User:
    print ("IDSR CASE ALERT FORM")
    IDSR_ID = 0
    
    def display(self):
        print ('')
        print ('User Information:')
        print ('User IDSR_ID:',self.IDSR_ID)
    
    def loadFromInput(self):
        self.IDSR_ID = float(input('Enter the ID'))
    
    def save(self):
        f = open('user.info','w')
        f.write(str(self.IDSR_ID) + '\n')
        f.close()
        
    def loadFromFile(self):
    	f = open('user.info', 'r')
        self.IDSR_ID = float(f.readline())
        
theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
    theUser = User()
    theUser.loadFromFile()
else:
    theUser = User()
    theUser.loadFromInput()
    theUser.save()
    
theUser.display()