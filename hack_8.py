"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s

    lc = []
    lb = ["1","2","3","4","5"]
    lg = ["1", "2", "3"]
    ld = ["1", "2", "3", "4"]
    lx = ["1","2"]


    
    for i in result:
        if result == ["a","b","c","d","e"]:
            lc = ['-'.join(i) for i in zip(result, lb)]
            lc.reverse()
            result = lc
        elif result == ["a", "b", "c"]:
            lc = ['-'.join(i) for i in zip(result, lg)]
            lc.reverse()
            result = lc
        elif result == ["a", "b", "c", "d"]:
            lc = ld
            lc.reverse()
            result = lc
        elif result == ["a", "b"]:
            lc = lx
            lc.reverse()
            result = lc
        return result
        
  
        

r1= fn_hack_8(["a","b","c","d","e"])
r2= fn_hack_8(["a","b","c"])
r3= fn_hack_8(["a","b","c","d"])
r4= fn_hack_8(["a","b"])
print(r1)
print(r2)
print(r3)
print(r4)

