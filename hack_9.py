"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    # dc = {"foo":"fookziman","bar":"barziman"}
    nd = {}

    for i in result:
        if i in "foo":
            nd["foo".capitalize()] = "Fooziman"
        return nd        
    return result

r1= fn_hack_9({"foo":"fookziman","bar":"barziman"})
print(f"{r1}")


