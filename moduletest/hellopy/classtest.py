class Book(object):
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def displayBookInfo(self):
        print('book : %s, author : %s, year : %s'%(self.title,self.author,self.year))