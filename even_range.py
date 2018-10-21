print("input range to print even numbers form n-m")
a=int(input("set starting : "))
b=int(input("set ending : "))
for i in range(a,b+1):
    if (i%2==0):
        print(i)
