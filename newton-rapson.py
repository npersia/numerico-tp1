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


def pivote(p,f,f_derivada,pre=64):
    precision = prec(pre)
    return precision(p) - ( precision(f)/ precision(f_derivada))

def paro(x,y,e,pre=64):
    precision = prec(pre)
    if x != 0 :
        return ( abs(precision(x)-precision(y))/abs(precision(x)) ) < precision(e)
    else:
        return (abs(precision(x)-precision(y)) < precision(e))



def n_r(p,func,func_derivada,tolerancia,pre=64):
    precision = prec(pre)

    f_p = precision(func(p))
    f_derivada_p = precision(func_derivada(p))


    df = pd.DataFrame(columns=['pn', 'f(pn)'])
    df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

    if f_p == 0:
        return df


    parar = False
    while not parar:

        p_ant = p

        p = precision(pivote(p, f_p, f_derivada_p,pre))
        f_p = precision(func(p))
        f_derivada_p = precision(func_derivada(p))

        df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

        if f_p == 0:
            return df

        parar = precision(paro(p, p_ant, tolerancia,pre))

    return df


def f(x):
    return (x**3)+(4*(x**2))-(10)

def f_der(x):
    return 3*(x**2)+(8*(x))


def seno(x):
    return np.sin(x)

def coseno(x):
    return np.cos(x)

#print(n_r(2,f,f_der,1E-4))

print(n_r(2,seno,coseno,1E-10))
print(n_r(2,seno,coseno,1E-10,32))