class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : -
        POST : -
        """
        if den != 0:
            self.__num = num
            self.__den = den
        else:
            raise ZeroDivisionError("Division par 0 impossible")

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : renvoie une chaîne de caractères expliquant la fraction
        """
        return f"Cette fraction divise {self.__num} par {self.__den}"

    def as_mixed_number(self, number):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : self.__num < self.__den et number est un nombre non flottant
        POST : renvoie la fraction propre + number
        """
        if self.__num < self.__den and isinstance(number, int):
            return number + (self.__num/self.__den)

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une variable de type Fraction
         POST : renvoie l'addition de deux fractions
         """
        return ((self.__num/self.__den) + (other.__num/other.__den))

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la soustraction de deux fractions
        """
        return ((self.__num / self.__den) - (other.__num / other.__den))

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la multiplication de deux fractions
        """
        return ((self.__num / self.__den) * (other.__num / other.__den))

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la division de deux fractions
        """
        return ((self.__num / self.__den) / (other.__num / other.__den))

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la première frction exposant la deuxième fraction
        """
        return ((self.__num / self.__den) ** (other.__num / other.__den))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie true si la première fraction est égale à la deuxième fraction

        """
        return (self.__num/self.__den) == (other.__num/other.__den)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        return float(self.__num/self.__den)

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : ?
        POST : ?
        """
        pass


if __name__ == "__main__":
    a = Fraction(3,1)
    b = Fraction (8, 2)
    print(a.__float__())