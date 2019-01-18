class Hello:
    var1 = 10
    _var2 = 20

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_var1(self):
        print(self.var1)

    def _print_var1(self):
        print(self.var1)

    def print_var2(self):
        print(self._var2)

    def _print_var2(self):
        print(self._var2)

apple = 'real_apple'
_apple = 'under_apple'

def print_apple():
    print('apple from another file!')

def _print_under_apple():
    print('underbar apple from another file')


# class Nihao(Hello):
#     def __init__