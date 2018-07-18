import matplotlib.pyplot as plt
import numpy as np
with open('tokenAnalyze') as f:
    contents = f.read()
contents = contents.split(',')

intlist = []
for var in contents:
    if(var.isdigit()):
        intlist.append(int(var))

bins = range(20, 100, 3)

plt.hist(intlist, bins, histtype='bar', rwidth=0.8)

plt.xlabel('Lenth of function')
plt.ylabel('Count')
plt.title('Histogram of function length')
plt.legend()
plt.show()
