import dominate
from dominate.tags import *
dv = div()
dv['class'] = 'form-group'

dv.add(input_("haha",name="test"))
print(dv)
d = div()
with d:
    attr(id='header')
    attr(cls='form-group')

print(d)