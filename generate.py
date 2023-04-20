import numpy as np


def f(x):
    return x + 5


x = np.linspace(2.2, 4, 100)

y = f(x)

f = open("file.txt", "w")

for i in range(len(x)):
    f.write(f"{x[i]}, {y[i]}\n")

f.close()
