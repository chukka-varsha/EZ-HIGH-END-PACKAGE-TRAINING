#linear search
arr=[5,2,3,7,3,5,4,8,5,67,4]
key=7
found=False
for index in range(len(arr)):
    if arr[index]==key:
        print("element found",index)
        found=True
        break
if found==False:
    print("element not found")
    
#floor number using bs
'''def bs_floor(l,key,si,li,floor):
    if(si<=li):
        mid=(si+li)//2
        if l[mid]==key:
            return l[mid]
        if l[mid]<key:
            floor=l[mid]
            return bs_floor(l,key,mid+1,li,floor)
        else:
            return bs_floor(l,key,si,mid-1,floor)
    return floor
l=list(map(int,input().split()))
key=int(input())
print(bs_floor(l,key,0,len(l)-1,-1))'''




#ceil number using bs
'''def bs_ceil(l,key,si,li,ceil):
    if(si<=li):
        mid=(si+li)//2
        if l[mid]==key:
            return l[mid]
        if l[mid]<key:
            return bs_ceil(l,key,mid+1,li,ceil)
        else:
            ceil=l[mid]
            return bs_ceil(l,key,si,mid-1,ceil)
    return ceil
l=list(map(int,input().split()))
key=int(input())
print(bs_ceil(l,key,0,len(l)-1,-1))'''


#subset of palindromes
'''def palin(s):
    n=len(s)
    def palin_rev(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=[]
    for i in range(len(s)):
        pal=palin_rev(i,i)
        if len(pal)>1:
            res.append(pal)
        pal2=palin_rev(i,i+1)
        if len(pal2)>1:
            res.append(pal2)
    return res
s=input()
print(palin(s))'''











        













    
    




 