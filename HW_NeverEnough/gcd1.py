#---------------------------------------
# [File]: gcd1.py
#---------------------------------------

 def g1(a, b): # Calculating GCD...
    """Print GCD from 2 numbers."""
    while b != 0:
        print(' a = ', a, '\t b = ', b, end='\n')
        a, b = b, a%b
    print(' *** GCD =', a)