# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:03:57 2019

@author: arnou
"""

#call the instance self
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls,amount):  #cls is the common convention for passing in the class as the parameter
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
   
  #static methods behave just like function the instance is not passed in as a parameter the reason that they are included is because of logical grouping  
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#print(Employee.num_of_emps)      
    
emp_1 = Employee('Corey', 'Arnouts', 50000)
emp_2 = Employee('test','user',60000)

import datetime
my_date = datetime.date(2016,7,11)

print(Employee.is_workday(my_date))


#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'
#
#first, last, pay = emp_str_1.split('-')
#
##new_emp_1 = Employee(first, last, pay)
#new_emp_1 = Employee.from_string(emp_str_1)
#
#print(new_emp_1.email)
#print(new_emp_1.pay)

#print(Employee.num_of_emps)


#print(emp_1.__dict__)
#print(Employee.__dict__)

#emp_1.raise_amount = 1.05
#

#Employee.set_raise_amt(1.05)

#emp_1.set_raise_amt(1.05)  #run the class method from an instance

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)