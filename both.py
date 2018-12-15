import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

dane=pd.read_csv("c:/Users/maksy/both_sexes.csv")

zmiennaWszyscy = dane["all_2534"]
zmiennaWszyscy = zmiennaWszyscy.fillna(0)
zmiennaLiceum = dane["HS_2534"]
zmiennaLiceum = zmiennaLiceum.fillna(0)
zmiennaCollege = dane["SC_2534"]
zmiennaCollege = zmiennaCollege.fillna(0)
zmiennaLicencjat = dane["BAp_2534"]
zmiennaLicencjat - zmiennaLicencjat.fillna(0)
zmiennaMagister = dane["GD_2534"]
zmiennaMagister = zmiennaMagister.fillna(0)
zmiennaBiali = dane["White_2534"]
zmiennaBiali = zmiennaBiali.fillna(0)
zmiennaCzarni = dane["Black_2534"]
zmiennaCzarni = zmiennaCzarni.fillna(0)
zmiennaBiedni = dane["poor_2534"]
zmiennaBiedni = zmiennaBiedni.fillna(0)
zmiennaSredni = dane["mid_2534"]
zmiennaSredni = zmiennaSredni.fillna(0)
zmiennaBogaci = dane["rich_2534"]
zmiennaBogaci = zmiennaBogaci.fillna(0)
zmiennaDzieci = dane["kids_all_2534"]
zmiennaDzieci = zmiennaDzieci.fillna(0)
zmiennaBrakdzieci = dane["nokids_all_2534"]
zmiennaBrakdzieci = zmiennaBrakdzieci.fillna(0)
zmiennaRok = dane["year"]
zmiennaRok = zmiennaRok.fillna(0)

#test różnic w małżeństwach miedzy białymi i czarnymi osobami (25-34 lata)
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
plt.ylabel("odsetek małżeństw")
plt.show()

#wykres wskażników opisujących jak zmieniała sie liczba małżeństw na przestrzeni lat 1960-2012

lzmiennaWszyscy=pd.Series(zmiennaWszyscy)
plt.plot(lzmiennaWszyscy, label="odsetek małżeństw")
plt.legend()
plt.xlabel("lata")
plt.ylabel("odsetek małżeństw")
plt.show()
