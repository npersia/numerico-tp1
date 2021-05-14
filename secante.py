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


def pivote(p,p_ant,f_p,f_p_ant,pre=64):
    precision = prec(pre)
    return precision(precision(p) - precision( precision(precision(f_p)*(precision(p)-precision(p_ant))) / precision(precision(f_p)-precision(f_p_ant))))

def paro(x,y,e,pre=64):
    precision = prec(pre)
    if x != 0 :
        return precision( abs(precision(x)-precision(y))/abs(precision(x)) ) < precision(e)
    else:
        return precision(abs(precision(x)-precision(y)) < precision(e))



def secante(p_ant,p,func,tolerancia,pre=64):
    precision = prec(pre)

    f_p_ant = precision(func(precision(p_ant)))
    f_p = precision(func(precision(p)))

    df = pd.DataFrame(columns=['pn', 'f(pn)'])
    df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

    if f_p == 0:
        return df

    parar = False
    while not parar:

        p_ant_aux = p
        f_p_ant_aux = f_p

        p = pivote(p, p_ant, f_p, f_p_ant,pre)

        p_ant = p_ant_aux
        f_p_ant = f_p_ant_aux

        f_p = precision(func(precision(p)))

        df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

        if f_p == 0:
            return df

        parar = paro(p, p_ant, tolerancia,pre)

    return df


def f(x):
    return (x**3)+(4*(x**2))-(10)

print(secante(2,1,f,1E-10,pre=32))

print(secante(2,1,f,1E-10,pre=64))