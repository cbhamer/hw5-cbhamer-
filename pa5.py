#'HW5 Functions'

def gcd(a, b):
    """
    takes two integers and returns a algorithm that will find the
    common divisor
    """
    if b == 0:
        return a

    return gcd(b, a % b)

def remove_pairs(stri):
    """
    takes the string of a path for a maze and returns a filtered string
    that doesn't have opposite paired diretions that are adjacent
    """
    if len(stri) <= 1:
        return str

    if stri[0] == directions(stri[1]):
        return remove_pairs(stri[2:])

    return stri[0] + remove_pairs(stri[1:])

def directions(d):
    """
    Helper function that pairs the opposite directions
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
    Takes in a function and two roots and will return another
    root in between the two given
    """
    def bisection_helper(x1, x2):
        y1 = func(x1)
        y2 = func(x2)

        if abs(y1) <= 10**-7:
            return x1
        elif abs(y2) <= 10**-7:
            return x2
        elif (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0):
            raise ValueError('Roots must be opposites of each other')
        x_mid = (x1 + x2) / 2
        y_mid = func(x_mid)

        if abs(y_mid) <= 10**-7:
            return x_mid
        elif y_mid * y1 < 0:
            return bisection_helper(x1, x_mid)
        return bisection_helper(x_mid, x2)
    return bisection_helper(x1, x2)
