import dominate
import sys
from dominate.tags import *
def generateLabel() :
    lblname = input("Please Insert Label Name")
    x = label(lblname,cls="col-md-2 control-label",_for="text-field")
    return x
def generateInput():
    inputname = input("Please Insert Input Name")
    placeholder = input("Please Insert Placeholder")
    c = input_(name=inputname,id=inputname,placeholder=placeholder,cls="form-control")
    return c
def generateSelect():
    selectname = input("Please Insert Select Name")
    placeholder = input("Please Insert Placeholder")
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
print ("Code : 8.Open New DIV Tag")
print ("Code : 9.Close Old Tag")
print ("0 To Exit")
loop_x = 1
dv = div()
dv['class'] = 'form-group'

while loop_x == 1:
    option = input("Please Select Option : ")
    if option == "1":
        lbl = generateLabel()
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(lbl)
        else:
            dv.add(lbl)
    if option == "2":
        txt = generateInput()
        if 'subdiv' in locals():
            subdiv.add(txt)
            print("SUB DIV IS EXIST")
        else:
            dv.add(txt)
    if option == "3":
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(txt)
        else:
            textarea = generateTextarea()
        #print(dv)
        dv.add(textarea)
    if option == "4":   
        s = generateSelect() 
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(txt)
        else:
            dv.add(s)
    if option == "5":
        print(dv)   
    if option == "6":
        dv = div()  
    if option == "0":
        loop_x = 0
    if option == "7":
        str_file = input("What is your file name")
        f = open(str_file, "w+")
        f.write(str(dv))
        f.close()
    if option == "8":
        subdiv = div()
        subdiv['class']="col-md-4"
    if option == "9":
        dv.add(subdiv)    
