'''
Name: Kyle Lindeman
email: lindemkj@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Group assignment, practicing git pull and push request  
Citations:
Anything else that's relevant:
'''
# we need to identify the class
class Chips:
    def setPrice(self, price):
        self.price = price
    def validatePrice(self, userPrice):
        if (self.price == userPrice):
            return ("Chips taste good")
        else: 
            return "This is the incorrect price."
#this is the int
    def __init__(self, type, price):
        self.type = type
        self.price = price
    def __repr__(self):
        """
        Return a string representing of the object 
        """ 
        return "type = " + self.type
    def __str__(self):
        """
        return a 'salty' string representing of the object
        """
        return "type = " + self.type + "price =" + str(self.price)