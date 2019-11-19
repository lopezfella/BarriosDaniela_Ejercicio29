ev_A.png ev_B.png ev_C.png ev_D.png: datosA.dat datosB.dat datosC.dat datosD.dat plot.py
	python plot.py

%.dat : a.out
	./a.out 

a.out: clase29.cpp
	c++ clase29.cpp
