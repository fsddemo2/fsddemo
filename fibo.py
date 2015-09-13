def fibonacci_iter(n):
 """ Fibonacci iterativo """

 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

def fibonacci_rec(n):
 """ Fibonacci recursivo """
 if n==1 or n==2:
  return 1
 return fibonacci_rec(n-1)+fibonacci_rec(n-2)


if __name__ == "__main__":
    print (fibonacci_iter(5))
    print (fibonacci_rec(6))
