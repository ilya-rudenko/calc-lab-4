import numpy as np
from utils import read_file, draw_plot
from methods import linear_function, polinom2_function, polinom3_function, exp_function, power_function, log_function, \
    SKO, pirson

x, y = read_file()

linear_f = linear_function(x, y)
polinom2_f = polinom2_function(x, y)
polinom3_f = polinom3_function(x, y)
exp_f = exp_function(x, y)
power_f = power_function(x, y)
log_f = log_function(x, y)


print("Linear:")
print(f"    SKO: {SKO(x, y, linear_f)}")
print(f"    Pirson: {pirson(y, linear_f(np.array(x)))}")
draw_plot(x, y, linear_f, "Linear function")

print("Polinom2:")
print(f"    SKO: {SKO(x, y, polinom2_f)}")
draw_plot(x, y, polinom2_f, "Polinom2 function")

print("Polinom3:")
print(f"    SKO: {SKO(x, y, polinom3_f)}")
draw_plot(x, y, polinom3_f, "Polinom3 function")


print(linear_function(x, y, return_res=True))
print(polinom2_function(x, y, return_res=True))
print(polinom3_function(x, y, return_res=True))



# if exp_f != None:
#     print("Exp:")
#     print(f"    SKO: {SKO(x, y, exp_f)}")
#     draw_plot(x, y, exp_f, "Exp function")
#
# if power_f != None:
#     print("Power:")
#     print(f"    SKO: {SKO(x, y, power_f)}")
#     draw_plot(x, y, power_f, "Power function")
#
# if log_f != None:
#     print("Log:")
#     print(f"    SKO: {SKO(x, y, log_f)}")
#     draw_plot(x, y, log_f, "Log function")
