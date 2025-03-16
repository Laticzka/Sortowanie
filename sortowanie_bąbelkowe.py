def sort_babel2(lista):
    for i in range(len(lista) - 1): #(n - 1) powtórzeń
        for j in range(len(lista) - 1 - i): #n / 2 powtórzeń
            if lista[j] > lista[j + 1]:
                #lista[j], lista[j + 1] = lista[j + 1], lista[j]
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp