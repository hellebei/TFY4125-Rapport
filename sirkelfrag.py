import iptrack
import trvalues

# trvalues(p,x) = [y,dydx,d2ydx2,alpha,R]
####################
#eval av alle takes#
####################

takes = []

#TAKE 1# 
p = iptrack.iptrack("sirkelfragment/take1.txt")
x = 2.592867889E-2
take1 = trvalues.trvalues(p,x)
takes.append(take1)

#TAKE 2# 
p = iptrack.iptrack("sirkelfragment/take2.txt")
x = 3.849361079E-2
take2 = trvalues.trvalues(p,x)
takes.append(take2)

#TAKE 3# 
p = iptrack.iptrack("sirkelfragment/take3.txt")
x = 2.649781596E-2
take3 = trvalues.trvalues(p,x)
takes.append(take3)

#TAKE 4# 
p = iptrack.iptrack("sirkelfragment/take4.txt")
x = 2.168204072E-2
take4 = trvalues.trvalues(p,x)
takes.append(take4)

#TAKE 5# 
p = iptrack.iptrack("sirkelfragment/take5.txt")
x = 3.534133048E-2
take5 = trvalues.trvalues(p,x)
takes.append(take5)

#TAKE 6# 
p = iptrack.iptrack("sirkelfragment/take6.txt")
x = 3.433439566E-2
take6 = trvalues.trvalues(p,x)
takes.append(take6)

#TAKE 7# 
p = iptrack.iptrack("sirkelfragment/take7.txt")
x = 3.774586870E-2
take7 = trvalues.trvalues(p,x)
takes.append(take7)

#TAKE 8# 
p = iptrack.iptrack("sirkelfragment/take8.txt")
x = 2.553466091E-2
take8 = trvalues.trvalues(p,x)
takes.append(take8)

#TAKE 9# 
p = iptrack.iptrack("sirkelfragment/take9.txt")
x = 2.465906542E-2
take9 = trvalues.trvalues(p,x)
takes.append(take9)

#TAKE 10# 
p = iptrack.iptrack("sirkelfragment/take10.txt")
x = 2.606001821E-2
take10 = trvalues.trvalues(p,x)
takes.append(take10)

for i in range(1, len(takes)+1): 
    print("take ", i)
    print(takes[i-1])
