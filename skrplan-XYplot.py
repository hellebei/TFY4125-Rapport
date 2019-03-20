import numpy as np
import matplotlib.pyplot as plt

f = open("skrplan/take7.txt" ,"r")
lines = f.readlines()
x = []
y = []
for i in range(2, len(lines)-1):
    x.append(float(lines[i].split('\t')[1]))
print(x)
for i in range(2, len(lines)-1):
    y.append(float(lines[i].split('\t')[2]))
print(y)
f.close()

fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)

plt.figure
plt.xlim(0, 1.2)
plt.ylim(0, 0.7)
plt.plot(x, y)
plt.grid()
plt.show()