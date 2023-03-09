#Write your code here
import math


class Calculator():
    def power(self,n,p):
        self.n = n
        self.p = p
        if n>0 and p>0:
            a=pow(n,p)
            return a
        else:
            raise Exception("n and p should be non-negative")
    


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
