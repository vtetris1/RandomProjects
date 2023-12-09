import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, fsolve

testData = {"x": np.array([-8,-7,-3,0,2,9]),
            "y": np.array([9,-3,2,1,2.5,8])}

def f(x, a, b, c, d):
    y = a*x**3 + b*x**2 + c*x + d
    return y

fitParams, fitError = curve_fit(f, testData["x"], testData["y"])
xPlot = np.linspace(-10,30,num=1000)

roots = fsolve(f, [-5,-1,12], args=tuple(fitParams.tolist()))

fig, ax = plt.subplots()

ax.plot(testData["x"], testData["y"],
        marker="o",linestyle="none")

ax.plot(xPlot, f(xPlot, *fitParams))

ax.plot(roots, np.zeros(roots.shape), marker="s", linestyle="none")

ax.axvline(0, linestyle=":", color="k")
ax.axhline(0, linestyle=":", color="k")

ax.set_xlim([-10,20])
ax.set_ylim([-5,10])
ax.grid(which="both")

plt.show()