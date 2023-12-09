import matplotlib.pyplot as plt
from seaborn import color_palette
import numpy as np

def start():
    fig, ax = plt.subplots(nrows=3, ncols=3)

    xline = np.array([400,400])
    yline = np.array([0,100])

    subplot = 0 

    


def testRuns():
    start()

def run():
    u = 100
    start()
    thRange = range(0, 90, 5)
    # thRange = range(65, 70, 1)
    N_th = len(thRange)
    colors = color_palette("hsv", n_colors=N_th)
    for th, color in zip(thRange, colors):
        plotTrajectory(u, th, color)
    plt.xlim(0,800)
    plt.ylim(0,300)
    plt.legend(loc="upper right", framealpha=1)
    plt.grid(which="both")
    plt.show()

def trajectory(u, th, x, g=9.81):
    y = (-g/(2*u**2*(np.cos(np.deg2rad(th)))**2) * x**2 + np.tan(np.deg2rad(th)) * x)
    return y

def plotTrajectory(u, th, color):
    xPlot = np.linspace(0, 1000, num=1000)
    yPlot = trajectory(u, th, xPlot)
    plt.plot(xPlot, yPlot, c=color, label=f"$\\theta = {th:.0f}\degree$")

#run()