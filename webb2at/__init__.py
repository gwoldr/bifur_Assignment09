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
    def __init__(self, type, cook): 
        self.type = type
        self.cook = cook
        
    def purchasetype(self, type):
        self.type = type
        print(f"Purchased meat: {type}")
    
    def modifyCook(self, cook):
        self.cook = cook
        
    def __str__(self):
        return f'Steak is {self.type} and the finish on the steak is {self.cook}' 
        
    def __repr__(self):
        return f"Steak(type={self.type}, cook={self.cook})"
        
    