import numpy as np
import matplotlib.pyplot as plt

f = open("sirkelfragment/take1.txt" ,"r")
lines = f.readlines()
x = []
y = []
l =0
for i in range(2, len(lines)-1):
    x.append(float(lines[i].split('\t')[0]))
print(x)
for i in range(2, len(lines)-1):
    y.append(float(lines[i].split('\t')[2]))
print(y)
f.close()

fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)

plt.figure
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.plot(x, y)
plt.grid()
plt.show()