import pandas as pd
import numpy as np



def prec64(n):
    return np.float64(n)

def prec32(n):
    return np.float32(n)

def prec(p):
    if p == 32:
        return prec32
    if p == 64:
        return prec64

def leibniz(n,p=64):

    precision = prec(p)
    par = 1
    sum = 0
    for x in range(n+1):
        sum = precision(precision(sum) + precision(par * 1/precision(precision(2 * x) + 1)))

        par = par * -1

    return precision(sum)








print(4*leibniz(1000000,p=32))
print(4*leibniz(1000000,p=64))