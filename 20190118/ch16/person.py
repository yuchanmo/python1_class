class Person:

    def __init__(self):
        self.A = 'Yang Li'
        self.__B = 'Yangying Gu'

    def PrintName(self):
        print(self.A)
        print(self.__B)

    def __PrintSecreteName(self):
        print('Catwoman')


p = Person()
p.A
p.PrintName()
p.__PrintSecreteName()

