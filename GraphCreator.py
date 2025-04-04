import random
import matplotlib.pyplot as plt

from RandomChart import get_random_data
###############################################################
###         Funkcje importowane

from EMA_custom import EMA
from SMA import SMA
from guppy_ema import guppy_mode_ema
from Least_Square_MA import LSMA

###############################################################



def _plot(input_dict:dict):

    plt.plot(list(input_dict.keys()),list(input_dict.values()))



###############################################################
size : int = 1000

random_data_data : tuple = get_random_data(size) ## trzymam dwie listy 


#   random_data_data[0]     --- lista od 1 do size
#   random_data_data[1]     --- wygenerowane losowo dane


_input = random_data_data[1] ### ułatwienie




### Testuje zachowanie LMSA


_plot(LSMA(_input,430))

ema_test : tuple = EMA(random_data_data[1],430)
plt.plot(list(ema_test.keys()),list(ema_test.values()),label="EMA",color="orange") 

###

# _plot(SMA(_input,30),colour="red")


plt.plot(random_data_data[0],random_data_data[1],color="black") # drukuje szum
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





