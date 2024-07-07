# Euclid's algo:
def gcd(a: int, b: int) -> int:
    while b>=1:
        a, b = b, a%b
    return a
    
class Fraction:
    def __init__(self, num, den) -> None:
        self.num = num
        self.den = den
        
    def __str__(self):
        return(str(self.num) + "/" + str(self.den))

    def __add__(self, other_fraction):
        new_den = self.den * other_fraction.den
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        common = gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)

    def __eq__(self, other_fraction):
        return (self.num*other_fraction.den == self.den*other_fraction.num)

    # Developed as activities:
    def __truediv__(self, other_fraction):
        new_den = self.den * other_fraction.num
        new_num = self.num * other_fraction.den
        grts_cmmon_div = gcd(new_num, new_den)
        return Fraction(new_num//grts_cmmon_div, new_den//grts_cmmon_div)

    def __sub__(self, other_fraction):
        new_den = self.den * other_fraction.den
        new_num = self.num * other_fraction.den - other_fraction.num * self.den
        common = gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)

    def __lt__(self, other_fraction):
        return (self.num*other_fraction.den < self.den*other_fraction.num)
