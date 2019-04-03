
#Eksperimentelt: s = roten av xˆ2 + yˆ2
#Så plotte s mot t
#Han sa at vi heller kunne plotte x mot t for at det skulle være enklere å se hvilken bane det var. 
# v = (x1-x0)/delta(t), men dette ble ikke så bra, så brukte http://web.media.mit.edu/~crtaylor/calculator.html for å få finere plot.

import numpy as np 
from matplotlib import pyplot as plt


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

sykloide("sykloide/take1.txt") 
skrplan("skrplan/take1.txt")
sirkel("sirkelfragment/take1.txt")

def plot_all_x():
    t, x, v = sirkel("sirkelfragment/take1.txt")
    t, x1, v1 = sykloide("sykloide/take1.txt")
    t, x2, v2 = skrplan("skrplan/take1.txt")
    plt.plot(t[:-5], x) #sirkelfragment
    plt.plot(t[:-3], x1) #sykloide
    plt.plot(t, x2) #skråplan
    plt.xlabel('$t$ [s]', fontsize=18)
    plt.ylabel("$s$ [m]", fontsize=18)
    plt.title("Posisjon x[m]", fontsize=20)
    plt.legend(['Sirkelfrag', 'Sykloide', 'Skråplan'], loc='upper left')
    plt.grid()
    plt.show()

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

plot_all_x()
plot_all_v() 

#TID MOT POSISJON
#plt.plot(t, s)
#plt.plot(t, x)
#plt.xlabel(r'$tid t [s]$')
#plt.ylabel(r'$posisjon x [m]$')
#plt.title("Sirkelfragment")
#plt.plot(t, x, t, y, x, y)
#plt.grid()
#plt.show()


"""
#TID MOR FART 
plt.plot(t[:-4], v)
plt.xlabel(r'$tid t [s]$')
plt.ylabel(r'$fart v [m/s]$')
plt.title("Sirkelfragment")
#plt.plot(t, x, t, y, x, y)
plt.grid()
plt.show()
"""