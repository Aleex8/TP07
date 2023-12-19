from fraction import Fraction, FractionNotUnderZero

try:
    #a = Fraction(1,0) #test except ZeroDivisionError
    #b = Fraction(2,4)
    #c = Fraction(4, 4)
    #print(b-c) #test except FractionNotUnderZero
    #d = Fraction(-2, 4)
    e = Fraction('deux',3)
except ZeroDivisionError as e:
    print(e)
except FractionNotUnderZero:
    print('Pas de fraction négatif')
except TypeError:
    print('Type error')
