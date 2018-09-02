import pandas as pd
import numpy as np

def calculator(first,second):
    a = np.array([first,second])
    b = np.array([3,1])
    c = a - b
    return c

first = input('the first element[?,] is')
second = input('the second element[,?] is')

print(calculator(first, second))