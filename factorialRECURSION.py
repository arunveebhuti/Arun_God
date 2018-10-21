def factorial(n):
      if n==0:
         result=1
      else:
           result=n*factorial(n-1)
      return result

    
n=int(input("Enter any number to print its factorial-"))
x=factorial(n)
print("Factorial of the given number is-",x)
