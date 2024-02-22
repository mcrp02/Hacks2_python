"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    dc = {"a":"@","e":"3","i":"¡","o":"0","u":"v"}
    bank=['f', 'q', 'n', 'x', 'b']
    ls = []
    list=[]
    i = 0

    for r in result:
        if r in dc:
            list.append(dc.get(r))
        elif r in bank:
            list.append(r.upper())
        else:
            list.append(r)
    result = "".join(list)
    return result

r1= fn_hack_3("fooziman")
r2= fn_hack_3("barziman")
r3=fn_hack_3("3q")
r4=fn_hack_3("qu")
r5=fn_hack_3("qux")
print(f"{r1} {r2} {r3} {r4} {r5}")
  
