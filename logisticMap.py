import matplotlib.pyplot as plt
import numpy as np

x = .3
nX = 1500 # Iterations
nA = 800

aAll = np.linspace(3.8, 3.9, nA)
plt.close("all")
fig = plt.figure()
for a in aAll:
    # f = lambda x: (a)*x*(.1+x)*(1-np.arctan(x)/np.cos(x)*np.arcsin(x))
    f = lambda x: a*x*(1-x)

    xAll = [x]
    for iX in range(1, nX):
        xAll.append(f(xAll[iX-1]))
    plt.plot(a*np.ones(nX)[100:], xAll[100:], 'r.', markersize=.05)

def onZoom(args):
    print(fig.axes[0].get_ylim(), fig.axes[0].get_xlim())

fig.axes[0].callbacks.connect("button_release_event", onZoom)
# fig.axes[0].callbacks.connect("xlim_changed", onZoom)
plt.xlabel("a")
plt.ylabel("x")
# plt.axis([min(aAll), max(aAll), 0, 3])
plt.show()
