#1. Write a program using functions to find greatest of three numbers. 
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c