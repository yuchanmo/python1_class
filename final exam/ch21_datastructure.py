from queue import Queue


class Node:
    def __init__(self,contents=None,next =None):
        self.c=contents
        self.next = next
    
    def getContents(self):
        return self.c


def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()


def testline():
    n1 = Node('car')
    n2 = Node('bus')
    n3 = Node('lorry')
    n1.next = n2
    n2.next = n3
    print_list(n1)

testline()
    

class Queue:
    def __init__(self):
        self.items = []
        self.f_idx = 0
        self.r_idx = 0

    def isempty(self):
        return True

    def add(self,value):
        self.items.append(value)
        self.r_idx += 1

    def delete(self):
        if self.isempty():
            raise OverflowError
        v = self.items[0]
        self.items.remove()
        return v
    
    def size(self):
        return self.r_idx - self.f_idx


hash('yuchan')

import hashlib

hashlib.md5('value'.encode(encoding='utf-8')).digest()


## binary search tree 공부??

class PMatching:

    def __init__(self,*args):
        self.items = []
        

    def put(self,value):
        self.items.append(value)

    def pop(self):
       
        return self.items.pop()


def CheckParentheis(check_string):
    string_to_check = list(check_string)
    p = PMatching()
    for i,s in enumerate(string_to_check):
        if s == '(':
            p.put(i)
        elif s == ')':
            s,e = (p.pop(),i)
            print((s,e))

CheckParentheis('(a*(b+c)+d)')


def hanoi(n,x,y,z):
    if n>0:
        hanoi(n-1,x,z,y)
        hanoi(n-1,z,y,x)

