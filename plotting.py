import numpy as np
from numpy.linalg import norm
from matplotlib import pyplot as plt

k_kule = 2/5
k_btb = 2/3
g = 9.81

def iptrack(filename):
	data=np.loadtxt(filename,skiprows=2)
	return np.polyfit(data[:,1],data[:,2],15)

def trvalues(p,x):
	y=np.polyval(p,x)
	dp=np.polyder(p)
	dydx=np.polyval(dp,x)
	ddp=np.polyder(dp)
	d2ydx2=np.polyval(ddp,x)
	alpha=np.arctan(-dydx)
	R=(1.0+dydx**2)**1.5/d2ydx2
	return [y,dydx,d2ydx2,alpha,R]

def alpha(p, x):
	return trvalues(p, x)[-2]

def R(p, x):
	return trvalues(p, x)[-1]

def y(p, x):
	return trvalues(p, x)[0]


def f(t, y, p):
	k = k_kule
	dv = g * np.sin(alpha(p, y[0])) / (1 + k)
	vx = np.cos(alpha(p, y[0]))*y[1]
	vy = np.sin(alpha(p, y[0]))*y[1]
	return np.array([vx, dv, vy])

def euler_onestep(t_n, y_n, h, f, p):
	y_next = y_n + h * f(t_n, y_n, p)
	t_next = t_n + h
	return t_next, y_next

def num_solve_ODE(t0, t_N, h, y0, step_method , f, p):
	t_values = np.array([t0])
	v_values = np.array([y0[1]])
	x_values = np.array([y0[0]])
	y_values = np.array([y0[2]])

	t_n = t0
	y_n = y0
	while t_n + h < t_N:
		t_n, y_n = step_method(t_n, y_n, h, f, p)
		t_values = np.append(t_values, t_n)
		v_values = np.concatenate((v_values, np.array([y_n[1]])))
		x_values = np.concatenate((x_values, np.array([y_n[0]])))
		y_values = np.concatenate((y_values, np.array([y_n[2]])))
	return t_values, v_values, x_values, y_values

def arc_length(x, y): 
	npts = len(x)
	arc = np.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
	s = np.array([arc])
	for k in range(1, npts):
		s = np.concatenate((s, np.array([arc])))
		arc = arc + np.sqrt((x[k] - x[k-1])**2 + (y[k] - y[k-1])**2)
	return s

def get_results(filename, t0, tN, x0, ypos, bane, p):

	y0 = np.array([x0, ypos, bane]) 

	return num_solve_ODE(t0, tN, 0.01, y0, euler_onestep, f, p)

def friction(p, x): 
	m = 0.0304
	k = 2/5
	return m * 9.81 * np.sin(alpha(p, x)) * (k/(1 + k))

def normal_force(x, v_num, p): 
	m = 0.0304
	return m * (v_num**2 / R(p, x) + np.cos(alpha(p, x)) * 9.81)

def main(): 
	p_skr = iptrack('skrplan/take1.txt')
	t_num, v_num_skr, x_num_skr, y_num_skr = get_results('skrplan/take1.txt', 0, 0.63, 5.419243434E-2, 6.199339146E-1, 0, p_skr)
	frik_skr = friction(p_skr, x_num_skr)
	norm_skr = normal_force(x_num_skr, v_num_skr, p_skr)

	#resultater sykloide
	p_syk = iptrack('sykloide/take1.txt')
	t_num, v_num_syk, x_num_syk, y_num_syk = get_results('sykloide/take1.txt', 1.000000000E-2, 0.6, 8.801083301E-2, 3.675549462E-1, 0, p_syk)
	frik_syk = friction(p_syk, x_num_syk)
	norm_syk = normal_force(x_num_syk, v_num_syk, p_syk)

	#resultater sirkerfragment
	p_sir = iptrack('sirkelfragment/take1.txt')
	t_num, v_num_sir, x_num_sir, y_num_sir = get_results('sirkelfragment/take1.txt', 0, 0.58, 2.592867889E-2, 6.013968289E-1, 0, p_sir)
	frik_sir = friction(p_sir, x_num_sir)
	norm_sir = normal_force(x_num_sir, v_num_sir, p_sir)

	t_num = t_num[:58]
	v_num_skr = v_num_skr[:58]
	x_num_skr = x_num_skr[:58]
	y_num_skr = y_num_skr[:58]
	frik_skr = frik_skr[:58]
	norm_skr = norm_skr[:58]

	v_num_syk = v_num_syk[:58]
	x_num_syk = x_num_syk[:58]
	y_num_syk = y_num_syk[:58]
	frik_syk = frik_syk[:58]
	norm_syk = norm_syk[:58]

	v_num_sir = v_num_sir[:58]
	x_num_sir = x_num_sir[:58]
	y_num_sir = y_num_sir[:58]
	frik_sir = frik_sir[:58]
	norm_sir = norm_sir[:58]

	# Plot the linear velocity 
	plt.xlabel("$t$ [s]")
	plt.ylabel("$v$ [m/s]")
	plt.title("Banefart v[m/s] for kule")
	plt.grid()
	plt.plot(t_num, v_num_sir, t_num, v_num_syk, t_num, v_num_skr)
	plt.legend(['Sirkelfrag', 'Sykloide','Skraplan'], loc='upper left')
	plt.figure()
	plt.show()

	# plot s(t)
	plt.xlabel("$t$ [s]")
	plt.ylabel("$s$ [m]")
	plt.title("Posisjon x[m] for kule")
	plt.grid()

	plt.plot(t_num, arc_length(x_num_sir, y_num_sir), t_num, arc_length(x_num_syk, y_num_syk), t_num, arc_length(x_num_skr, y_num_skr))
	plt.legend(['Sirkelfrag','Sykloide', 'Skraplan'], loc='upper left')
	plt.show()

"""
	# plot friksjon
	plt.xlabel("$x$ [m]")
	plt.ylabel("$f$ [N]")

	plt.title("Friksjon f[N] for kulen")
	plt.ylim(top=1)  # adjust the top leaving bottom unchanged
	plt.ylim(bottom=-1)
	plt.grid()
	plt.plot(x_num_sir, frik_sir,x_num_sir, frik_syk, x_num_sir, frik_skr )
	plt.legend(['Sirkelfrag',  'Sykloide','Skraplan'], loc='upper left')
	plt.show()
"""
main()