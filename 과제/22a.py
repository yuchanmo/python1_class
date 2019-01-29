class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,data):
        self.top +=1
        self.stack.append(data)

    def pop(self):
        if self.top >=0 :
            self.top -= 1
            return self.stack.pop()

def match(exp):
    s = Stack()
    for i in range(len(exp)):
        if exp[i] == '(':
            s.push(i)
        elif exp[i] == ')':
            print('(' + str(s.pop())+', ' +str(i)+ ')')

match("(a*(b+c)+d)))")

def hanoi(n,x,y,z):
    hanoi(n-1,x,z,y)
    hanoi(n-1,z,y,x)

def hanoi(n):
    t1 = Stack()
    t2 = Stack()
    t3 = Stack()
    for i in range(n,0,-1):
        t1.push(i)

    def move(n,x,y,z):
        if n > 0 :
            move(n-1,x,z,y)
            y.push(x.pop())
            print(t1.stack,t2.stack,t3.stack)
            move(n-1,z,y,x)
    move(n,t1,t2,t3)


def Save():
    hanoi(10)


    for i in range(1,10):
        print(i)

Save()
    