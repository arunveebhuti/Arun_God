facto=1
def fact(f):
    for i in range(20):
        facto=f*facto
        f=f-1

f=int(input("Enter the number to print its factorial :"))
if f<0:
    print("sorry user,,!! factorial not exist")
elif f==0:
    print("factorial of 0 is 1")
else:
    fact(f)
