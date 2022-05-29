import numpy as np
def sort(x,y):
    for i in range (len(x)):
        for j in range(0 , len(x) - i -1):
            if(x[j] > x[j+1]):
                x[j], x[j+1] = x[j+1], x[j]
                y[j], y[j+1] = y[j+1], y[j]

n = len(a)
div = np.zeros(n)

def divided_Difference(x,y,div):
    product = 1
    suma = 0
    for k in range (0, n):
        for j in range(0, k+1):
            for i in range (0, k+1):
                if(i != j):
                    product *= (x[j] - x[i])
            suma += (y[j] / product)
            product = 1
        div[k] = suma
        suma = 0


sort(a,b)
divided_Difference(a,b,div)


for i in range (0,n):
    print('x -', a[i])

