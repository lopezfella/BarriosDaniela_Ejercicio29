import numpy as np
import matplotlib.pyplot as plt

fileA = np.loadtxt("datosA.dat")
gridA = np.reshape(fileA, (200, 200))

fileB = np.loadtxt("datosB.dat")
gridB = np.reshape(fileB, (200, 200))

fileC = np.loadtxt("datosC.dat")
gridC = np.reshape(fileC, (200, 200))

fileD = np.loadtxt("datosD.dat")
gridD = np.reshape(fileD, (200, 200))

plt.figure()
plt.subplot(3,3,1)
plt.imshow(gridA)
plt.title("Nx=30, Ntc")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.subplot(3,3,2)
plt.plot(fileA) //No olvidar escoger columna
plt.xlabel("Posicion")
plt.ylabel("Phi")
plt.subplot(3,3,3)
plt.plot(fileA) //No olvidar escoger columna
plt.xlabel("Tiempo")
plt.ylabel("Phi")

plt.savefig("evA.png")


plt.figure()
plt.subplot(3,3,1)
plt.imshow(gridB)
plt.title("Nx=31, Ntc")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.subplot(3,3,2)
plt.plot(fileB) //No olvidar escoger columna
plt.xlabel("Posicion")
plt.ylabel("Phi")
plt.subplot(3,3,3)
plt.plot(fileB) //No olvidar escoger columna
plt.xlabel("Tiempo")
plt.ylabel("Phi")

plt.savefig("evB.png")

plt.figure()
plt.subplot(3,3,1)
plt.imshow(gridC)
plt.title("Nx=29, Ntc")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.subplot(3,3,2)
plt.plot(fileC) //No olvidar escoger columna
plt.xlabel("Posicion")
plt.ylabel("Phi")
plt.subplot(3,3,3)
plt.plot(fileC) //No olvidar escoger columna
plt.xlabel("Tiempo")
plt.ylabel("Phi")

plt.savefig("evC.png")


plt.figure()
plt.subplot(3,3,1)
plt.imshow(gridD)
plt.title("Nx=29, Ntc-10")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.subplot(3,3,2)
plt.plot(fileD) //No olvidar escoger columna
plt.xlabel("Posicion")
plt.ylabel("Phi")
plt.subplot(3,3,3)
plt.plot(fileD) //No olvidar escoger columna
plt.xlabel("Tiempo")
plt.ylabel("Phi")

plt.savefig("evD.png")

