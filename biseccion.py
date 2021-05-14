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




def pivote(a,b,pre=64):
    precision = prec(pre)
    return precision(precision(precision(a)+precision(b))/2)

#PRE: recibe una func, que debe ser continua en el intervalo de analisis.
#       Se suponen raices simples
#
#POS: retorna TRUE si existe una raiz entre x e y
def bolzano(x,y):
    return (x * y) < 0

def paro(x,y,e,pre=64):
    precision = prec(pre)
    if x != 0 :
        return precision( abs(precision(x)-precision(y))/abs(precision(x)) ) < precision(e)
    else:
        return precision(abs(precision(x)-precision(y)) < precision(e))


def biseccion(a,b,func,tolerancia,pre=64):
    precision = prec(pre)

    f_a = precision(func(precision(a)))
    f_b = precision(func(precision(b)))

    p = pivote(a, b,pre)
    f_p = precision(func(precision(p)))


    df = pd.DataFrame(columns=['an', 'bn', 'pn', 'f(pn)'])
    df = df.append({'an': a, 'bn': b, 'pn': p, 'f(pn)': f_p}, ignore_index=True)

    if f_a == 0:
        return df
    if f_b == 0:
        return df
    if f_p == 0:
        return df

    parar = False
    while not parar:
        if bolzano(f_p,f_a):
            b = p
        else:
            a = p
            f_a = f_p

        p_ant = p

        p = pivote(a, b, pre)
        f_p = precision(func(precision(p)))

        df = df.append({'an': a, 'bn': b, 'pn': p, 'f(pn)': f_p}, ignore_index=True)
        if f_p == 0:
            return df

        parar = paro(p, p_ant, tolerancia,pre)

    return df




def f(x):
    return (x**3)+(4*(x**2))-(10)


print(biseccion(np.float64(1),np.float64(2),f,1E-10))

print(biseccion(np.float64(1),np.float64(2),f,1E-10,pre=32))