import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

A1 = 7
#A2 = 3
#A3 = 11
czestotliwosc1 = 10
#czestotliwosc2 = 25
#czestotliwosc3 = 40
#czestProbkowania = 500
#czas = 1

#t = np.linspace(0, czas, czas * czestProbkowania)
#sygnal=np.concatenate([np.concatenate([A1*np.sin(2*np.pi*czestotliwosc1*t), A2*np.sin(2*np.pi*czestotliwosc2*t)]), A3*np.sin(2*np.pi*czestotliwosc3*t)])
#przefiltrowany = ag.dolnoprzepustowy(sygnal, czestProbkowania, 17.5)
#t = np.linspace(0, 3, 3*czas * czestProbkowania)

#plt.subplot(2, 1, 1)
#plt.plot(t, sygnal)
#plt.ylim([-12, 12])
#plt.xlabel("t[s]", size=18)
#plt.ylabel("A[-]", size=18)
#plt.subplot(2, 1, 2)
#plt.plot(t, przefiltrowany, color='g')
#plt.ylim([-12, 12])
#plt.xlabel("t[s]", size=18)
#plt.ylabel("A[-]", size=18)
#plt.show()

#tranfsormata
t1 = np.linspace (0, 1, 256*1)
f = np.linspace (0, 250, 256*1)
sygnal1 = A1*np.sin (2* np.pi*czestotliwosc1*t1)
trans = ag.FFT(sygnal1)

plt.subplot(2, 1, 1)
plt.plot(t1, sygnal1, color='g')
plt.ylim(-8, 8)
plt.xlabel("t[s]", size=18)
plt.ylabel("A[-]", size=18)
plt.subplot(2, 1, 2)
plt.stem(f, trans)
plt.xlim(0, 20)
plt.xlabel("f[Hz]", size=18)
plt.ylabel("A[-]", size=18)
plt.show()
