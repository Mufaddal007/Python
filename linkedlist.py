class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        head=[]
        print(head)
class Solution: 
    a=[]
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
        
    head=[]
    def insert(self,head,data):
        no=Node(data)
        head=no.data
        
        
        
        
        
mylist= Solution()
#T=int(input())
head=None
for i in range(3):
    data=i
    head=mylist.insert(head,data)    
mylist.display(head); 	  
