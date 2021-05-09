import pandas as pd

def pivote(a,b):
    return (a+b)/2

#PRE: recibe una func, que debe ser continua en el intervalo de analisis.
#       Se suponen raices simples
#
#POS: retorna TRUE si existe una raiz entre x e y
def bolzano(x,y):
    return (x * y) < 0

def paro(x,y,e):
    return (abs(x-y) < e)


def biseccion(a,b,func,tolerancia):
    f_a = func(a)
    f_b = func(b)

    p = pivote(a, b)
    f_p = func(p)


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

        p = pivote(a, b)
        f_p = func(p)

        df = df.append({'an': a, 'bn': b, 'pn': p, 'f(pn)': f_p}, ignore_index=True)
        if f_p == 0:
            return df

        parar = paro(p, p_ant, tolerancia)

    return df




def f(x):
    return (x**3)+(4*(x**2))-(10)


print(biseccion(1,2,f,1E-4))