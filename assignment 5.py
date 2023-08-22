#!/usr/bin/env python
# coding: utf-8

# In[1]:


### challenge 1: Square Numbers and Return Their Sum


class point:
    sqsum_=0
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def sqsum(self):
        sqsum_=(self.x*self.x)+(self.y*self.y)+(self.z*self.z)
        return sqsum_
obj1=point(1,3,5)
val=obj1.sqsum()
print(val)


# In[5]:


### challege 2: Implement a calculator calss

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add (self):
        print(self.num1+self.num2)
    def subtract(self):
        if self.num1>self.num2:
            print(self.num1-self.num2)
        else:
            print(self.num2-self.num1)
    def multiply (self):
        print(self.num1*self.num2)
    def divide (self):
        if self.num1>self.num2:
            print(self.num1/self.num2)
        else:
            print(self.num1/self.num1)
            


obj=calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()


# In[6]:


### challege:3 Implement the complete student class
class Student:
    __name="sree"
    __rollNumber="843"
    def setName(self):
        __name="sreeja"
        print(__name)
    def getName(self):
        print(Student.__name)
    def setRollNumber(self):
        __rollNumber="2049200325"
        print(__rollNumber)
    def getRollNumber(self):
        print(Student.__rollNumber)
         
st=Student()
st.setName()
st.getName()
st.setRollNumber()
st.getRollNumber()


# In[7]:


### challege:4 Implement a Banking Account
class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
class SavingsAccount(Account):
    def __init__(self,title,balance,interestRate):
        self.interestRate=interestRate
        super().__init__(title,balance)
    def details(self):
        print(self.title,self.balance,self.interestRate)
sv=SavingsAccount("Ashish",5000,5)
sv.details()


# In[6]:


### challenge:5 Handling a Bank Account

class Account:
    def __init__(self):
        self.balance =2000
    def deposit(self,d):
        self.balance+=d
        print(self.balance)
    def withDraw(self,wd):
        if self.balance>wd:
            self.balance-=wd
            print(self.balance)
            
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
    def interestRate(self,i):
        self.i=i
        self.interest=self.i*self.balance/100
        print(self.interest)
        
a=Account()
a.deposit(500)
a.withDraw(500)
s=SavingsAccount()
s.interestRate(5)

