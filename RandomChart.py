import random
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from typing import Optional ## dodac potem opcjonalny smoothing


###         Opis funkcji

### Do funkcji wrzucam ile elementów mam wygenerować 
### 
###             jako return otrzymuje wygenerowane dwie listy, jedna z numerami od 1 do n
###             druga zaweiera szum dla każdego n perlina 



def get_random_data(number_of_instances:int):
    
    arr_of_noise : list = [] # inicjalizacja listy
    arr_of_numbers :list = []
    noise : object = PerlinNoise(octaves=1)

    ###         Parametry szumu 
    power = random.randint(2,3)
    delta_X = 300 ## przesunięcie funkcji trendu | f(x+delta_x)

    _price : dict={} # tworze słownik wyników dzien:cena

    for i in range(number_of_instances):


            ###     Parametry
        S = 1/6
        Part_A : float = 21*noise(S*((i+233)/89))
        Part_B :float = 55*noise(S*(i / 144))
        Part_C : float =  34*noise(S*(i / 10))
        Part_D : int = 13

        trend : float = (i+delta_X)**(1/power)


        
        _price[i] = abs(round(Part_A + Part_B - Part_C+Part_D,2))+trend

    return _price








