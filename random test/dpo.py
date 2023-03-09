n=int(input())

if 1700<n<1918 :
    if n%4==0:
        print("12.09.{}".format(n))    
    else:
        print("13.09.{}".format(n))
elif n==1918:
    print("26.09.1918")
elif 1918<n<2700:
    if n%400 or (n%4==0 and n%100!=0):
        print("12.09.{}".format(n)) 
    else:
        print("13.09.{}".format(n))

        



