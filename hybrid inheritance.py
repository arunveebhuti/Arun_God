class delhi:
    def delh(self):
        print("I have started my journey from delhi")

class Bhopal(delhi):
    def bhp(self):
        print("I went to bhopal")

class bbsr(delhi):
    def bb(self):
        print("I went to bbsr")
class vizag(bbsr,Bhopal):
    def vz(self):
        print("I have finaly reached vizag")
v=vizag()
print("route 1")
v.delh()
v.bhp()
v.vz()

print("\n\nroute 2")
v.delh()
v.bb()
v.vz()