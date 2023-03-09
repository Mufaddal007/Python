n=50
for x in range(n,0,-1):
        y=list(str(x))
        y.reverse()
        if y==list(str(x)):
                print("".join(y))
                print("check")
