"""
Name: Roman Groenewold
Email: groenern@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project has each group member create their own classes, and this main.py uses them
Anything Else: No problems setting up project
"""
# import packages to use classes
import hugheah
import lindemkj
import webb2at

# declare objects (one of each class)
mySoda = hugheah.Soda("Coca-Cola")
myChips = lindemkj.Chips("doritos", 1.75)
mySteak = webb2at.Steak("ribeye", "medium rare")

# print bare bones information "dunder" class
print("Dunder method 1: " + mySoda.__repr__())
print("Dunder method 2: " + myChips.__repr__())
print("Dunder method 3: " + mySteak.__repr__())

# non-dunder methods being used
mySoda.setSodaType("7-Up")
myChips.setPrice(1.5) 
mySteak.modifyCook("rare")

# displaying outputs
print(mySoda.checkSoda("Coca-Cola")) # check is coca cola is in the list of sodas
print(myChips.validatePrice(1.75)) #test validatePrice with original value of 1.75
print(mySteak.__str__())

