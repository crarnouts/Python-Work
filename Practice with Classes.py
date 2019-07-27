# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:30:34 2019

@author: arnou
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
        
    
emp_1 = Employee('Corey', 'Arnouts', 50000)
emp_2 = Employee('test','user',60000)

Employee.fullname(emp_1)
emp_1.fullname()

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())