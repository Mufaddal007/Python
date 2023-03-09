import textwrap

def wrap(string, max_width):
    strarr=textwrap.wrap(string,max_width)
    
    for x in range(0,len(strarr)):
        if x !=None:
            return strarr[x]
    
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
