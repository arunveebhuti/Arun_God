class trip:
    def travel(self):
        print("I went there through flight")
class singapore(trip):
    def sing(self):
        print("I went to singapore")
class america(trip):
    def us(self):
        print("I went to america")
a=america()
a.us()
a.travel()
print("\n\n")

s=singapore()
s.sing()
s.travel()

