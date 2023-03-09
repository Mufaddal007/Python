#declaring inputs, Taking inputs and creating splitted array of inputs
n = int(input())
a = []
for x in range(n):
    a.append(input().split())
query_name=input("Enter query name--->")

#creating ditionary 
testdic={}
for x in range(0,len(a)):
    testdic[a[x][0]]=a[x][1:4]

#calculating average    
ave=0
for x in testdic[query_name]:
   ave+=float(x)

#finalizating output    
ave=ave/len(testdic[query_name])

#printing output
forave="{:.2f}".format(ave)
print(forave)
