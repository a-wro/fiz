#!/usr/bin/env python
import tkinter as tk
import matplotlib.pyplot as plt
from random import random
from math import hypot
from numpy import pi

def calcPi(e=None):
    events = int(inp.get())
    out_xs = []
    out_ys = []
    in_xs = []
    in_ys = []
    inside = 0
    for i in range(0, events):
        x = random() # [0..1]
        y = random()
        dist = hypot(x,y)
        if dist < 1: 
            inside += 1
            in_xs.append(x)
            in_ys.append(y)
        else:
            out_xs.append(x)
            out_ys.append(y)
    plt.scatter(out_xs, out_ys, s=.2)
    plt.scatter(in_xs, in_ys, s=.2, color='red')

    pi_est = (inside / events) * 4.0
    diff = pi - pi_est
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




