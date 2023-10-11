'''a=input()
if(a.isupper()):   
#ord is to det ascii
    print((ord(a)-64))
else:
    print((ord(a)-96))'''


'''a=input()
b=int(input())
if(ord(a)+b>122):
    print(chr((ord(a)+b)-26))
else:
    print(chr(ord(a)+b))'''
#printing star
'''a=int(input())
for i in range(a+1):
    for j in range(i):
        print('*',end=" ")
    print()'''
#method
'''a=int(input())
for i in range(a):
    print('* '*(i+1))'''

#pyramid
'''a=int(input())
for i in range(a):
    print(" "*(a-i)+"* "*(i+1))'''

#pyramid reverse
'''a=int(input())
for i in range(a):
    print(" "*(i+1)+'* '*(a-i))'''


#pattern
'''a=int(input())
for i in range(a):
    for j in range(i):
        print(i,end=" ")
    print()'''


'''input:n
output:10
        20
        300
a=int(input())
for i in range(1,a+1):
    print((10**(i-1))*i)'''

'''a=int(input())
for i in range(1,a+1):
    print(((10**i)//9)*i)'''

#if self-non static
class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        temp=node(x)
        temp.next=self.head
        self.head=temp
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
b=cse()
b.create(20)
b.create(30)
b.add_front(60)
b.create(40)

b.display()



        
    
    
       
    
    

    
    

    
        




      

    








