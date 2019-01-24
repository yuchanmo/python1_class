#Atom : 원자 (원자 번호, x,y,z) 정보 출력
#해당 원자의 기호(dictionary key 값 참조) 출력

#Atom class
#   - property
#       - atno : 원자 번호
#       - x,y,z : 원자의 position x,y,z 정보
#   - method
#       - symbol : 원자번호로 입력받은 정보에 대해서 원자 기호(symbol) return
#       - repr : 원자에 대한 정보 문자열로 return

class Atom(object):
    __Atno_to_Symbol = {1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O'}
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)

    def symbol(self):
        return self.__Atno_to_Symbol[self.atno]

    def __repr__(self):
        return '%d %10.4f %10.4f %10.4f' %(self.atno,self.position[0],
                self.position[1],self.position[2])


#molecure class
#   - property
#       - name : 분자 이름
#       - atomlist : 분자의 구성 원자목록
#   - method
#       - addatom : 분자의 구성 원자 목록 추가(1개씩)
#       - repr : 분자에 대한 정보 출력, 분자이름/ 분자 구성하고 있는 원자갯수/ 각원자의 정보목록(원자번호,x,y,z)


class Molecule:

    def __init__(self,name = 'Generic'):
        self.name = name
        self.atomlist = []

    def addAtom(self,atom):
        self.atomlist.append(atom)

    def __repr__(self):
        s = 'This is a molecule names %s\n' %(self.name)
        s = s + 'It has %d atoms \n'%(len(self.atomlist))
        for atom in self.atomlist:
            s = s + '%s\n '%atom
        return s

at = Atom(6,0.0,1.0,2.0)
print(at)
#6     0.0000     1.0000     2.0000
at.symbol()
#'C'



mol = Molecule('Water')
at = Atom(8,0.,0.,0.)
mol.addAtom(at)
mol.addAtom(Atom(1,0.,0.,1.))
mol.addAtom(Atom(1,0.,1.,0.))
print(mol)

#분자정보 입력(물), 어떤 원자로 이루어져있는지 정보 입력후 출력
# This is a molecule names Water
# It has 3 atoms
# 8     0.0000     0.0000     0.0000
#  1     0.0000     0.0000     1.0000
#  1     0.0000     1.0000     0.0000
