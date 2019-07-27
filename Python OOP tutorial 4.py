# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:57:24 2019

@author: arnou
"""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
        
        
class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())
    


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User', 60000)

print(emp_1)
repr(emp_1)
str(emp_1)

print(int.__add__(1,2))

print(emp_1 + emp_2)



dev_1 = Developer('Corey', 'Schafer', 50000,'Python')
dev_2 = Developer('Test', 'Employee', 60000,'Java')

mgr_1 = Manager('Sue','Smith',90000, [dev_1])

print(isinstance(mgr_1,Employee))

print(issubclass(Manager,Employee))

#print(mgr_1.email)
#
#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)
#
#mgr_1.print_emps()

#
#print(dev_1.email)
#print(dev_1.prog_lang)


#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_2.email)