

def countPairs(arr):
    # Write your code here
    cnt=0
    test=[]
    for x in range(len(arr)):
        for y in range(x):
            if int(arr[x]) & int(arr[y]) in [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072]:
                test.append([arr[x],arr[y]])
                
                cnt+=1
                
    print( cnt)
    print(test)
if __name__ == '__main__':
    
    arr = [1,2,1,3]

   

    result = countPairs(arr)

   
