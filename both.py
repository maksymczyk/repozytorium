import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

dane=pd.read_csv("c:/Users/maksy/both_sexes.csv")

zmiennaWszyscy = 1 - dane["all_2534"]
Wszyscy = zmiennaWszyscy.mean()
zmiennaWszyscy = zmiennaWszyscy.fillna(Wszyscy)
zmiennaDyplom = 1 - dane["GD_2534"]
Dyplom = zmiennaDyplom.mean()
zmiennaDyplom = zmiennaDyplom.fillna(Dyplom)
zmiennaLiceum = 1 - dane["HS_2534"]
Liceum = zmiennaLiceum.mean()
zmiennaLiceum = zmiennaLiceum.fillna(Liceum)
zmiennaBiali = 1 - dane["White_2534"]
Biali = zmiennaBiali.mean()
zmiennaBiali = zmiennaBiali.fillna(Biali)
zmiennaCzarni = 1 - dane["Black_2534"]
Czarni = zmiennaCzarni.mean()
zmiennaCzarni = zmiennaCzarni.fillna(Czarni)
zmiennaBiedni = 1 - dane["poor_2534"]
Biedni = zmiennaBiedni.mean()
zmiennaBiedni = zmiennaBiedni.fillna(Biedni)
zmiennaSredni = 1 - dane["mid_2534"]
Sredni = zmiennaSredni.mean()
zmiennaSredni = zmiennaSredni.fillna(Sredni)
zmiennaBogaci = 1 - dane["rich_2534"]
Bogaci = zmiennaBogaci.mean()
zmiennaBogaci = zmiennaBogaci.fillna(Bogaci)
zmiennaDzieci = 1 - dane["kids_all_2534"]
Dzieci = zmiennaDzieci.mean()
zmiennaDzieci = zmiennaDzieci.fillna(Dzieci)
zmiennaBrakdzieci = 1 - dane["nokids_all_2534"]
Brakdzieci = zmiennaBrakdzieci.mean()
zmiennaBrakdzieci = zmiennaBrakdzieci.fillna(Brakdzieci)
zmiennaRok = dane["year"]

#test różnic w małżeństwach miedzy białymi i czarnymi osobami (
print(stats.shapiro(zmiennaCzarni))
print(stats.shapiro(zmiennaBiali))

print(stats.mannwhitneyu(zmiennaCzarni, zmiennaBiali))

#wykres testu

plt.figure(1)
wzmiennaCzarni = pd.Series(zmiennaCzarni).mean()
wzmiennaBiali = pd.Series(zmiennaBiali).mean()
ludzie= pd.Series([wzmiennaCzarni , wzmiennaBiali])
stdzmiennaCzarni= pd.Series(zmiennaCzarni).std()
stdzmiennaBiali= pd.Series(zmiennaBiali).std()
stdludzie = pd.Series([ stdzmiennaCzarni, stdzmiennaBiali])
plt.bar(range(len(ludzie)), ludzie, color='g', label="odsetek małżeństw" , yerr=stdludzie , width=0.5, align='center')
plt.xticks(range(len(ludzie)) , ['osoby czarnoskóre', 'osoby białoskóre'])
ax = plt.gca()
plt.ylabel("odsetek małżeństw")
plt.show()

#wykres wskażników opisujących jak zmieniała sie liczba małżeństw na przestrzeni lat 1960-2012

lzmiennaWszyscy=pd.Series(zmiennaWszyscy)
lzmiennaWszyscy=lzmiennaWszyscy*100
plt.plot(lzmiennaWszyscy)
plt.xlabel("rok")
plt.ylabel("odsetek małżeństw [%]")
y_pos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # Układa kolumny w równych odstępach
plt.xticks(y_pos, zmiennaRok, rotation = 'vertical')
plt.show()

#wykres wskażników opisujących jak zmieniała sie liczba małżeństw bezdzietnych na przestrzeni lat 1960-2012

lzmiennaBrakdzieci=pd.Series(zmiennaBrakdzieci)
lzmiennaBrakdzieci=lzmiennaBrakdzieci*100
plt.plot(lzmiennaBrakdzieci)
plt.xlabel("rok")
plt.ylabel("odsetek małżeństw bezdzietnych [%]")
y_pos2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
plt.xticks(y_pos2, zmiennaRok, rotation = 'vertical')
plt.show()
