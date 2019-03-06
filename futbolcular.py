#prject definition
#Complaints with EasyGUI

from easygui import *

#https://stackoverflow.com/questions/38982323/why-dont-i-need-to-import-sys
import sys


"""message = 'Welcome'
title = 'Complaints'
msgbox(message, title,'OK')



inform_message = 'Enter personal information'
title = 'Personal Information'
fieldNames = ['Name', 'Email','State','City','Street']



if multenterbox(inform_message,title, fieldNames):
	pass
else:
	sys.exit(0)
"""
gs = list()
bjk = list()
fb = list()

file = open("futbolcular.txt","r")
a =file.readlines()
msg = "Contents of " 
title = "Show File Contents"
codebox(msg, title,a)
	

	



for satır in file:
    satır = satır[:-1]
    satır_elemanları = satır.split(",")
        
    if (satır_elemanları[-1] == "Fenerbahçe"):
         fb.append(satır + "\n")
    elif (satır_elemanları[-1] == "Galatasaray"):
         gs.append(satır + "\n")

    else:
         bjk.append(satır + "\n")
            
file1 = open("gs.txt","w")
for i in gs:
         file1.write(i)
file1.close()        
            

file2 = open("fb.txt","w")
for i in fb:
         file2.write(i)
file2.close()  
          
file3 = open("bjk.txt","w")
for i in bjk:
         file3.write(i)
file3.close()


file.close()

	
options_message = "Which team Do you want to show ?\nOr Press <cancel> to exit."
title = "Team"
options = ["Fb","Gs","Bjk"]
     
choice = choicebox(options_message, title, options)





"""if choice is None:
     sys.exit(0)
       
    

       
if choice == choice[0]:  
	if (satır_elemanları[-1] == "Fenerbahçe"):
		fb.append(satır + "\n")
file = open("fb.txt","r")
a =file.readlines()
file.close()
		
if choice == choice[1]:    
	if (satır_elemanları[-1] == "Galatasaray"):
		b = gs.append(satır + "\n")
msg2 = "Contents of " 
title2 = "Show File Contents"
codebox(msg2, title2,b)

		
else:
text3 = bjk.append(satır + "\n")
msg3 = "Contents of " 
title3 = "Show File Contents"
codebox(msg3, title3,text3)



			
    with open("gs.txt","w") as file1:
        for i in gs:
            file1.write(i)
            
            

    with open("fb.txt","w") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w") as file3:
        for i in bjk:
            file3.write(i)
"""
