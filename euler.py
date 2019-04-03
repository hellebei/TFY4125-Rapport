
import numpy as np
import sirkelfrag

import rettlinje
import sykloide

def get_startpos(eksperiment):
    startpos = []
    if eksperiment == sirkelfrag: 
        startpos = [2.592867889E-2, 3.849361079E-2, 2.649781596E-2, 2.168204072E-2, 3.534133048E-2, 3.433439566E-2, 3.774586870E-2, 2.553466091E-2, 2.465906542E-2, 2.606001821E-2]
    elif eksperiment == rettlinje: 
        startpos = [5.419243434E-2, 2.773968890E-2, 1.163395790E-2, 2.828350832E-2, 2.860749991E-2, 2.110851047E-2, 3.496679580E-2, 2.511133088E-2, 1.540866188E-2, 2.936850342E-2]
    elif eksperiment == sykloide: 
        startpos = [8.801083301E-2, 9.966031278E-2, 5.988160137E-2, 9.653484260E-2, 6.471187347E-2, 1.090367233E-1, 9.369350607E-2, 1.158559310E-1, 9.056803589E-2, 6.215467059E-2]
    else: 
        print("Hm den finner ikke eksperiment")
        pass
    return startpos

def get_result(eksperiment): 
    takes = eksperiment.main()
    result = []
    detailed_result_take1 = []
    startpos = get_startpos(eksperiment)
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
        tt = 0
        k = 2/5
        if i==0:
            detailed_result_take1.append([s[0], v[0], tt])
        for n in range(0, nsteps-1): 
            s_rn = s[n] + v[n] * dt 
            s[n+1] = s_rn
            v_nr = v[n] + (a /(1+k))* dt
            v[n+1] = v_nr
            if i == 0:
                tt = tt + dt
                detailed_result_take1.append([s_rn, v_nr, tt])


        result.append([s[-1], v[-1]])
    return result, detailed_result_take1

def print_res(result):
    for res in result: 
        print("Strekning: ", res[0], "\t Fart: ",res[1])

def test_code(): 
    print("*******************************\n        SIRKELFRAGMENT       \n*******************************")
    res_sf = get_result(sirkelfrag)[0]
    print_res(res_sf)
    print("*******************************\n          RETTLINJE         \n******************************")
    res_rl = get_result(rettlinje)[0]
    print_res(res_rl)
    print("*******************************\n          SYKLOIDE         \n******************************")
    res_syk = get_result(sykloide)[0]
    print_res(res_syk)