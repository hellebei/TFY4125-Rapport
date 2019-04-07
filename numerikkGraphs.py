import numpy as np 
from matplotlib import pyplot as plt 
import euler
import sirkelfrag
import rettlinje
import sykloide

import eksgrafer

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
    t, vs = plot_veloc_graph(sirkelfrag)
    t, vr = plot_veloc_graph(rettlinje)
    t, vsy = plot_veloc_graph(sykloide)
    plt.plot(t, vs, t, vsy, t, vr)
    plt.title("Hastighet og tid")
    plt.xlabel('tid t[s]')
    plt.ylabel('hastighet v[m/s]')
    plt.legend(['Sirkelfragment', 'Sykloide', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()


def plot_all_dist():
    t, ss = plot_dist_graph(sirkelfrag)
    t, sr = plot_dist_graph(rettlinje)
    t, ssy = plot_dist_graph(sykloide)
    #t, x, v = eksgrafer.sirkel("sirkelfragment/take1.txt")
    t, x1, v1 = eksgrafer.sykloide("sykloide/take1.txt")
    #t, x2, v2 = eksgrafer.skrplan("skrplan/take1.txt")
    plt.plot(t, ss, t, sr, t, ssy)
    #plt.plot(t[:-5], x) #sirkelfragment
    plt.plot(t, x1) #sykloide
    #plt.plot(t, x2) #skråplan
    plt.title("Posisjon og tid")
    plt.xlabel('tid t[s]')
    plt.ylabel('strekning s[m]')
    plt.legend(['Sirkelfragment', 'Sykloide', 'Skråplan', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()



#plot_veloc_graph(sirkelfrag)
#plot_veloc_graph(rettlinje)
#plot_veloc_graph(sykloide)
#plot_dist_graph(sirkelfrag)
#plot_dist_graph(rettlinje)
#plot_dist_graph(sykloide)
plot_all_dist()
#plot_all_vel()