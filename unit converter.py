import math
pre=['yocto','zepto','atto','femto','pico','nano','micro','milli','centi','deci','Deca','Hecto','kilo','Mega','Giga','tera','Peta',\
     'Exa','Zetta','Yotta']
nots=['y','z','a','f','p','n','u','m','c','d','da','h','k','M','G','T','P','E','Z','Y']
tens1=[-24,-21,-18,-15,-12,-9,-6,-3,-2,-1,1,2,3,6,9,12,15,18,21,24]
while 1:
    ui1=input("which unit you want to convert from ?\n")
    ui2=input("which unit you want to convert to?\n")
    c=tens1[nots.index(ui2)]-tens1[nots.index(ui1)]
    print(pow(10,c),pre[nots.index(ui1)])

