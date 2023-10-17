#histogram
'''l=list(map(int,input().split()))
maxele=max(l)
for i in range(maxele,0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()'''


#lonest_substring_without_reapeting_characters
#leetcode:3
"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

'''def lengthOfLongestSubstring(s):
    l,longestSubString=0,0
    sw=set()
    for r in range(len(s)):
        while s[r] in sw:
            sw.remove(s[l])
            l+=1
        sw.add(s[r])
        longestSubString=max(longestSubString,(r-l+1))
    return longestSubString
s=input()
print(lengthOfLongestSubstring(s))'''



#prime algorithm
'''num=int(input())
def SieveOfEratosthenes(num):
    prime=[True]*(num+1)
    p=2
    while(p*p<=num):
        if prime[p]:
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1
    for p in range(2,num+1):
        if(prime[p]):
            print(p)
SieveOfEratosthenes(num)'''




#sliding_window_algorithm
'''l=list(map(int,input().split()))
target=int(input())
i=0
j=0
currsum=l[0]
while j<len(l)-1:
    if currsum==target:
        print(i,j,currsum)
        break
    elif currsum>target:
        currsum-=l[i]
        i+=1
    else:
        j+=1
        currsum+=l[j]'''

#inheritance
'''class cse:
    def fun1(self):
        print("fun1")
    def fun2(s):
        print("fun2")
class two:
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
    
o=cse()
a=two()
a.fun3()
a.fun4()'''


#single

'''class cse:
    def fun1(self):
        print("fun1")
    def fun2(s):
        print("fun2")
class two(cse):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
    
o=cse()
a=two()
a.fun3()
a.fun4()
a.fun1()'''



#multiple
'''class cse:
    def fun1(self):
        print("fun1")
    def fun2(s):
        print("fun2")
class two(cse):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class three(two):
    def fun5(self):
        print("fun5")
    
    
o=cse()
a=two()
b=three()
a.fun3()
b.fun5()'''



#overiding
'''class cse:
    def fun1(self):
        print("fun1")
class two(cse):
    def fun1(self):
        print("fun1")
class three(two):
    def fun5(self):
        print("fun5")
    
    
o=cse()
o.fun1()
a=two()
a.fun1()'''


'''class cse:
    def fun1(self):
        print("fun1-father")
class two(cse):
    def fun1(self):
        print("fun2-mother")
class three(two,cse):
    def fun5(self):
        print("fun5")
        
o=cse()
a=two()
a.fun1()
b=three()'''
         
         
         
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


'''import math
def Main():
    num=-85
    num=math.fabs(num)
    print(num)
if __name__=="__main__":
    Main()'''  


#aggressive cows
def can_i_place(arr,min_dist,cows):
    last=arr[0]
    count=1
    for i in range(1,len(arr)):
        if abs(last-arr[i])>=min_dist:
            count+=1
            last=arr[i]
    if count>=cows:
        return True
    else:
        return False
def solve(arr,cows):
    limit=max(arr)-min(arr)
    for i in range(1,limit+1):
        if can_i_place(arr,i,cows)==True:
            continue
        else:
            return i-1
arr=[0,3,4,7,9,10]
cows=4
x=solve(arr,cows)
print(x)






