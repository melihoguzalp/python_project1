#prject definition
#Complaints with EasyGUI

from easygui import *

#https://stackoverflow.com/questions/38982323/why-dont-i-need-to-import-sys
import sys


message = 'Welcome'
title = 'Complaints'
msgbox(message, title,'OK')




file = open("futbolcular.txt","r")
a =file.readlines()
msg = "Mix teams and players " 
title = "Show Player Details"
codebox(msg, title,a)
	


with open("futbolcular.txt","r") as file:
    
    fb = list()
    gs = list()
    bjk = list()
    
    for line in file:
        line = line[:-1]
        line_component = line.split(",")
        
        if (line_component[-1] == "Fenerbahçe"):
            fb.append(line + "\n")
        elif (line_component[-1] == "Galatasaray"):
            gs.append(line + "\n")
		
        else:
            bjk.append(line + "\n")
    
      
    with open("fb.txt","w") as file1:
        for i in fb:
            file1.write(i)  
    
            
    with open("gs.txt","w") as file2:
        for i in gs:
            file2.write(i)
            
  
    with open("bjk.txt","w") as file3:
        for i in bjk:
            file3.write(i)

options_message = "Which team Do you want to show ?\nOr Press <cancel> to exit."
title = "Team"
options = ["Fb","Gs","Bjk"]
     
choice = choicebox(options_message, title, options)

if choice == options[0]:
	file1 = open("fb.txt","r")
	a =file1.readlines()
	file1.close()
	msg = "Contents of " 
	title = "Show File Contents"
	codebox(msg, title,a)
	
elif choice == options[1]:
	file2 = open("gs.txt","r")
	c =file2.readlines()
	file.close()
	msg2 = "Contents of " 
	title2 = "Show File Contents"
	codebox(msg2, title2,c)

else:
	choice == options[2]
	file3 = open("bjk.txt","r")
	d =file3.readlines()
	file3.close()
	msg3 = "Contents of " 
	title3 = "Show File Contents"
	codebox(msg3, title3,d)
