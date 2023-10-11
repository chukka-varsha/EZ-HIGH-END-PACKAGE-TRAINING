'''n=input()
if n==n[::-1]:
    print("pal")
else:
    print("not")'''

'''s=input()
i=0
j=len(s)-1
while(i<j):
    if(s[i]!=s[j]):
        print("not pal")
        break
    i+=1
    j-=1
else:
    print("pal")'''

'''s=input()
i=0
j=len(s)-1
while(i<j):
    if(s[i]!=s[j]):
        return 'not pal'
        break'''

def fun(s,i,j):
    if(i>j):
        return True
    if(s[i]!=s[j]):
        return False
    return fun(s,i+1,j-1)
s=input()
print(fun(s,0,len(s)-1))



                  
    
    
    



    

