class check:
    a=[]
    def pushchr(self,s):
        self.a.append(s)
        print(s)


o=check()
for x in range(3):
    o.pushchr(x)

print(o.a)
