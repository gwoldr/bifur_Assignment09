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
    def __init__(self, barcode):           #_init_ is automatic, we don't need to define it. Self means the current object.
        self.barcode = barcode                     #store the title in the current object       
    def __repr__(self):                    #Whatever we've stored, this will return it in a readable format
        return "Barcode = " + self.barcode
    def __str__(self):                     #Does pretty much the same thing, makes a pretty string from the object
        return "Barcode = " + self.barcode
    def getBarcode(self):
        return self.barcode
    def setBarcode(self, barC):
        self.barcode = barC
    def capitalizeBrand(self, brand):
        # Make the brand capitalized if entered incorrectly
            return brand.upper()
    def checkSoda(self, brand):
        if brand in Sodas:
            print("This product is a soda.")
        else:
            print("This movie is not a soda.")

Sodas = ["Coca-Cola", "Pepsi", "Dr. Pepper","Sprite", "Fanta", "Diet Coke", "7-Up", "Mountain Dew"] 