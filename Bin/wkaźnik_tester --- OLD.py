import random
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise


#importuje SMA z pliku SMA
from Funkcje.indicators.SMA import SMA


#######################################################################################
##
##                                  zainstaluj
##          
##                            pip install perlin-noise
##
##
##                                  needed for generating random charts


##########################################################################################





#aby bylo bardziej czytelnie ja używam formatu nazywania zmiennych tak ::

###                         nazwa_zmiennej : typ_zmiennej = wartosc
###
#                          
#                                       np.   max_id : int = 40 



### do generowania cen uzuje szumu perlina wiec pobierz go sobie
###  pip install perlin-noise



# Initialize Perlin noise
noise : object = PerlinNoise(octaves=1)  # Octaves control detail level

length :int  = 1000  # długośc wykresu -- ile mam wygenerowac cen

wykres :dict ={} ## zaczynam słownik -- niepotrzebne podejście słownikowe | kiedyś zrobić listą



### parametry do wykresu losowych cen

a,b,c = 20,1,30 ### parametry do proporcji w tworzniu warotsći w perlinie
delta_x : int = 400 ### parametr który odsuwa sie od gwałtowniej czseci funkcji tj. f(x+delta_x), -- lepiej wieksze
X = random.randint(2,3) ### ten parametr mniejwiecej ustwaia krztałt całego wykresu - ustawiam funkcje pierwiastka

###potem można dodać logarytm a nie A*(1/n)




for id in range(length): ## tworze słownik o id  od 0 do lenght i przypisuje tam szumy do cen
    ### do id ceny dodaje wartośc szumu
    wykres[id]=round(abs(a*noise((id+144) / 120)  +   b*noise(id / 120)- noise(id / 10)*b + c),2)+(id+delta_x)**(1/X)


### wygładzanie perlina przy użyciu SMA

okres_SMA : int = 90

wygladzone:dict = SMA(list(wykres.values()),okres_SMA) ## wywołanie funkcji SMA


plt.plot(list(wykres.keys()),list(wykres.values())) ## wyswietlam cene mega zaszumioną 
plt.plot(list(wygladzone.keys()),list(wygladzone.values())) ## wygładzam perlinem
plt.show()