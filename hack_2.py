"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    v = ["a","e","i","o","u"]
    bank=[]
    
    for i in result:
        if i not in v:
            bank.append(i)        
    result= "".join(bank)    
    return result

