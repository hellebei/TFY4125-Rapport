import math
import numpy as np 
from matplotlib import pyplot as plt

def get_gjen(filename):
    f = open(filename ,"r")
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
        print(v)
    
    return(sum(v)/len(v))

g1 =    get_gjen('sykloide/take1.txt')
g2 =    get_gjen('sykloide/take2.txt')
g3 =    get_gjen('sykloide/take3.txt')
g4 =    get_gjen('sykloide/take4.txt')
g5 =    get_gjen('sykloide/take5.txt')
g6 =    get_gjen('sykloide/take6.txt')
g7 =    get_gjen('sykloide/take7.txt')
g8 =    get_gjen('sykloide/take8.txt')
g9 =    get_gjen('sykloide/take9.txt')
g10 =   get_gjen('sykloide/take10.txt')
g_liste = [g1,g2,g3,g4,g5,g6,g7,g8,g9,g10]


GJENNOMSNITT = 0
STANDARDAVVIKET = 0
STANDARRDFEILEN = 0
for i in g_liste:
    GJENNOMSNITT+= i
GJENNOMSNITT= GJENNOMSNITT/len(g_liste)
print(GJENNOMSNITT)
sum_forskjell = 0
for x in g_liste:
    sum_forskjell += (x-GJENNOMSNITT)**2
STANDARDAVVIKET = math.sqrt((1/(len(g_liste)-1))*sum_forskjell)
STANDARRDFEILEN = STANDARDAVVIKET/(math.sqrt(len(g_liste)))
print(STANDARDAVVIKET)
print(STANDARRDFEILEN)
