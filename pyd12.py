#multilevel inheritance
'''class cse:
    def fun1(self):
        print("Fun1")
    def fun2(s):
        print("Fun2")
class two(cse):
    def fun3(self):
        print("Fun3")
    def fun4(s):
        print("4")
class three(two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun5()
b.fun3()
b.fun1()'''

#multiple inheritance
'''class cse:
    def fun1(self):
        print("Fun-father")
    def fun2(self):
        print("Fun2")
class two:
    def fun1(self):
        print("Fun-mother")
    def fun3(self):
        print("Fun3")
class three(cse,two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun1()
b.fun2()
b.fun3()'''

#overiding
'''class cse:
    def fun1(self):
        print("Fun1")
    def fun1(s):
        print("Fun2")
o=cse()
o.fun1()'''


#overiding
'''class cse:
    def fun1(self):
        print("Fun1")
class two(cse):
    def fun1(self):
        print("Fun3")
class three(two):
    def fun5(self):
        print("5")
o=cse()
a=two()
b=three()
b.fun1()'''


       
    







l=list(map(int,input().split()))
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
print(*l)
    