import numpy as np 
from matplotlib import pyplot as plt

import euler
import sirkelfrag
import rettlinje
import sykloide  

def sirkel(filnavn): 
    f = open(filnavn ,"r")
    lines = f.readlines()

    t = []
    x = []
    y = []
    s = []
    v = []

    for i in range(2, len(lines)-1):
        t.append(float(lines[i].split('\t')[0]))
    #print(t)
    for i in range(2, len(lines)-1):
        x.append(float(lines[i].split('\t')[1]))
    #print(x)
    for i in range(2, len(lines)-1):
        y.append(float(lines[i].split('\t')[2]))
    #print(y)

    for i, elem in enumerate(x): 
        s.append(np.sqrt(x[i]**2 + y[i]**2))
        #print(s)

    # v = (x1-x0)/delta(t)
    for i in range(2, len(x) - 2): 
        #v.append(np.divide((x[i + 1]-x[i-1]),(t[i + 1]-t[i-1])))
        v.append((1*x[i-2]-8*x[i-1]+0*x[i+0]+8*x[i+1]-1*x[i+2])/(12*1.0*(t[i+1]-t[i])**1))
        #print(v)
    print(sum(v)/len(v))

    return t,x,v


def skrplan(filnavn): 
        
    f = open(filnavn,"r")
    lines = f.readlines()
    t = []
    x = []
    y = []
    s = []
    v = []

    for i in range(2, len(lines)-1):
        t.append(float(lines[i].split('\t')[0]))
    #print(t)
    for i in range(2, len(lines)-1):
        x.append(float(lines[i].split('\t')[1]))
    #print(x)
    for i in range(2, len(lines)-1):
        y.append(float(lines[i].split('\t')[2]))
    #print(y)

    for i, elem in enumerate(x): 
        s.append(np.sqrt(x[i]**2 + y[i]**2))
        #print(s)


    # v = (x1-x0)/delta(t)
    for i in range(2, len(x) - 2): 
        #v.append(np.divide((x[i + 1]-x[i-1]),(t[i + 1]-t[i-1])))
        v.append((1*x[i-2]-8*x[i-1]+0*x[i+0]+8*x[i+1]-1*x[i+2])/(12*1.0*(t[i+1]-t[i])**1))
        #print(v)
    print(sum(v)/len(v))
    
    
    return t,x,v


def sykloide(filnavn): 
    f = open(filnavn ,"r")
    lines = f.readlines()
    t = []
    x = []
    y = []
    s = []
    v = []
    for i in range(2, len(lines)-1):
        t.append(float(lines[i].split('\t')[0]))
    #print(t)
    for i in range(2, len(lines)-1):
        x.append(float(lines[i].split('\t')[1]))
    #print(x)
    for i in range(2, len(lines)-1):
        y.append(float(lines[i].split('\t')[2]))
    #print(y)

    for i, elem in enumerate(x): 
        s.append(np.sqrt(elem**2 + y[i]**2))
        #print(s)

    # v = (x1-x0)/delta(t)
    for i in range(2, len(x) - 2): 
        #v.append(np.divide((x[i + 1]-x[i-1]),(t[i + 1]-t[i-1])))
        v.append((1*x[i-2]-8*x[i-1]+0*x[i+0]+8*x[i+1]-1*x[i+2])/(12*1.0*(t[i+1]-t[i])**1))
    print(sum(v)/len(v))

    return t,x,v

#sykloide("sykloide/take1.txt") 
#skrplan("skrplan/take1.txt")
#sirkel("sirkelfragment/take1.txt")


def plot_all_v():
    t, x, v = sirkel("sirkelfragment/take1.txt")
    t, x1, v1 = sykloide("sykloide/take1.txt")
    t, x2, v2 = skrplan("skrplan/take8.txt")
    plt.plot(t[:-14], v)
    plt.plot(t[:-12], v1)
    plt.plot(t[:-4], v2)
    plt.title("Hastighet v[m/s]", fontsize=20)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel("$s$ [m]", fontsize=18)
    plt.legend(['Sirkelfrag', 'Sykloide', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()

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
    plt.plot(t, ss, t, ssy, t, sr)
    plt.title("Posisjon og tid")
    plt.xlabel('tid t[s]')
    plt.ylabel('strekning s[m]')
    plt.legend(['Sirkelfragment', 'Sykloide', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()

#plot_veloc_graph(sirkelfrag)
#plot_veloc_graph(rettlinje)
#plot_veloc_graph(sykloide)
#plot_dist_graph(sirkelfrag)
#plot_dist_graph(rettlinje)
#plot_dist_graph(sykloide)
#plot_all_dist()
#plot_all_vel()

def plot_all_x():
    t, x, v = sirkel("sirkelfragment/take1.txt")
    t, x1, v1 = sykloide("sykloide/take1.txt")
    t, x2, v2 = skrplan("skrplan/take1.txt")
    t, ss = plot_dist_graph(sirkelfrag)
    #t, sr = plot_dist_graph(rettlinje)
    #t, ssy = plot_dist_graph(sykloide)
    plt.plot(t[:-5], x) #sirkelfragment
    plt.plot(t[:-3], x1) #sykloide
    plt.plot(t, x2) #skråplan
    plt.plot(t, ss)
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel("$s$ [m]", fontsize=18)
    plt.title("Posisjon x[m]", fontsize=20)
    plt.legend(['Sirkelfrag', 'Sykloide', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()

plot_all_x()
