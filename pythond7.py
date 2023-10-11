#quick sort
'''def quicksort(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def fun(l,start,end):
    if start<end:
        pi=quicksort(l,start,end)
        fun(l,start,pi-1)
        fun(l,pi+1,end)
l=list(map(int,input().split()))
fun(l,0,len(l)-1)
print(l)'''

#inversion count
'''l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count=count+1
print(count)'''



#Mergesorting: for the sorted two arrays i.e.,left and right.
'''def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        print(left,right)
        mergel=merge(left,right)
        #print(mergel)
        return mergel
    return l
def merge(left,right):
    res=[]
    i=j=k=0   #left=right=res=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
l=[3,9,3,1,0]
print(mergesort(l))'''


#without the merge function
'''def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0         #left=right=res=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
l=list(map(int,input().split()))
mergesort(l)
print(l)'''

#merge with inversion count

'''def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0         #left=right=res=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1
        return li+ri+inversion
    return 0
l=[22, 54, 52, 417, ]
print("Inversion count:",mergesort(l,0))
print(l)'''









#subset sum
'''def fun(l,target):
    def bt(start,sum,subset):
        if sum==target:
            res.append(subset[:])
            return 
        if sum>target or start==len(l):
            return
        subset.append(l[start])
        bt(start+1,sum+l[start],subset)
        subset.pop()
        bt(start+1,sum,subset)
        
    res=[]
    bt(0,0,[])
    return res
    
l=list(map(int,input().split()))
n=int(input())
result=fun(l,n)
print(*result,sep='\n')'''

'''def fun(l, target):
    def bt(start, sum, subset):
        if sum == target:
            res.append(subset[:])
            return
        if sum > target or start == len(l):
            return
        subset.append(l[start])
        bt(start + 1, sum + l[start], subset)
        subset.pop()
        bt(start + 1, sum, subset)

    res = []
    bt(0, 0, [])
    return res

l = list(map(int, input().split()))
n = int(input())
result = fun(l, n)

for subset in result:
    print(subset)'''

                          


