import numpy as np 
from matplotlib import pyplot as plt 
import euler
import sirkelfrag
import rettlinje
import sykloide

def plot_veloc_graph(eksp):

    t = []
    v = []
    results = euler.get_result(eksp)[1]
    for item in results: 
        veloc = item[1]
        time = item[2]
        v.append(veloc)
        t.append(time)

    print(len(t))
    print(len(v))
    plt.figure()
    plt.plot(t,v)  # plotting the velocity vs. time: v(t)
    plt.xlabel(r'$tid t [s]$')
    plt.ylabel(r'$hastighet v [m/s]$')
    plt.grid()
    plt.show()

def plot_dist_graph(eksp):
    
    t = []
    s = []
    results = euler.get_result(eksp)[1]
    for item in results: 
        strekn = item[0]
        time = item[2]
        s.append(strekn)
        t.append(time)

    print(len(t))
    print(len(s))
    plt.figure()
    plt.plot(t,s)  # plotting the dist vs. time: s(t)
    plt.xlabel(r'$tid t [s]$')
    plt.ylabel(r'$strekning s [m]$')
    plt.grid()
    plt.show()




plot_veloc_graph(sirkelfrag)
#plot_veloc_graph(rettlinje)
#plot_veloc_graph(sykloide)
#plot_dist_graph(sirkelfrag)
#plot_dist_graph(rettlinje)
#plot_dist_graph(sykloide)