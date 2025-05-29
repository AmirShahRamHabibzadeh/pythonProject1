import re
from datetime import datetime




def laptop_validator(laptop):
    errors = []


    if not (type(laptop[1]) == int and laptop[1] > 0):
        errors.append("Laptop must be an integer > 0")

    if not (type(laptop[2]) == str and laptop[2] > 0):
