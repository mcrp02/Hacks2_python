"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

def fn_hack_4(s):
    result = s
    bank=['f','n','b']
    ls=[]
    
    for i in result:
        if i not in bank:
            ls.append(i)
    result="".join(ls)
    return result


r1= fn_hack_4("fooziman")
r2= fn_hack_4("barziman")
r3=fn_hack_4("qux")
print(f"{r1} {r2} {r3}")
