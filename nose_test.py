from fibo import fibonacci_iter, fibonacci_rec, fibo_iter_call

def test_fibo():
   """
   Resultado para los primeros 15 elementos
        1  ==  1
        2  ==  1
        3  ==  2
        4  ==  3
        5  ==  5
        6  ==  8
        7  ==  13
        8  ==  21
        9  ==  34
        10  ==  55
        11  ==  89
        12  ==  144
        13  ==  233
        14  ==  377
   """
   resultados = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
   # 0 no es usado es solo para que calse el indice

   for x in range(1,15):
       assert fibonacci_iter(x) == resultados[x]
       assert fibonacci_rec(x) == resultados[x]
       assert fibo_iter_call(x) == resultados[x]
     
