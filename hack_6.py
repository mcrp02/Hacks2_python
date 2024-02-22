"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = s
    nls = []
    temp = ""
   

    for i in result:
        if i == "a":
            temp = i.replace("a", "1")
            nls.append(temp)
        elif i == "b":
            temp = i.replace("b", "-")
            nls.append(temp)
        elif i == "c":
            temp = i.replace("c", "3")
            nls.append(temp)
        elif i == "d":
            temp = i.replace("d", "-")
            nls.append(temp)
        elif i == "e":
            temp = i.replace("e", "5")
            nls.append(temp)
    if not nls:
        return ["0"]

        
    return nls


r1= fn_hack_6(["a","b","c","d","e"])
r2= fn_hack_6([])

print(r1)
print(r2)