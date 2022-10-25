'''
Name: Alyssa Hughes
email: hugheah@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project is about creating classes and pushing them to Github.
Citations:
Anything else that's relevant: This is my soda class.
'''
class Soda():
    #We are ensuring that a movie can't be made without a title
    def __init__(self, sodaType):           #_init_ is automatic, we don't need to define it. Self means the current object.
        self.sodaType = sodaType #store the title in the current object       
    def __repr__(self):                    #Whatever we've stored, this will return it in a readable format
        return "Soda = " + self.sodaType
    def __str__(self):                     #Does pretty much the same thing, makes a pretty string from the object
        return "Soda = " + self.sodaType
    def getSodaType(self):
        return self.sodaType
    def setSodaType(self, soda):
        self.sodaType = soda
    def capitalizeBrand(self, brand):
        # Make the brand capitalized if entered incorrectly
            return brand.upper()
    def checkSoda(self, brand):
        if brand in Sodas:
            return ("This product is a soda.")
        else:
            return ("This movie is not a soda.")

Sodas = ["Coca-Cola", "Pepsi", "Dr. Pepper","Sprite", "Fanta", "Diet Coke", "7-Up", "Mountain Dew"] 