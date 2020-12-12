import dominate
import sys
from dominate.tags import *
def listcommand():
    print ("Welcome To HTML Generator :")
    print ("Select Option ")
    print ("Code : 1. label 2.text 3.textarea 4.select ")
    print ("Prese 5 to preview");
    print ("Code : 1. = create label")
    print ("Code : 2. = create text")
    print ("Code : 3. = create textareat")
    print ("Code : 4. = create select")
    print ("Code : 5. = preview result")
    print ("Code : 6. = reset")
    print ("COde : 7. = save to file")
    print ("Code : 8. = open new tag")
    print ("Code : 9. = close tag")
    print ("Code : 0. = To Exit")
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
    c = textarea(name=textareaname,id=textareaname,cls="form-control")
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
print ("Code : 1. = create label")
print ("Code : 2. = create text")
print ("Code : 3. = create textarea")
print ("Code : 4. = create select")
print ("Code : 5. = preview result")
print ("Code : 6. = reset")
print ("COde : 7. = save to file")
print ("Code : 8. = open div tag")
print ("Code : 9. = close tag")
print ("Code : 0. = To Exit")
loop_x = 1
dv = div()
dv['class'] = 'form-group'

while loop_x == 1:
    option = input("Please Select Option : ")
    if option == "1" or option == "create label":
        lbl = generateLabel()
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(lbl)
        else:
            dv.add(lbl)
    if option == "2" or option == "create text":
        txt = generateInput()
        if 'subdiv' in locals():
            subdiv.add(txt)
            print("SUB DIV IS EXIST")
        else:
            dv.add(txt)
    if option == "3" or option == "create textarea":
        txtarea = generateTextarea()
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(txtarea)
        else:
            dv.add(txtarea)
    if option == "4" or option == "create select":   
        s = generateSelect() 
        if 'subdiv' in locals():
            print("SUB DIV IS EXIST")
            subdiv.add(s)
        else:
            dv.add(s)
    if option == "5" or option == "preview result":
        print(dv)   
    if option == "6" or option == "reset":
        dv = div()  
    if option == "0" or option == "exit":
        loop_x = 0
    if option == "7" or option == "save to file" :
        str_file = input("What is your file name")
        f = open(str_file, "w+")
        f.write("\n")
        f.write(str(dv))
        f.close()
    if option == "8" or option == "open div tag" :
        subdiv = div()
        subdiv['class']="col-md-10"
    if option == "9":
        dv.add(subdiv) 
