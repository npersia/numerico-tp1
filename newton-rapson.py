import pandas as pd



def pivote(p,f,f_derivada):
    return (p) - ( f / f_derivada)

def bolzano(x,y):
    return (x * y) < 0

def paro(x,y,e):
    if x != 0:
        return ( abs(x-y)/abs(x) ) < e
    else:
        return (abs(x-y) < e)



def n_r(p,func,func_derivada,tolerancia):
    f_p = func(p)
    f_derivada_p = func_derivada(p)


    df = pd.DataFrame(columns=['pn', 'f(pn)'])
    df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

    if f_p == 0:
        return df


    parar = False
    while not parar:

        p_ant = p

        p = pivote(p, f_p, f_derivada_p)
        f_p = func(p)
        f_derivada_p = func_derivada(p)

        df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

        if f_p == 0:
            return df

        parar = paro(p, p_ant, tolerancia)

    return df


def f(x):
    return (x**3)+(4*(x**2))-(10)

def f_der(x):
    return 3*(x**2)+(8*(x))

print(n_r(10,f,f_der,1E-4))