# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def cuadrado(x):
    return x ** 2

def raiz_cuadrada(x):
    return x ** 0.5

def operar(func, *args):
    for n in args:
        print(func(n))


def print_hi(name):
    print(f'Hi, {name}')
    operar(raiz_cuadrada, 9, 25, 64, 49)

if __name__ == '__main__':
    print_hi('PyCharm')
