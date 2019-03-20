import iptrack
import trvalues

# trvalues(p,x) = [y,dydx,d2ydx2,alpha,R]
####################
#eval av alle takes#
####################
def main():
    takes = []

    #TAKE 1# 
    p = iptrack.iptrack("sykloide/take1.txt")
    x = 8.801083301E-2
    take1 = trvalues.trvalues(p,x)
    takes.append(take1)

    #TAKE 2# 
    p = iptrack.iptrack("sykloide/take2.txt")
    x = 9.966031278E-2
    take2 = trvalues.trvalues(p,x)
    takes.append(take2)

    #TAKE 3# 
    p = iptrack.iptrack("sykloide/take3.txt")
    x = 5.988160137E-2
    take3 = trvalues.trvalues(p,x)
    takes.append(take3)

    #TAKE 4# 
    p = iptrack.iptrack("sykloide/take4.txt")
    x = 9.653484260E-2
    take4 = trvalues.trvalues(p,x)
    takes.append(take4)

    #TAKE 5# 
    p = iptrack.iptrack("sykloide/take5.txt")
    x = 6.471187347E-2
    take5 = trvalues.trvalues(p,x)
    takes.append(take5)

    #TAKE 6# 
    p = iptrack.iptrack("sykloide/take6.txt")
    x = 1.090367233E-1
    take6 = trvalues.trvalues(p,x)
    takes.append(take6)

    #TAKE 7# 
    p = iptrack.iptrack("sykloide/take7.txt")
    x = 9.369350607E-2
    take7 = trvalues.trvalues(p,x)
    takes.append(take7)

    #TAKE 8# 
    p = iptrack.iptrack("sykloide/take8.txt")
    x =1.158559310E-1
    take8 = trvalues.trvalues(p,x)
    takes.append(take8)

    #TAKE 9# 
    p = iptrack.iptrack("sykloide/take9.txt")
    x = 9.056803589E-2
    take9 = trvalues.trvalues(p,x)
    takes.append(take9)

    #TAKE 10# 
    p = iptrack.iptrack("sykloide/take10.txt")
    x =6.215467059E-2
    take10 = trvalues.trvalues(p,x)
    takes.append(take10)

    return takes


'''
def print_takes(takes):
    for i in range(1, len(takes)+1): 
        print("take ", i)
        print(takes[i-1])'''



