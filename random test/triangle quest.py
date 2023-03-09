n=int(input())
ones=0
for y in range(1,n):
    ones+pow(10,(y-1))
    print(y*ones)
