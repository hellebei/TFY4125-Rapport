
#from sklearn import datasets
import math
#import scipy
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.neural_network import MLPRegressor
import numpy.polynomial.polynomial as poly
#from scipy.optimize import curve_fit
import iptrack, trvalues


#Konstanter
result = []
result2 = []
p = iptrack.iptrack("sykloide/take1.txt")
N = 686
x_0 = 8.801083301E-2
h = 0.01
v_0 = 0
t_0 = 0
k = 0.20
g = 9.81
m = 2.8*10**-3
alpha = 2/3
#mu =

t = np.zeros(N+1)
xA = np.zeros(N+1)
v = np.zeros(N+1)

t[0] = t_0
xA[0] = x_0
v[0] = v_0

f = open("sykloide/take1.txt" ,"r")
lines=f.readlines()
result=[]
result2=[]
for x in range(lines):
	result.append(float(x.split('\t')[1]))
	result2.append(float(x.split('\t')[2]))
#print(result)
f.close()

#a = trvalues.trvalues(p, result2)[1]
#print(a)
theta = trvalues.trvalues(p, result)[3]
print(theta)

#Friksjonskraftgraf utifra posisjon
"""
mu_liste = []
f_liste = []
for n in range(N):
	a = g*math.sin(theta[n])
	b = (k*v[n])/m
	c = 1+alpha
	d = g*math.cos(theta[n])
	mu_liste.append((a-((a-b)/c-b)/d))

for n in range(N):
	f_liste.append(mu_liste[n]*m*g*math.cos(theta[n]))


plt.figure()
plt.plot(result, f_liste)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$posisjon x [cm]$')
plt.ylabel(r'$friksjonskraft f [N]$')
plt.grid()
plt.show()


#Normalkraftgraf utifra posisjon

#n_kraft = []
#for n in range(N):
#	n_kraft.append(g*m*math.cos(theta[n]))


#plt.figure()
#plt.plot(result, n_kraft)  # plotting the velocity vs. time: v(t)
#plt.xlabel(r'$posisjon x [cm]$')
#plt.ylabel(r'$Normalkraft N [N]$')
#plt.grid();
#plt.show()


def model_func(x, a, k, b):
	return a * np.exp(-k*x) + b
"""