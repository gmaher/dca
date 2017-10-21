import sys
import os
sys.path.append(os.path.abspath('../..'))
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from config import config

mpl.rcParams['legend.fontsize'] = 10


def genCurve(a,b,c,d,e,px,py,pz,N=100):
    s = np.linspace(0, 1, N)
    theta = a*2*np.pi*s

    r = b*s + c
    t = d*np.ones_like(s)
    x = px + r * np.sin(theta)
    y = py + r * np.cos(theta)
    z = pz + e*s
    return x,y,z,t

def genParams():
    a = (config.a[1]-config.a[0])*np.random.rand()+config.a[0]
    b = (config.b[1]-config.b[0])*np.random.rand()+config.b[0]
    c = (config.c[1]-config.c[0])*np.random.rand()+config.c[0]
    d = (config.d[1]-config.d[0])*np.random.rand()+config.d[0]
    e = (config.e[1]-config.e[0])*np.random.rand()+config.e[0]
    px = (config.p[1]-config.p[0])*np.random.rand()+config.p[0]
    py = (config.p[1]-config.p[0])*np.random.rand()+config.p[0]
    pz = (config.p[1]-config.p[0])*np.random.rand()+config.p[0]
    return a,b,c,d,e,px,py,pz

def genSimpleParams():
    a  = (config.a[1]-config.a[0])*np.random.rand()+config.a[0]
    b  = (config.b[1]-config.b[0])*np.random.rand()+config.b[0]
    c  = config.c[1]
    d  = config.d[1]
    e  = (config.e[1]-config.e[0])*np.random.rand()+config.e[0]
    px = (config.p[1]-config.p[0])*np.random.rand()+config.p[0]
    py = (config.p[1]-config.p[0])*np.random.rand()+config.p[0]
    pz = 0
    return a,b,c,d,e,px,py,pz

Ncurves = 100
curves = []
for i in range(Ncurves):
    a,b,c,d,e,px,py,pz = genSimpleParams()
    CURVE = genCurve(a,b,c,d,e,px,py,pz)
    curves.append(CURVE)

fig = plt.figure()
ax = fig.gca(projection='3d')
for CURVE in curves:
    ax.plot(CURVE[0], CURVE[1], CURVE[2], label='parametric curve')
#ax.legend()

plt.show()
