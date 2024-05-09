import math 
def gcd(a, b):
    """
    takes two integers and returns a algorithm that will find the 
    common divisor 
    """
    if b == 0:
        return a

    return gcd(b, a%b)

def remove_pairs(str):
    """
    docstring.... 
    """
    if len(str) <= 1:
        return str

    if str[0] == directions(str[1]):
        return remove_pairs(str[2:])

    return str[0] + remove_pairs(str[1:])
    
def directions(d):
    """
    docstring...
    """
    if d == 'N':
        return 'S'
    elif d == 'S':
        return 'N'
    elif d == 'E':
        return 'W'
    elif d == 'W':
        return 'E'
    else:
        return d
  
def bisection_root(func, x1, x2):
    """
    docstring....
    """
    def bisection_helper(x1, x2):
        y1 = func(x1)
        y2 = func(x2)
   
        if abs(y1) <= 10**-7:
            return x1
        elif abs(y2) <= 10**-7:
            return x2
        elif (y1 > 0 and y2>0) or (y1<0 and y2<0):
            raise ValueError('Roots must be opposites of each other')
  
        x_mid = (x1 + x2) / 2
        y_mid = func(x_mid)

        if abs(y_mid) <= 10**-7:
            return x_mid
        
        elif y_mid * y1 < 0:
            return bisection_helper(x1, x_mid)
      
        return bisection_helper(x_mid, x2)
    return bisection_helper(x1, x2)
