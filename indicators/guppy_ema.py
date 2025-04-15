import matplotlib.pyplot as plt
from Funkcje.indicators.EMA_custom  import EMA


### Funkcja Guppy EMA generuje średnią ważoną kroczacą dla każdej wartości z listy

def guppy_mode_ema(price_arr:list ,arr_of_peroid:list):

    ###     price_arr -- ceny
    ###     arr_of_peroid -- lista wszytkich okresów do guppy

    for element in arr_of_peroid :
        ema_string : tuple = EMA(price_arr,element)
        plt.plot(list(ema_string.keys()),list(ema_string.values()),label="EMA") 