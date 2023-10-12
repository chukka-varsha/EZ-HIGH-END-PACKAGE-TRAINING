#sqrt of a num using bs
'''n=int(input())
start=0
end=n//2
floor=-1
while start<=end:
    mid=(start+end)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        start=mid+1
    else:
        end=mid-1
print(floor)'''




'''def sqrt_binary(number,epsilon=1e-8):
    if number<0:
        raise ValueError("connot compute the square")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_squared=mid*mid
        if mid_squared<number:
            left=mid
        else:
            right=mid
    return (left+right)/2
number=int(input())
result=sqrt_binary(number)
print(f"the square root of {number} is approximately",result)'''

#two pointers
'''l=list(map(int,input().split()))
left=0
i=0
right=len(l)-1
while i<right:
    if l[i]==0:
        l[i],l[left]=l[left],l[i]
        left=left+1
        i=i+1
    elif l[i]==1:
        i=i+1
    elif l[i]==2:
        l[i],l[right]=l[right],l[i]
        right=right-1
print(*l)'''
    


