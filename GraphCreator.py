import random
import matplotlib.pyplot as plt

from RandomChart import get_random_data
###############################################################
###         Funkcje importowane

from Funkcje.indicators.EMA_custom import EMA
from Funkcje.indicators.SMA import SMA
from Funkcje.indicators.guppy_ema import guppy_mode_ema
from Funkcje.indicators.Least_Square_MA import LSMA



"""Import funkcji przecinania"""

from Crossing import get_Crossing



###############################################################



def _plot(input_dict:dict,label_cus:str):

    plt.plot(list(input_dict.keys()),list(input_dict.values()),label=label_cus)



def _plot_crosses(input_dict:dict):

    plt.plot(list(input_dict.keys()),list(input_dict.values()),'o')






###############################################################
size : int = 200

random_data_data : dict = get_random_data(size) ## trzymam dwie listy 


#   random_data_data[0]     --- lista od 0 do size
#   random_data_data[1]     --- wygenerowane losowo dane


losowe_ceny = list(random_data_data.values()) ### ułatwienie | dane dla dni od 




### Testuje zachowanie LMSA

lsma = LSMA(losowe_ceny,25)
_plot(lsma,"LSMA")


## ema

ema_test : dict = EMA(losowe_ceny,52)


plt.plot(list(ema_test.keys()),list(ema_test.values()),label="EMA",color="orange") 

###

#SMA
sma = SMA(losowe_ceny,15)
_plot(sma,"SMA")




"""Pokazanie wykresu ceny /prawdziwgo/ """
plt.plot(list(random_data_data.keys()),list(random_data_data.values()),color="black",label="$$$") # drukuje szum



"""znajduje punkty przecieciecia"""

print(losowe_ceny)


_plot_crosses(get_Crossing(lsma,random_data_data))
_plot_crosses(get_Crossing(sma,random_data_data))
_plot_crosses(get_Crossing(ema_test,random_data_data))



plt.legend()
plt.show()
















# smooth : dict = SMA(random_data_data[1],21) # przyzywam wygładzanie

### test dla EMA custom


##




### generacja guppy

# lista_dla_guppy = [12,26] ### dla każdej z tej wartości powstanie pasemko
# guppy_mode_ema(random_data_data[1],lista_dla_guppy) ## wywołanie funkcji guppy ema


###



### Drukowanie SMA

#plt.plot(list(smooth.keys()),list(smooth.values()),label="SMA",color = "orange") # drukuje wygladzone

### Drukowanie ceny





