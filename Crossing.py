
# Ten kod oblicza punkty przecięcia dwóch wykresów reprezentowanych jako słowniki (zestaw_1 i zestaw_2).
# 1. Funkcja `get_info` oblicza współczynniki prostej (a, b) dla dwóch punktów.
# 2. Funkcja `punkt_przeciecia` oblicza współrzędne punktu przecięcia dwóch prostych.
# 3. Funkcja `inscope` sprawdza, czy punkt przecięcia mieści się w zakresie dwóch punktów na osi X.
# 4. Główna funkcja `crossing`:
#    - Znajduje wspólne klucze (dni) w obu zestawach danych.
#    - Iteruje po tych dniach i sprawdza:
#      a) Jeśli wartości w obu zestawach są równe, zapisuje punkt przecięcia.
#      b) Jeśli wartości się różnią, oblicza współczynniki prostych i punkt przecięcia.
#      c) Sprawdza, czy punkt przecięcia mieści się w zakresie i zapisuje go.
# 5. Na końcu zwraca słownik z punktami przecięcia.




def get_Crossing(zestaw_1:dict,zestaw_2:dict):
    """
    Funkcja pokazująca gdzie nastąpiło przecięcie dwóch wykresów.
    :param zestaw_1: Pierwszy zestaw danych (słownik).
    :param zestaw_2: Drugi zestaw danych (słownik).
    :return: Słownik z punktami przecięcia.
    """

    def get_info(x1:float,y1:float,x2:float,y2:float):


        a:float = (y2 - y1) / (x2 - x1)   ##współczynnik kierunkowy
        b:float = y1 - a * x1 ## wyraz wolny
        return [a,b] ## zwracam współczynniki prostej
    


    def punkt_przeciecia(a:float,b:float,c:float,d:float):


        """
        y=ax+b
        y=cx+d
        
        
        """

        ## obliczam punkt przcięcia prostych
        X:float = (d-b)/(a-c)
        Y:float = a*X+b

        return [X,Y]


    def inscope(val:float,range_1:int,range_2:int):


        return(abs(2*val-(range_1+range_2))-abs(range_1-range_2))<0 ### Wyprowadzona ?własnie? Wyprowadzona samodzielnie formułka


    """

    Funkcja pokazująca gdzie nastąpiło przecięcie dwóch wykresów.
    :param zestaw_1: Pierwszy zestaw danych (słownik).
    :param zestaw_2: Drugi zestaw danych (słownik).



    """

    keys_1 = set(zestaw_1.keys())
    keys_2 = set(zestaw_2.keys())
    
    universum = keys_1 & keys_2 ## intersekcja kluczy
    print(universum)
    max_element = max(universum) ## maksymalny element intersekcji kluczy


    size = len(universum) ## rozmiar intersekcji kluczy
    

    crossing_points :dict = {} ## słownik do przechowywania punktów przecięcia


    for day in universum:
        
        #jeżeli wyjde pozazakres dni to urywam pętle
        if (day + 1) > max_element:
            continue


            # jezeli ceny są rowne
        if zestaw_1[day] == zestaw_2[day]:
            
            crossing_points[day] = zestaw_1[day]
            continue    


        Z_1 :float = zestaw_1[day]
        Z_1_plus : float = zestaw_1[day+1]    

        Z_2 :float = zestaw_2[day]
        Z_2_plus : float = zestaw_2[day+1]    

        
        # print(day)

        # print(day,Z_1,day+1,Z_1_plus)


        ##linia zestawu 1
        a,b=get_info(day,zestaw_1[day],day+1,zestaw_1[day+1]) ## współczynniki prostej zestawu 1

        ##linia zestawu 2

        c,d=get_info(day,zestaw_2[day],day+1,zestaw_2[day+1]) ## współczynniki prostej zestawu 2

        ## sprawdzam gdzie sie przecieły

        ### warunki nierównoległości
        if(a==c):continue

        day_cross,price_cross = punkt_przeciecia(a,b,c,d)
        # print(day_cross,price_cross)

        if inscope(day_cross,day,day+1)==1:
            crossing_points[day_cross]=price_cross

        
    return crossing_points






"""Testing"""

# Z1 ={1:1,2:3,3:5,4:7,5:9}
# Z2 ={1:0,2:2,3:6,4:9,5:5}
# print(crossing(Z1,Z2))


# import matplotlib.pyplot as plt


# plt.plot(list(Z1.keys()),list(Z1.values()),label="Zestaw 1")
# plt.plot(list(Z2.keys()),list(Z2.values()),label="Zestaw 2")

# plt.show()