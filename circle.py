import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import tkinter as tk

def calcPi(e=None):
    n = int(inp.get())
    x = 1-2*np.random.random(int(n)) # [-1; 1]
    y = 1-2.*np.random.random(int(n))
    insideX,  insideY  = x[(x*x+y*y)<=1], y[(x*x+y*y)<=1]
    print(type(insideX))
    outsideX, outsideY = x[(x*x+y*y)>1], y[(x*x+y*y)>1]

    fig, ax = plt.subplots(1)
    ax.scatter(insideX, insideY, c='b',  s=.2, alpha=0.8, edgecolor=None)
    ax.scatter(outsideX, outsideY, c='r', s=.2, alpha=0.8, edgecolor=None)

    circle = Circle((.0, .0), 1, color='r', fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal')


    inside = len(insideX)
    pi_est = (inside / n) * 4.0
    diff = np.pi - pi_est
    diffLabelSv.set('Difference: ' + str(diff))
    piLabelSv.set('Estimation: ' + str(pi_est))


def show(e=None):
    plt.show()

root = tk.Tk()

inp = tk.Entry(root, text='Number of random points')
inp.grid(row=0, sticky=tk.W+tk.E)

calculateBtn = tk.Button(root, text='Estimate pi', command=calcPi)
calculateBtn.grid(row=0, column=1, sticky=tk.W)

diffLabelSv = tk.StringVar()
diffLabel = tk.Label(root, textvariable=diffLabelSv)
diffLabel.grid(row=3, sticky=tk.W+tk.E, columnspan=2)

piLabelSv = tk.StringVar()
piLabel = tk.Label(root, textvariable=piLabelSv)
piLabel.grid(row=4, sticky=tk.W+tk.E, columnspan=2)

showBtn = tk.Button(root, text='Show graph', command=show)
showBtn.grid(row=2, sticky=tk.W+tk.E, columnspan=2)


root.mainloop()
