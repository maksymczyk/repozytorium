import aseegg as ag
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("c:/Users/maksy/repozytorium/hci/sub-01_trial-07.csv", names = ['nr', 'data1', 'data2', 'data3', 'data4', 'z'])
#print(dane)
datax = data['data1']
czestProbkowania = 200
czas = len(datax)/czestProbkowania #37.97s
t = np.linspace(0, czas, czas*czestProbkowania)

#filtracje
filtr1 = ag.pasmowozaporowy(datax, czestProbkowania, 49,51)
filtr2 = ag.pasmowoprzepustowy(filtr1, czestProbkowania, 1, 50)

#przed
plt.plot(t, datax, color = 'g')
plt.xlabel("t[s]", size = 14)
plt.ylabel("A[mV]", size = 14)
# plt.show()
#po
plt.plot(t, filtr2, color = 'r')
plt.xlabel("t[s]", size = 14)
plt.ylabel("A[mV]", size = 14)
# plt.show()

#mrugnięcia
sygnal = data['data1']
cyfra = data['z']
i2=0
for i in range(len(sygnal)):
    if sygnal[i]>=0.05 and i2<0.05:
        # i2=i wyświetla tylko jedną cyfrę i nie wiem dlaczego
        print(cyfra[i]) #kod pokazuje sie dobry tylko cyfry są wyświetlone wielokrotnie, a warunek wyżej tego nie naprawia
