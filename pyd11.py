#triplet sum
'''l=list(map(int,input().split()))
target=int(input())
found=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==target:
                found=1
                break
            
if(found==0):
    print("not found")
else:
    print("found")'''


#agressive cows
'''def can_i_place_My_Cows(arr, min_dist, cows):
    last = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if abs(last - arr[i]) >= min_dist:
            count += 1
            last = arr[i]
    if count >= cows:
        return True
    else:
        return False
def solve(arr, cows):
    limit = max(arr)-min(arr)
    for i in range(1, limit+1):
        if can_i_place_My_Cows(arr, i, cows) == True:
            continue
        else:
            return i-1
arr= [0, 3, 4, 7, 9, 10]
#arr=[1,3,5,6,8]
#cows=3
cows = 4
result = solve(arr, cows)
print(result)'''




#profit
'''w=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
print(l)
maxpr=0
for weight,profit in l:
    if weight<=w:
        maxpr+=profit
        w-=weight
    else:
        maxpr+=w*(profit/weight)
        break
print(maxpr)'''



            



