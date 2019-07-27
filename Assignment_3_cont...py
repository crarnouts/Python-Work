# -*- coding: utf-8 -*-

    '''
        Create an immutable class Box that has private attributes length and width that takes values for length and width upon construction (instantiation via the constructor). 
        Make sure to use Python 3 semantics. Make sure the length and width attributes are private and accessible only via getters. 
        Immutable here means that any change to its internal state results in a new Box being returned.
        
        Remember, here immutable means there are no setter methods. States can change with the methods required below i.e. combine(), invert().
        
        In addition, create...
        - A method called render() that prints out to the screen a box made with asterisks of length and width dimensions
        - A method called invert() that switches length and width with each other
        - Methods get_area() and get_perimeter() that return appropriate geometric calculations
        - A method called double() that doubles the size of the box. Hint: Pay attention to return value here
        - Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if their respective lengths and widths are identical.
        - A method print_dim that prints to screen the length and width details of the box
        - A method get_dim that returns a tuple containing the length and width of the box
        - A method combine() that takes another box as an argument and increases the length and width by the dimensions of the box passed in
        - A method get_hypot() that finds the length of the diagonal that cuts throught the middle
        In the function exercise01():
        - Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively 
        - Print dimension info for each using print_dim()
        - Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
        - Combine box3 into box1 (i.e. box1.combine())
        - Double the size of box2
        - Combine box2 into box1
        - Using a for loop, iterate through and print the tuple received from calling box2's get_dim()
        - Find the size of the diagonal of box2
'''

class Box:

    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def render(self):
        #width = 5
        inner_size = self.width - 2
        #length = 4
        print ('*' * self.width)
        for i in range(self.length-2):
            print ('*' + ' ' * inner_size + '*')
        print ('*' * self.width)
    def invert(self):
        width_2 = self.width
        length_2 = self.length
        self.width = length_2
        self.length = width_2
    def get_area(self):
        return self.width * self.length
    def get_perimeter(self):
        return 2*self.width + 2*self.length
        
        

        
        
Box1 = Box(3,4)

print(Box1.width)
print(Box1.length)
Box1.get_area()


Box1.render()
Box1.invert()

print(Box1.width)
print(Box1.length)
Box1.render()


