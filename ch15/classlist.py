
class HousePark:
    lastname = '박'
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,where):
        print('%s,%s 여행을 가다'%(self.fullname,where))
    def love(self,other):
        print('%s,%s 사랑에 빠졌네'%(self.fullname,other.fullname))
    def __add__(self,other):
        print('%s,%s 결혼했네'%(self.fullname,other.fullname))
    def __sub__(self,other):
        print('%s,%s 이혼했네'%(self.fullname,other.fullname))
        
    def fight(self,other):
        print('%s,%s 싸웠네'%(self.fullname,other.fullname))


class HouseKim(HousePark):
    lastname = '김'
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
    def introduceMyself(self):
        print('My name is %s, I am %s year old'%(self.fullname,self.age))
    def travel(self, where,day):
        print('%s,%s 여행 %d일 가네'%(self.fullname,where,day))


class ParkList(list):
    def __init__(self):
        self.name = "ParkList"
    def print(self):
        for i in self:
            print(i)

v = ParkList()
v.append('sdfsdf')
v.append('sdfsdfsdf')
v.print()


if __name__=='__main__':
    pey = HousePark('응용')
    pey.travel('태국')
    p2 = HousePark('셀리언')
    ki = HouseKim('라우웅쿵',0)
    pey.love(ki)
    pey.fight(ki)
    pey - p2

    pey + ki
    ki.travel('europe',30)
    ki.introduceMyself()
            


