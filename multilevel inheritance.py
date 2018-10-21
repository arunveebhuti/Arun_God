class companyname:
    def cn(self):
        print("new thoughts")

class hr(companyname):
    def hr1(self):
        print("HR is working under the company")
class emp(hr):
    def empl(self):
        print("Employee is working under HR ")
        print("Employee is working for the company")

e=emp()
e.cn()
e.empl()
e.hr1()


