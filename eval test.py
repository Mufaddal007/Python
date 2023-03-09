str1=input()
str2=str1.split()
str3=[]
for x in range(len(str2)):
    s1=[]
    for y in str2[x]:
        if y.islower():
            s1.append(y.upper())
        elif y.isupper():
            s1.append(y.lower())

    str3.append("".join(s1))


print(" ".join(str3))


#######
def swap_case(s):
       
    str2=s.split()
    str3=[]
    for x in range(len(str2)):
        s1=[]
        for y in s:
            if y.islower():
                s1.append(y.upper())
            elif y.isupper():
                s1.append(y.lower())
            elif y.isdigit():
                s1.append(y)
            elif not y.isspace() or not y.isdigit() or not y.isaplha():
                s1.append(y)
        str3.append("".join(s1))

    str4=" ".join(str3)
    return str4

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
