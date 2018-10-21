class mom:
    def m(self):
        print("i am his mother")
class dad:
    def d(self):
        print("i am his father")
class kid(mom,dad):
    def k(self):
        print("i am their kid")
b=kid()
b.d()
b.m()
b.k()