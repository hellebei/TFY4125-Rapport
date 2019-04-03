import iptrack
import trvalues

# trvalues(p,x) = [y,dydx,d2ydx2,alpha,R]
####################
#eval av alle takes#
####################
def main():
    takes = []

    #TAKE 1# 
    p = iptrack.iptrack("skrplan/take1.txt")
    x = 5.419243434E-2
    take1 = trvalues.trvalues(p,x)
    takes.append(take1)

    #TAKE 2# 
    p = iptrack.iptrack("skrplan/take2.txt")
    x = 2.773968890E-2
    take2 = trvalues.trvalues(p,x)
    takes.append(take2)

    #TAKE 3# 
    p = iptrack.iptrack("skrplan/take3.txt")
    x = 1.163395790E-2
    take3 = trvalues.trvalues(p,x)
    takes.append(take3)

    #TAKE 4# 
    p = iptrack.iptrack("skrplan/take4.txt")
    x = 2.828350832E-2
    take4 = trvalues.trvalues(p,x)
    takes.append(take4)

    #TAKE 5# 
    p = iptrack.iptrack("skrplan/take5.txt")
    x = 2.860749991E-2
    take5 = trvalues.trvalues(p,x)
    takes.append(take5)

    #TAKE 6# 
    p = iptrack.iptrack("skrplan/take6.txt")
    x = 2.110851047E-2
    take6 = trvalues.trvalues(p,x)
    takes.append(take6)

    #TAKE 7# 
    p = iptrack.iptrack("skrplan/take7.txt")
    x = 3.496679580E-2
    take7 = trvalues.trvalues(p,x)
    takes.append(take7)

    #TAKE 8# 
    p = iptrack.iptrack("skrplan/take8.txt")
    x = 2.511133088E-2
    take8 = trvalues.trvalues(p,x)
    takes.append(take8)

    #TAKE 9# 
    p = iptrack.iptrack("skrplan/take9.txt")
    x = 1.540866188E-2
    take9 = trvalues.trvalues(p,x)
    takes.append(take9)

    #TAKE 10# 
    p = iptrack.iptrack("skrplan/take10.txt")
    x = 2.936850342E-2
    take10 = trvalues.trvalues(p,x)
    takes.append(take10)


    return takes
