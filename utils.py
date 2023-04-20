import numpy as np
import matplotlib.pyplot as plt


def read_file():
    x = []
    y = []

    f = open("file.txt", "r")

    for line in f:
        xi, yi = [float(i) for i in line.split(",")]
        x.append(xi)
        y.append(yi)

    f.close()

    z = zip(x, y)
    zs = sorted(z, key=lambda tup: tup[0])
    x = [x[0] for x in zs]
    y = [x[1] for x in zs]

    return x, y


def draw_plot(x, y, f, title):
    left = min(x)
    right = max(x)

    x_linspace = np.linspace(left - 2, right + 2, 100)

    plt.title(title)

    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")

    plt.xticks(np.arange(left - 2, right + 2, 1))

    plt.plot(x_linspace, f(x_linspace), color="r")
    plt.plot(x, y, color="g")

    plt.show()
