def g3(a,b,c):
   if a>b:
    if b>c:
        print(a,"Is greatest")
    else:
        print(c,"Is greatest")
   elif b>c:
    print(b,"is greatest")
   else:
      print(c,"Is greatest")
      
print("Enter three numbers to print greatest number among them\n")
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
g3(a,b,c)


    
