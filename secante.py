import pandas as pd



def pivote(p,p_ant,f_p,f_p_ant):
    return (p) - ( (f_p*(p-p_ant)) / (f_p-f_p_ant))

def paro(x,y,e):
    if x != 0:
        return ( abs(x-y)/abs(x) ) < e
    else:
        return (abs(x-y) < e)



def secante(p_ant,p,func,tolerancia):
    f_p_ant = func(p_ant)
    f_p = func(p)

    df = pd.DataFrame(columns=['pn', 'f(pn)'])
    df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

    if f_p == 0:
        return df

    parar = False
    while not parar:

        p_ant_aux = p
        f_p_ant_aux = f_p

        p = pivote(p, p_ant, f_p, f_p_ant)

        p_ant = p_ant_aux
        f_p_ant = f_p_ant_aux

        f_p_ant = func(p_ant)
        f_p = func(p)

        df = df.append({'pn': p, 'f(pn)': f_p}, ignore_index=True)

        if f_p == 0:
            return df

        parar = paro(p, p_ant, tolerancia)

    return df


def f(x):
    return (x**3)+(4*(x**2))-(10)

print(secante(2,1,f,1E-4))