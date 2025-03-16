def sortowanie_wstaw(lista):
    for i in range(1, len(lista)):  # n powtórzeń
        do_wstaw = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > do_wstaw:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = do_wstaw
