import dominate
import sys
from dominate.tags import *
def generateLabel() :
    lblname = input("Please Insert Label Name")
    x = label(lblname,cls="col-md-2 control-label")
    return x
def generateInput():
    inputname = input("Please Insert Input Name")
    c = input_(name=inputname,id=inputname)
    return c
def generateSelect():
    selectname = input("Please Insert Select Name")
    c = select(name=selectname,cls="form-control")
    #c.add(option())
    return c
def generateTextarea():
    textareaname = input("Please Insert Textarea Name")
    c = textarea(name=textareaname,cls="form-control")
    return c
def generateP():
    selectname = input("Please Insert Select Name")
    c = select(name=selectname,cls="form-control")
    #c.add(option())
    return c

print ("Welcome To HTML Generator :")
print ("Select Option ")
print ("Code : 1. label 2.text 3.textarea 4.select ")
print ("Prese 5 to preview");
print ("Code : 1. label ")
print ("Code : 2. text")
print ("Code : 3.textarea 4.select ")
print ("Code : 4.select ")
print ("Code : 5.Preview ")
print ("Code : 6.Reset")
print ("COde : 7.Save To File")
print ("0 To Exit")
loop_x = 1
dv = div()
dv['class'] = 'form-group'

while loop_x == 1:
	option = input("Please Select Option : ")
	if option == "1":
		lbl = generateLabel()
		dv.add(lbl)
	if option == "2":
		txt = generateInput()
		dv.add(txt)
	if option == "3":
		textarea = generateTextarea()
		#print(dv)
		dv.add(textarea)
	if option == "4":	
		s = generateSelect() 
		dv.add(s)
	if option == "5":
		print(dv)	
	if option == "6":
		dv = div()	
	if option == "0":
		loop_x = 0
	if option == "7":
		f = open("demofile2.txt", "w+")
		f.write(str(dv))
		f.close()
