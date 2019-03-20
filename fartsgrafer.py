import numpy as np 
from matplotlib import pyplot as plt 
import euler
import sirkelfrag
import rettlinje
import sykloide


#Fartsgraf
f = open("sirkelfragment/take1.txt" ,"r")
lines = f.readlines()
t = []
for i in range(2, len(lines)-1):
    t.append(float(lines[i].split('\t')[0]))
results_sfrag = euler.get_result(sirkelfrag)
v = []

plt.figure()
plt.plot(t,v)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$tid t [s]$')
plt.ylabel(r'$hastighet v [m/s]$')
plt.grid()
#plt.show()