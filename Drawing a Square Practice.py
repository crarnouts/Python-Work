# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:32:34 2019

@author: arnou
"""

width=int(input("Width of rectangle?: "))
length = int(input("Length of rectangle?: "))


#width = 5
inner_size = width - 2
#length = 4
print ('*' * width)
for i in range(length-2):
    print ('*' + ' ' * inner_size + '*')
print ('*' * width)



#let's make it into a class

class Box:

    
    def __init__(self, width, length):
        self.width = int(input("Width of rectangle?: "))
        self.length = int(input("Length of rectangle?: "))
    def render(self):
        #width = 5
        inner_size = width - 2
        #length = 4
        print ('*' * width)
        for i in range(length-2):
            print ('*' + ' ' * inner_size + '*')
            print ('*' * width)

        
        
Box_1 = Box(5,4)

print(Box_1.width)
print(Box_1.le)