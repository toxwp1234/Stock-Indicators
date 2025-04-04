###
###
###
### Tutaj jest simple moving avrage
###
### W moim zaimplementowaniu cena aktualna ma sie wlicza
###
###

### do funkcji daje dane dni oraz okres
### SMA ([10,20,30,20,10],2)
### każda pozycja ma  id równe jej pozycji. Dlatego 0:10 1:20 2:30 3:20 4:10 -- tak jakby pozycja 1 to 20
###

def SMA(ceny_zamkniecia : list, okres:int):

    dane : dict ={} #tworze słownik który bedzie przetrzymywał dane w postaci dane[numer_id] = wartośc

    lenght_of_list = len(ceny_zamkniecia) #dlugosc listy z cenami
  
    #gdy okres jest dluzszy od listy cen
    if(okres>lenght_of_list):
        print("błedne dane")
        return {}

    #ile razy powtarzam petle

    n : int = lenght_of_list-okres+1

    for id in range(lenght_of_list-1,okres-2,-1):

        suma : int = 0  ##inicjalizuje sume która zostanie potem, podzielona przez okres aby odrzymać średnia
        
        #pętla aby przejśc przez każdy element pod naszym i policzyć srednią
        for i in range(okres):
            suma += ceny_zamkniecia[id-i]

        dane[id] = suma/okres



    sorted(dane)
    return dane




