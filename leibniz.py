import pandas as pd
import numpy as np


def leibniz(n):

    par = 1
    sum = 0
    for x in range(n+1):
        sum = sum + ((par * 1)/((2 * x) + 1))

        par = par * -1


    return sum


print(4*leibniz(100000))