#counting sort
'''l=[2,4,8,3,8,1,2,4,7,4]
count=[0 for i in range(10)]
for i in range(len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(l)
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(res)'''


'''l=[2,4,8,3,1,2,4,7,4]
count=[0 for i in range(10)]
for i in range(len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(l)
for i in range (len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(res)'''

#python functions
#pattern
''''for i in range(5):
    print("* "*(i))'''

'''a=range(1,10,2)
print(a,type(a))
a=range(1,10,2)
print(list(a),type(a))'''

#map
'''l=[[1,3,2],[8,6,7],[9,0,0]]
l=list(map(lambda a:sorted(a),l))
print(l)'''

#filter
'''l=[[1,3,2],[8,6,7],[9,0,0]]
a=[2,3,4,5,6]
l=list(filter(lambda a:a%2==0,a))
print(l)'''


'''l=[[1,3,2],[8,6,7],[9,0,0]]
l.sort(key=lambda x:x[0]+x[1])
print(l)'''




#finding sum of elements using divide and conquer
'''def divide(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    mid=len(l)//2
    ls=divide(l[:mid])
    rs=divide(l[mid:])
    return ls+rs
l=list(map(int,input().split()))
z=divide(l)
print(z)'''


#max element using divide and conquer
def maxim(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    mid=len(l)//2
    lm=maxim(l[:mid])
    rm=maxim(l[mid:])
    return max(lm,rm)   
l=list(map(int,input().split()))
z=maxim(l)
print(z)











    