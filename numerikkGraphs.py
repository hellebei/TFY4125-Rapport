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
    return t, v

def plot_dist_graph(eksp):
    
    t = []
    s = []
    results = euler.get_result(eksp)[1]
    for item in results: 
        strekn = item[0]
        time = item[2]
        s.append(strekn)
        t.append(time)
    return t, s

def plot_all_vel():
    plt.gca().set_color_cycle(['red', 'green', 'blue'])
    t, vs = plot_veloc_graph(sirkelfrag)
    t, vr = plot_veloc_graph(rettlinje)
    t, vsy = plot_veloc_graph(sykloide)
    plt.plot(t, vs, t, vr, t, vsy)
    plt.xlabel(r'$tid t [s]$')
    plt.ylabel(r'$hastighet v [m/s]$')
    plt.legend(['sirkelfrag', 'rett linje', 'sykloide'], loc='upper left')
    plt.grid()
    plt.show()

def plot_all_dist():
    plt.gca().set_color_cycle(['red', 'green', 'blue'])
    t, ss = plot_dist_graph(sirkelfrag)
    t, sr = plot_dist_graph(rettlinje)
    t, ssy = plot_dist_graph(sykloide)
    plt.plot(t, ss, t, sr, t, ssy)
    plt.xlabel(r'$tid t [s]$')
    plt.ylabel(r'$strekning s [m]$')
    plt.grid()
    plt.show()

#plot_veloc_graph(sirkelfrag)
#plot_veloc_graph(rettlinje)
#plot_veloc_graph(sykloide)
#plot_dist_graph(sirkelfrag)
#plot_dist_graph(rettlinje)
#plot_dist_graph(sykloide)
plot_all_dist()
plot_all_vel()