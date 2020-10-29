"""OOP examples for module 2"""

import pandas as pd
import numpy as np

COLORS = ['cyan', 'teal', 'crimson', 'purple', 'fuscia']
FAV_NUMS = [2.71, 3.141, 7]

def increment(x):
    return x + 1

class BareMinimumClass:
  pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers.
        Complex numbers have a real part and imaginary part.
        """
        self.r = realpart 
        self.i = imagpart   
    
    def add(self, other_complex):
        self.r += other_complex.r 
        self.i += other_complex.i  
        
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)
    
class SocialMediaUser:
    def __init__(self, name, loc, upvote=0):
        self.name =str(name)
        self.loc = loc
        self.upvote = int(upvote)

    def recieve_upvote(self, num_upvote=1):
        self.upvote += num_upvote  
        
    def is_popular(self):
        return self.upvote > 100

class Animal:
    """General Representation of Animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type  
    
    def run(self):
        return "Vroom, Vroom, I go quick"  
    def eat(self, food):
        return "Huge fan of that " + str(food)


class Sloth(Animal):
    pass

if __name__ == '__main__':
    num1 = Complex(3, 5)
    num2 = Complex(4, 2)
    num1.add(num2)
    print(num1.r, num1.i)

    user1 = SocialMediaUser('Just', 'LA')
