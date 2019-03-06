#prject definition
#Complaints with EasyGUI

from easygui import *

#https://stackoverflow.com/questions/38982323/why-dont-i-need-to-import-sys
import sys



#welcoome message
message = 'Welcome'
title = ''
msgbox(message, title,'OK')



#to read singer file
file = open("singer.txt","r")
singer_read =file.readlines()
msg = "Mix Country and Singer " 
title = "Show Singer Details"
codebox(msg, title,singer_read)



#to add new singer

addsinger = open("singer.txt","a")
title = "titleSinger"
newsinger = enterbox("Name of Singer and Country",title)

if(newsinger):
	addsinger.write( newsinger+"\n")
	addsinger.close()
else:
	addsinger.close()	
	sys.exit(0)



#to show added new singer

file = open("singer.txt","r")
singer_read =file.readlines()
msg = "Mix Countries and Singers " 
title = "Show Singer Details"
codebox(msg, title,singer_read)	


	
file = open("singer.txt","r") 
for line in file:
	line = line[:-1]
	line_component = line.split(",")
	
	tr = []
	eng = []
	fr = []

if (line_component[-1] == "Tukey"):
	tr.append(line + "\n")
elif (line_component[-1] == "England"):
	eng.append(line + "\n")	
else:
	fr.append(line + "\n")
            
	
      
file1 = open("tr.txt","w")
for i in tr:
	file1.write(i)  
file1.close()    
            
file2 = open("eng.txt","w") 
for i in eng:
	file2.write(i)
file2.close()            
  
file3 = open("fr.txt","w") 
for i in fr:
	file3.write(i)
file3.close()




#choose a country to see added new singer

options_message = "Which country do you want to show ?\nOr Press <cancel> to exit."
title = "Team"
options = ["England","France","Turkey"]
     
choice = choicebox(options_message, title, options)




#to see all Turkish singers

if choice == "Turkey":
	file1 = open("tr.txt","r")
	turkey_read =file1.readlines()
	file1.close()
	msg = "Turkish Singer" 
	title = "Show File Contents"
	codebox(msg, title,turkey_read)
	
	
#to see all British singers	

elif choice == "England":
	file2 = open("eng.txt","r")
	england_read =file2.readlines()
	file.close()
	msg2 = "British Singer " 
	title2 = "Show File Contents"
	codebox(msg2, title2,england_read)


#to see all French singers

elif choice == "France":
	file3 = open("fr.txt","r")
	france_read =file3.readlines()
	file3.close()
	msg3 = "French Singer " 
	title3 = "Show File Contents"
	codebox(msg3, title3,france_read)


#exit
else:
	sys.exit(0)


