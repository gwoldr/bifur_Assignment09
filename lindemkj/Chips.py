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
class Cookies:
    def setPrice(self, price):
        self.validatePrice(price)
    def validatePrice(self, price):
        if price < 0:
            print ("Cookies taste good")
        else: 
            self.price = price
#this is the int
    def __init__(self, type, price):
        self.type = type
        self.validatePrice(price)
    def __repr__(self):
        """
        Return a string representing of the object 
        """ 
        return "type = " + self.type
    def __str__(self):
        """
        return a 'yummy' string representing of the object
        """
        return "type = " + self.type + "price =" + str(self.price)