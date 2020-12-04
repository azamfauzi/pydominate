import dominate
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
    
print ("Welcome To HTML Generator :")
print ("Select Option ")
print ("Code : 1. label 2.text 3.textarea 4. groupclass")
print ("0 To Exit")

option = input("Please Select Option : ")

dv = div()

dv['class'] = 'form-group'
dv.add(input_("haha",name="test",cls="form-control"))

#print(dv)
d = div()
with d:
    attr(id='header')
    attr(cls='form-group')
dv.add(d)
lbl = generateLabel()
x = generateInput()
s = generateSelect()
#dv.add(lbl)
#dv.add(x)  
dv.add(s)
print(dv)