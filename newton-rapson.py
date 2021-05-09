import pandas as pd



def pivote(p,func,func_derivada):
    return (p) - ( (func(p)) / (func_derivada(p)) )

def bolzano(x,y):
    return (x * y) < 0

def paro(x,y,e):
    if x != 0:
        return ( abs(x-y)/abs(x) ) < e
    else:
        return (abs(x-y) < e)



def n_r(semilla,func,func_derivada,tolerancia):
    p = pivote(semilla , func, func_derivada)
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