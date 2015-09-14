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

a,b = 0,1
def fibo_iter():
 """ Esta funcion hace igual que un iterador """
 global a,b
 while True:
  a,b = b, a+b
  yield a

def fibo_iter_call(n):
    """ Esta funcion llama cuantas veces se necesite al iterador """
    global a,b
    a, b = 0,1
    f=fibo_iter()
    result = 1
    for x in range(n):
        result = next(f)
    return result

def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]
 
## fib() as written in example 1.
def get_memoize(n):
    return memoize(fibonacci_iter,n)

if __name__ == "__main__":
    print (fibonacci_iter(5))
    print (fibonacci_rec(6))
    print (fibo_iter_call(7))
    print (get_memoize(8))
