import numpy as np


def linear_function(x, y, return_res=False):
    n = len(x)

    sx = 0
    sxx = 0
    sy = 0
    sxy = 0

    for i in range(n):
        sx += x[i]
        sxx += x[i] ** 2
        sy += y[i]
        sxy += x[i] * y[i]

    matrix = np.array([
        [sxx, sx],
        [sx, n]
    ])

    answ = np.array([sxy, sy])

    res = np.linalg.solve(matrix, answ)

    f = lambda x: res[0] * x + res[1]

    if return_res:
        return res

    return f


def polinom2_function(x, y, return_res=False):
    n = len(x)

    sx = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sy = 0
    sxy = 0
    sx2y = 0

    for i in range(n):
        sx += x[i]
        sx2 += x[i] ** 2
        sx3 += x[i] ** 3
        sx4 += x[i] ** 4
        sy += y[i]
        sxy += x[i] * y[i]
        sx2y += y[i] * x[i] ** 2

    matrix = np.array([
        [n, sx, sx2],
        [sx, sx2, sx3],
        [sx2, sx3, sx4]
    ])

    answ = np.array([sy, sxy, sx2y])

    res = np.linalg.solve(matrix, answ)

    f = lambda x: res[2] * x ** 2 + res[1] * x + res[0]

    if return_res:
        return res

    return f


def polinom3_function(x, y, return_res=False):
    n = len(x)

    sx = 0
    sx2 = 0
    sx3 = 0
    sx4 = 0
    sx5 = 0
    sx6 = 0
    sy = 0
    sxy = 0
    sx2y = 0
    sx3y = 0

    for i in range(n):
        sx += x[i]
        sx2 += x[i] ** 2
        sx3 += x[i] ** 3
        sx4 += x[i] ** 4
        sx5 += x[i] ** 5
        sx6 += x[i] ** 6
        sy += y[i]
        sxy += x[i] * y[i]
        sx2y += y[i] * x[i] ** 2
        sx3y += y[i] * x[i] ** 3

    matrix = np.array([
        [n, sx, sx2, sx3],
        [sx, sx2, sx3, sx4],
        [sx2, sx3, sx4, sx5],
        [sx3, sx4, sx5, sx6]
    ])

    answ = np.array([sy, sxy, sx2y, sx3y])

    res = np.linalg.solve(matrix, answ)

    f = lambda x: res[3] * x ** 3 + res[2] * x ** 2 + res[1] * x + res[0]

    if return_res:
        return res

    return f


def exp_function(x, y, return_res=False):
    for i in y:
        if i <= 0:
            return None

    ln_y = np.log(y)

    ret_res = linear_function(x, ln_y, return_res=True)

    res = [np.exp(ret_res[1]), ret_res[0]]

    f = lambda x: res[1] * np.exp(res[0] * x)

    if return_res:
        return res

    return f


def power_function(x, y):
    for i in x:
        if i <= 0:
            return None

    for i in y:
        if i <= 0:
            return None

    Y = np.log(y)
    X = np.log(x)

    coefs = linear_function(X, Y, return_res=True)

    A = coefs[1]
    B = coefs[0]

    a = np.exp(A)
    b = B

    f = lambda x: a*(x**b)

    return f


def log_function(x, y, return_res=False):
    for i in x:
        if i <= 0:
            return None

    ln_x = np.log(x)

    ret_res = linear_function(ln_x, y, return_res=True)

    res = ret_res

    f = lambda x: res[0] * np.log(x) + res[1]

    if return_res:
        return res

    return f


def comp_e(x, y, f):
    sum = 0

    for i in range(len(x)):
        sum += (y[i] - f(x[i])) ** 2

    return sum


def SKO(x, y, f):
    return np.sqrt(comp_e(x, y, f) / len(x))


def pirson(x, y):
    x_m = np.mean(x)
    y_m = np.mean(y)

    num = 0

    denx = 0
    deny = 0

    for i in range(len(x)):
        num += (x[i] - x_m) * (y[i] - y_m)
        denx += (x[i] - x_m) ** 2

        deny += (y[i] - y_m) ** 2

    return num / np.sqrt(denx * deny)
