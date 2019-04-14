def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

''' one = successor(zero):
    rerurn lambda f:lambda x: f(zero(f)(x))
    rerurn lambda f:lambda x: f(x)'''

def one(f):
    return lambda x: f(x)

''' two = successor(one):
    return lambda f: lambda x: f(one(f)(x))
    return lambda f: lambda x: f(f(x))'''

def two(f):
        return lambda x: f(f(x))

three = successor(two)
four = successor(three)

def church_to_int(n):
    #Convert the Church numeral n to a Python integer.
    #church_to_int(zero) --> 0
    begin = 0
    
    def func(i):
        return i + 1

    return n(func)(begin)
 
def add_church(m, n):
    #Return the Church numeral for m + n, for Church numerals m and n.
    return church_to_int(m) + church_to_int(n)

def mul_church(m, n):
    #Return the Church numeral for m * n, for Church numerals m and n.
    return church_to_int(m) * church_to_int(n)

def pow_church(m, n):
    #Return the Church numeral m ** n, for Church numerals m and n.
    return church_to_int(m) ** church_to_int(n)
