"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    ls = []
    
    for i in result:
        if i == "a":
            ls.append(i.replace("a", "1"))
        elif i =="b":
            ls.append(2)
        elif i == "c":
            ls.append(i.replace("c", "3"))
        elif i == "d":
            ls.append(4)
        elif i == "e":
            ls.append(i.replace("e", "5"))
    if not ls:
        return [0]
        
    return ls


r1= fn_hack_7(["a","b","c","d","e"])
r2= fn_hack_7([])

print(r1)
print(r2)
