# 15(3-1)설명
# ShapeClass
#     - property
#         - x :  x축(사각형 기준으로 width)
#         - y :  y축(사각형 기준으로 height)
#         - description : 해당 모양을 설명하는 설명자
#         - author : 도형을 만든 사람
#     - method
#         - init : 초기화(x,y 값을 미리 받아서 해당 값 초기화)
#         - perimiter : 도형 둘레
#         - describe : 도형에 대한 설명값 설정(self.description 정보 값 변경)
#         - authorName : 도형 만든 사람에 대한 값 설정(self.authorname)
#         - scaleSize : scale(몇배)값을 입력 받아, x&y값을 scaling

#실행결과
# 4500
# 290
# 1125.0

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobdy has claimed to make this shape yet"

    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2*self.x + 2*self.y
    
    def describe(self,text):
        self.description = text

    def authorName(self,text):
        self.author = text

    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale


#test code
rectangle = Shape(100,45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe('A wide rectangle,more than twice as wide as it is tall')
rectangle.scaleSize(0.5)

print(rectangle.area())


#15(3-2)
#Square : 정사각형 만들기
#Double Square : x = 2y 인 사각형 만들기

'''Square의 경우 x,y값을 입력받지만
가로/세로 길이가 같기 때문에 x값으로 
통일해서 self.x/self.y에 초기화해준다'''
class Square(Shape):

    def __init__(self, x,y):        
        super().__init__(x,x)
        super().describe('This is square')


'''Double Square의 경우 x = 2y 이기 떄문에
가로길이에 세로 길이 2배를 해준 값으로 
self.x/self.y에 초기화해준다'''
class DoubleSquare(Shape):
    def __init__(self, x, y):
        super().__init__(y, y*2)


#15(3-3)
#Inside double Square class 만들기

'''바깥 사각형과/ 안쪽 사각형 두개로 이루어져있고
바깥쪽 사각형이 안쪽 사각형을 composite하고 있는 형태로 구현
기본적으로 둘다 Square(정사각형)이므로 둘중에 입력 받은 값중
x값을 취해서 초기화 해줬으며,
안쪽 사각형의 경우는 면적이 1/4이기 때문에, x의 1/2값으로
초기화 할 수 있도록, 클래스 생성 시 초기화 매개변수로
x/2 값을 넘겨주도록 한다'''


class InsideDoubleSquare(Square):

    def __init__(self, x, y):
        super().__init__(x, x)
        self.innersquare = Square(x/2,x/2) 
        