
import numpy as np
import sirkelfrag

takes = sirkelfrag.main()
result = []
startpos = [2.592867889E-2, 3.849361079E-2, 2.649781596E-2, 2.168204072E-2, 3.534133048E-2, 3.433439566E-2, 3.774586870E-2, 2.553466091E-2, 2.465906542E-2, 2.606001821E-2]
for i in range (0,9):
    s0=startpos[i]
    v0=0 
    nsteps = 1000
    v = np.zeros(nsteps)
    s = np.zeros(nsteps)
    v[0] = v0
    s[0] = s0
    g = 9.81 
    dt = 0.00058
    #akselerasjon langs planet 
    alpha = takes[i][3] #hentes som 5. verdien fra sykloide
    a = g * np.sin(alpha)
    

    for n in range(0, nsteps-1): 
        s[n+1] = s[n] + v[n] * dt 
        v[n+1] = v[n] + a * dt 

    result.append([s[-1], v[-1]])

for res in result: 
    print("Strekning: ", res[0], "\t Fart: ",res[1])