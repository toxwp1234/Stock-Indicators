'''


        Least Square Moving Avrage

        - polega na przewidywaniu przy pomocy regresji liniowrj
         przyszłych cen.


         = = = jak działa?
        
        
         - z "okres" elementowego zbiory licze liniową regresje.
            potem obliczając przewidywaną wartość


'''



'''
                Przez to że nie chce używać żadnych trzecich bibliotek poświęcam czas obliczenia na włąsnoreęcznie 
                napisanie funkcji regresji liniowej
'''



def LSMA(arr:list,okres:int):


    """
    Funkcje potrzebne do policzenia regresji liniowej
    

    """

        ####   Funkcja która splituje liste w miejsu pos_1 i pos_2 | [1,2,3,4] --(dla 1 i 2)--> [2,3] 

        ### Ucinam OD pozycji pos_1 do pos_2 
    def arr_split(arr:list,pos_1,pos_2):

        return arr[pos_1:pos_2+1]


        ### Funkcja licząca średnią wartość w zbiorze ||| Funkcja Pomocnicza
    def avr(arr:list):
        return sum(arr)/len(arr)




        ### Kowariancja
    def covar(x:list,y:list):
        suma : int  = 0
        x_mean = avr(x) ### średnia wartość X
        y_mean = avr(y) ### średnia wartość Y
        

        # print(y,len(x))
        for i in range(len(x)):
            suma+=(x[i]-x_mean)*(y[i]-y_mean)
        return suma


    ### Wariacja 

    def var(x:list):
        suma : int = 0
        x_mean=avr(x)
        for i in range (len(x)):
            suma+=(x[i]-x_mean)**2
        
        return suma


    def expected(x,xs:list,ys:list):
        x_mean = avr(xs)
        y_mean = avr(ys)
        nachylanie : float = covar(xs,ys)/var(xs)
        wolny = y_mean - nachylanie*x_mean
        return nachylanie*x + wolny


    """

    Mechanizm Funkcji

    
    przelatuje przez wszyskie mozliwe dni i dla każdego ciągu obliczam liniową regresję i obliczam
    wartość "teorytyczną" dla ostatniego elementu





    """
    ### jeżeli okres jest jakis inny
    if(okres<=1):
        return {i: arr[i] for i in range(len(arr))}


    size:int = len(arr) ## wielkośc mojej tablicy



    day_list:list = list(range(0,okres,1)) # GENERUJE tablice z iloścą dni


    wynik : dict = {} ### tworze słownik gdzie zapisuje moje wyniki dla każdego dnia


    for day in range(okres-1,size,+1): ### lece przez wszykie element 

        wynik[day] = expected(okres-1,day_list,arr_split(arr,day-okres+1,day)) #korekta o 1 bo by zrwało za długo

    
    return wynik



"""
Testy



import matplotlib.pyplot as plt


test_lista :list = [2,4,9,7,3,2]
plt.plot((list(range(len(test_lista)))),(test_lista))


slownik_test : dict =LSMA(test_lista,4)

print(slownik_test)


plt.plot(list(slownik_test.keys()),list(slownik_test.values()))

plt.show()



"""
