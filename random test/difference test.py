class Difference:
    
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        b=[]
        
        for x in range(len(a)):
            if x==len(a)-1:
                b.append(abs((a[0]-a[x])))
            else:
                b.append(abs(a[x]-a[x+1]))
        b.sort()
        print(b)
        
        self.maximumDifference=b[len(b)-1] 
         

        



	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


