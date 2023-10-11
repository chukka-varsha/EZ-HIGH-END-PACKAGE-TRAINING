#bubble sort
'''l=list(map(int,input().split()))
n=len(l)
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''



#selection sort
'''l=list(map(int,input().split()))
n=len(l)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
            
print(l)'''



#insertion sort
'''l=list(map(int,input().split()))
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)'''





#magic square with loops
'''n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:
    print(*i)
print("magic constant is:",n*(n*n+1)//2)'''

#using recusrion
'''def generate(n):
    sq=[[0]*n for i in range(n)]
    def fill(i,j,num):
        if num>(n*n):
            return sq
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if sq[i][j]:
            i=i+1
            j=j-2
            return fill(i,j,num)
        sq[i][j]=num
        return fill(i-1,j+1,num+1)
    return fill(n//2,n-1,1)
    
    
n=int(input())
for i in generate(n):
    print(*i)'''

#subset sum
'''def check(arr,target,n):
    if target==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target:
        return check(arr,target,n-1)
    return check(arr,target-arr[n-1],n-1) or check(arr,target,n-1)
    


arr=[3,12,5,4,24,2]
target=9
z=check(arr,target,len(arr))
if z==True:
    print("true")
else:
    print("false")'''





