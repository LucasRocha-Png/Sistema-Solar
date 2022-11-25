"""
Created by: Lucas Rocha

At: 13:42

This file contains all the exception checkers to clean main code.
"""

def rgb_color_checker(rgb_color) -> None:
    if len(rgb_color) != 3:
        raise Exception("RGB tuple must have 3 int values")
    
    for value in rgb_color:
        if type(value) != int or value < 0 or value > 255:
            raise ValueError("The value must be a int between 0-255")
            
def pos_checker(pos) -> None:
    if len(pos) != 2:
        raise Exception("Pos tuple must have 2 int values")       

    for value in pos:
        if type(value) != int:
            raise ValueError("Pos values must be a int")        
            
def int_checker(int_, name) -> None:
    if type(int_) != int:
        raise ValueError(f"{name} must be a int")   


def str_checker(str_, name):
    if type(str_) != str:
        raise ValueError(f"{name} must be a str") 