# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:04:26 2024

@author: Lenovo
"""

class A():
    def __init__(self,n):
        # self.number=n
        # print(self.number)
        print("A")

class B(A):
    def __init__(self,n):
        
        super(A,self).__init__(n)
        self.number=n
        print(self.number)
        print("B")

class D():
    
    def __init__(self,n):
        
        self.number=n
        print("D")    
        print(self.number)
        
    def say(self):
        print("D_say")
            

class C(B,D):
    
    def __init__(self,n):
        
        super().__init__(n)
        
   
class T():
    def __init__(self):
        pass
    
    def test(self):
        self.c=C()
        self.c.say()
if __name__=='__main__':
    t=C(10)
    print(t.number)
    print(type(t.number))
    