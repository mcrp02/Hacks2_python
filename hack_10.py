"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    c = 1
    ls = []
    
    for i in result:
        if isinstance(i, dict):
            nd = {str(c): str(c + 1)}
            ls.append(nd)
            c += 2
        else:
            ns = {str(c), str(c + 1)}
            ls.append(ns)
    result = ls   
    return result


r1= fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}] )
print(r1)

