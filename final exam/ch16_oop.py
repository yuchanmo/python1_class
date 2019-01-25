class AParent:
    def A(self):
        print('iamparent')

class A(AParent):
    def A(self):
        print('I am A')


class B:
    def A(self):
        print('IamBinA')
    
    def B(self):
        print('IamBinB')

class C(B,A):
    def C(self):
        print('IamCinC')


c = C()
c.A()
c.B()
c.C()