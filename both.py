import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

dane=pd.read_csv("c:/Users/maksy/both_sexes.csv")

zmiennaWszyscy = 1-dane["all_2534"]
zmiennaWszyscy = zmiennaWszyscy.fillna(0)
zmiennaLiceum = 1-dane["HS_2534"]
zmiennaLiceum = zmiennaLiceum.fillna(0)
zmiennaCollege = 1-dane["SC_2534"]
zmiennaCollege = zmiennaCollege.fillna(0)
zmiennaLicencjat = 1-dane["BAp_2534"]
zmiennaLicencjat - zmiennaLicencjat.fillna(0)
zmiennaMagister = 1-dane["GD_2534"]
zmiennaMagister = zmiennaMagister.fillna(0)
zmiennaBiali = 1-dane["White_2534"]
zmiennaBiali = zmiennaBiali.fillna(0)
zmiennaCzarni = 1-dane["Black_2534"]
zmiennaCzarni = zmiennaCzarni.fillna(0)
zmiennaBiedni = 1-dane["poor_2534"]
zmiennaBiedni = zmiennaBiedni.fillna(0)
zmiennaSredni = 1-dane["mid_2534"]
zmiennaSredni = zmiennaSredni.fillna(0)
zmiennaBogaci = 1-dane["rich_2534"]
zmiennaBogaci = zmiennaBogaci.fillna(0)
zmiennaDzieci = 1-dane["kids_all_2534"]
zmiennaDzieci = zmiennaDzieci.fillna(0)
zmiennaBrakdzieci = 1-dane["nokids_all_2534"]
zmiennaBrakdzieci = zmiennaBrakdzieci.fillna(0)
zmiennaRok = 1-dane["year"]
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

#test t dla wszystkich

true_mu = 0
testt1 = scipy.stats.ttest_1samp(zmiennaWszyscy, true_mu)
print(testt1)

#wykres wskażników opisujących jak zmieniała sie liczba małżeństw na przestrzeni lat 1960-2012

lzmiennaWszyscy=pd.Series(zmiennaWszyscy)
plt.plot(lzmiennaWszyscy, label="odsetek małżeństw")
plt.legend()
plt.xlabel("lata")
plt.ylabel("odsetek małżeństw")
plt.show()

#test t da bezdzietnych

testt2 = scipy.stats.ttest_1samp(zmiennaBrakdzieci, true_mu)
print(testt2)

#wykres wskażników opisujących jak zmieniała sie liczba małżeństw bezdzietnych na przestrzeni lat 1960-2012

lzmiennaBrakdzieci=pd.Series(zmiennaBrakdzieci)
plt.plot(lzmiennaBrakdzieci, label="odsetek małżeństw bezdzietnych")
plt.legend()
plt.xlabel("lata")
plt.ylabel("odsetek małżeństw bezdzietnych")
plt.show()
