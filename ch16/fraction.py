class Fraction(object):

    def __init__(self,num,den):
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __eq__(self,other):
        return ((self.num == other.num)and(self.den == other.den))

    def add(self,other):
        self.num1 = self.num * other.den
        other.num1 = other.num * self.den
        return Fraction(self.num1 + other.num1,self.den * other.den)

    def mul(self,other):
        pass

    def toFloat(self):
        pass

    def simplify(self):
        pass

    def __hash__(self):
        hashable = (self.num,self.den)
        return hash(hashable)

    def __repr__(self):
        pass

    @staticmethod
    def gcd(a,b):
        while(b!=0):
            (a,b) = (b,a%b)
        return a

    @classmethod
    def clf():
        print('hello')






f1 =Fraction(4,6)
f2 = Fraction(5,9)

print(f1)
print(f1.toString())
print(f1.add(f2).toString())

print(f1.__str__())


f1==f2

s = set()

s.add(f1)
s.add(f2)

print(s)


print(Fraction.gcd(10,5))
