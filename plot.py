import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

x = np.linspace(0,1,100)
t = np.linspace(0,1,100)
plx, plt = np.meshgrid(x,t)

phi = np.genfromtxt('datos.txt')
fig0 = plt.figure(figsize=(15,12))

ax0 = fig0.add_subplot(111, projection='3d')
ax0.plot_surface(plx,plt,phi, color = 'darkred')
ax0.set_xlabel('$t$',size=15)
ax0.set_ylabel('$x$',size=15)
ax0.set_zlabel('$phi$',size=15)
ax0.set_title('Plot Difusion', size = 20)

plt.savefig('plot_Dif.pdf')
