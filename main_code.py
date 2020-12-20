# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
import random
import matplotlib.animation as ani
# %matplotlib qt
plt.ion()

Pair = namedtuple("Pair", ["first", "second"])
limit = 20
d={}
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-1,limit+1)
ax.set_ylim(-1,limit+1)
line, = ax.plot([],[])

# ax1= plt.axes(xlim=(-1, limit+1), ylim=(-1, limit+1))

x_ed = random.randint(1,limit)
y_ed = random.randint(1,limit-1)
print (x_ed,y_ed)
ys = []
for i in range(limit+1):
    if i == x_ed:
        continue
    for j in range(limit+1):
        pnt = str(i)+ str(j)
        d[pnt] = Pair(i,j)
        ax.plot([d[pnt].first], [d[pnt].second], 'ro')

for i in range(y_ed, limit+1):
    ax.plot(x_ed,i, 'bo')
    ys.append(i)        # for static dislocation
   # ani.FuncAnimation(fig,animate,frames=20,fargs=(x_ed,y_ed,limit),repeat = True)
    #plt.show(block = False);
for i in range(y_ed+1, limit+1):
     ax.plot(x_ed+1,i,'bo')        # moving next dilsocation to next line
for i in range(0,y_ed+1):
     ax.plot(x_ed,i,'ro')          # filling white space of first with red
     ax.plot(x_ed+1,i,'wo')        # replacing next white with red
     #plt.show();
for i in range(y_ed,limit+1):
     ax.plot(x_ed,i,'ro');
ani.FuncAnimation(fig,animate,frames=limit-1, fargs=(x_ed,y_ed,limit), interval = 1000, repeat = True)
