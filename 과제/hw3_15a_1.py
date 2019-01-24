
#code설명
# Animal : parent class 
#     method
#         - init : 초기화(animal 이 만들어짐을 소개)
#         - whoami : 자기 자신에 대해 소개하는 행위(Animal)
#         - eat : 먹는 행위
    
# Dog : sub class
#     method
#         - init : 초기화(animal init + dog가 만들어졌음을 소개)
#         - whoami : 자기 자신 소개(overriding : dog)
#         - bark : 강아지가 짖는 행위 (Woof)


#정답
# Animal created
# Dog created
# Dog
# Eating
# Woof

class Animal:
    
    def __init__(self):
        print('Animal created')
    
    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print('Dog created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof')

d = Dog()
d.whoAmI()
d.eat()
d.bark()