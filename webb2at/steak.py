'''
Name: Adam Webb
email: webb2at@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: group assignment practicing git pull and push requests.
Citations:

''' 
class Steak: 
    def __init__(self, type, ISBN="1234", quantity=0 ): 
        self.type = type
        self.quantity = quantity
        self.ISBN = ISBN
        
    def purchasetype(self, type):
        self.type = type
        print(f"Purchased meat: {type}")
    
    def modifyTuning(self, tuning):
        print(f"Modified tuning from {self.tuning} to {tuning}")
        self.tuning = tuning
        
    def __str__(self):
        return f' barcode is {ISBN} and number of steaks purchased is {quantity}' 
        
    def __repr__(self):
        rep = f"Steak(type={self.type}, quantity={self.quantity}, ISBN={self.ISBN})"
        return rep
    