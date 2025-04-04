

def EMA(arr:list,okres:int):

    #### definicja funckji wagi dla każdego elementu
    def f(X:int)-> float: return 1/X


    size_of_arr : int = len(arr)

    wyniki : dict ={}


    for x in range(okres-1,size_of_arr,1):
        # print(x)
        

        suma_wag : float = 0
        suma_cenowa :float = 0


        for i in range(okres):
            
            # print(x-i, arr[x-i],end=": weight :")
            # print(f"{f(i+1)}")
            suma_wag += f(i+1)
            suma_cenowa += f(i+1)*arr[x-i]


        wyniki[x] = [suma_cenowa/suma_wag]

        # print(suma_cenowa/suma_wag)
        

        # print()
    

    return wyniki

