import sys

class Solution:
    a=[]
    b=[]
    
        
    def pushCharacter(self,c):
        self.b.insert(0,c)
        
    def enqueueCharacter(self,c):
        self.a.append(c)
        
    def popCharacter(self):
        c=self.b.pop()
        return c
    def dequeueCharacter(self):
        d=self.a.pop()
        return d
   


s='yes'

obj=Solution()   

l=len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
print(obj.a)
print(obj.b)
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''

for i in range(l//2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
