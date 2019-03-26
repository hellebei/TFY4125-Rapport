import math

def get_gjen(filename):
    pass

g1 = get_gjen('skråplan/take1.txt')
g2 = get_gjen('skråplan/take2.txt')
g3 = get_gjen('skråplan/take3.txt')
g4 = get_gjen('skråplan/take4.txt')
g5 = get_gjen('skråplan/take5.txt')
g6 = get_gjen('skråplan/take6.txt')
g7 = get_gjen('skråplan/take7.txt')
g8 = get_gjen('skråplan/take8.txt')
g9 = get_gjen('skråplan/take9.txt')
g10 = get_gjen('skråplan/take10.txt')
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
print(STANDARRDFEILEN)
