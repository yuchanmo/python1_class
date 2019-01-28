class Student:
    __name = ''
    __age = ''
    def __init__(self,name,age):
        self.__name = name
        self.__age =age
    
    def printMySelf(self):
        print(self.__name,self.__age)

    
class SnuStudent(Student):
    schoolname = "SNU"
    def __init__(self, name, age):
        super().__init__(name, age)

    def printMySelf(self):
        super().printMySelf() 
        print(self.schoolname)
        print(super().__name)


s = SnuStudent('유찬',35)
s.printMySelf()