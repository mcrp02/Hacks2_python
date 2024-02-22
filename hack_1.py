"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    bank = []
    ls=[]

    for i in range(0, len(result), 3):
        ls.append(result[i:i+3])
        

    for l in ls:
        if(len(l) % 2 != 0):
            container = f"{l[0]}{l[1].upper()}{l[2]}"
            bank.append(container)
        else:
            bank.append(l)    
    result="".join(bank)
    return result



  
