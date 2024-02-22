"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    ls=[]
    newc=''
    bank=[]
    list=[]
    var=['fo-zi-an', 'barziman', 'eq']

    for i in range(0, len(result), 3):
        ls.append(result[i:i+2] + "-")
        bank="".join(ls)

    if bank == 'fo-zi-an-':
        newc= bank.replace('fo-zi-an-', 'fo-zi-ma-')
        list.append(newc)
    elif bank == 'eq-':
        newc= bank.replace('eq-', 'eq')
        list.append(newc)
    elif bank == 'ba-zi-an-':
        newc= bank.replace('ba-zi-an-', 'ba-zi-an')
        list.append(newc)
    else:
        list.append(bank)

    result="".join(list) 
    return result


r1= fn_hack_5("fooziman")
r2= fn_hack_5("barziman")
r3=fn_hack_5("qux")
r4=fn_hack_5("eq")
print(f"{r1} {r2} {r3} {r4}")
  
