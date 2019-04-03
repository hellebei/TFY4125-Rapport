
#from sklearn import datasets
import math
#import scipy
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.neural_network import MLPRegressor
import numpy.polynomial.polynomial as poly
#from scipy.optimize import curve_fit
import iptrack, trvalues

def friksjon(filename, x0): 
	#Konstanter
	x_0 = x0
	result = []
	result2 = []
	#p = iptrack.iptrack("skrplan/take1.txt")
	N = 686
	#x_0 = 5.419243434E-2
	#h = 0.01
	v_0 = 0
	t_0 = 0
	#k = 0.20
	g = 9.81
	m = 3.04*10**-3
	#alpha = 2/3

	t = np.zeros(N+1)
	xA = np.zeros(N+1)
	v = np.zeros(N+1)

	t[0] = t_0
	xA[0] = x_0
	v[0] = v_0

	p = iptrack.iptrack(filename)
	

	f = open(filename ,"r")
	lines=f.readlines()
	result=[]
	result2=[]

	for x in range(2, len(lines)-2):
		result.append(float(lines[x].split('\t')[1]))
		result2.append(float(lines[x].split('\t')[2]))
	#print(result)
	f.close()

	#a = trvalues.trvalues(p, result2)[1]
	#print(a)
	theta = trvalues.trvalues(p, result)[3]
	print(theta)

	#Normalkraftgraf utifra posisjon
	n_kraft = []
	N = len(result)
	for n in range(N):
		n_kraft.append(g*m*math.cos(theta[n]))

	return result, n_kraft

	"""
	#Friksjonskraftgraf utifra posisjon
	N = len(result)
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
"""


#Normalkraft
result, n_kraft = friksjon("sirkelfragment/take1.txt", 2.592867889E-2)
result1, n_kraft1 = friksjon("sykloide/take1.txt", 8.801083301E-2)
result2, n_kraft2 = friksjon("skrplan/take5.txt", 5.419243434E-2)

plt.figure()
plt.plot(result, n_kraft) 
plt.plot(result1, n_kraft1) 
plt.plot(result2, n_kraft2)  # plotting the velocity vs. time: v(t)
plt.title("Normalkraft N[N]", fontsize=20)
plt.legend(['Sirkelfrag', 'Sykloide', 'Skråplan'], loc='upper left')
plt.xlabel('posisjon x[cm]', fontsize=18)
plt.ylabel('normalkraft N[N]', fontsize=18)
plt.grid()
plt.show()

"""
#Friksjon
result, f_liste = friksjon("sykloide/take1.txt")
plt.figure()
plt.plot(result, f_liste)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$posisjon x [cm]$')
plt.ylabel(r'$friksjonskraft f [N]$')
plt.grid()
plt.show()

"""
#def model_func(x, a, k, b):
#	return a * np.exp(-k*x) + b