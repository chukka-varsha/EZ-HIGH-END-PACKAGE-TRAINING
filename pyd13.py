#two pointers
'''def fun(l,target):
    left=0
    right=len(l)-1
    while left<right:
        if l[left]+l[right]==target:
            return [left,right]
        elif (l[left]+l[right]<target):
            left=left+1
        else:
            rigth=right-1
l=list(map(int,input().split()))
target=int(input())
x=fun(l,target)
print(x)'''
#knapsack
'''def knapsack(W,wt,val,n):
    dp=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]=0
            elif wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][W-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][w]
val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
print(knapsack(W,wt,val,n))'''

#rotated array
#leetcode: 189
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


'''def rotate(nums,k):
    for i in range(k):
        a=nums.pop()
        nums.insert(0,a)
    return nums
nums=list(map(int,input().split()))
k=int(input())
print(rotate(nums,k))'''

#search_in-rotated_array
#leetcode-33
"""Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""


'''def search(nums,target):
    si=0
    li=len(nums)-1
    while si<=li:
        mid=(si+li)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>=nums[si]:
            if target>=nums[si] and target<=nums[mid]:
                li=mid-1
            else:
                si=mid+1
        else:
            if target>nums[mid] and target<=nums[li]:
                si=mid+1
            else:
                li=mid-1
     return -1
    
nums=list(map(int,input().split()))
target=int(input())
print(search(nums,target))'''


#three pointers
'''def fun(l,target):
    for p3 in range(len(l)-2):
        p1=p3+1
        p2=len(l)-1
        while p1<=p2:
            if l[p1]+l[p2]+l[p3]==target:
                return [p3,p1,p2]
            elif (l[p1]+l[p2]+l[p3]<target):
                p1=p1+1
            else:
                p2=p2-1
        return False
l=list(map(int,input().split()))
target=int(input())
x=fun(l,target)
print(x)'''


        


        