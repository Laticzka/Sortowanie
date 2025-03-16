def sortowanie_scalanie(tab, pocz, kon):
    if pocz < kon:
        polowa = (pocz + kon) // 2
        sortowanie_scalanie(tab, pocz, polowa)
        sortowanie_scalanie(tab, polowa + 1, kon)
        scal(tab, pocz, polowa, kon)


def scal(tab, pocz, polowa, kon)
    n1 = polowa - pocz + 1
    n2 = kon - polowa

    tab_L = []
    tab_R = []

    for i in range(n1):
        tab_L[i] = tab[pocz + 1]

    for j in range(n2):
        tab_R[j] = tab[polowa + 1 + j]

        i = 0
        j = 0
        k = pocz

        while i < n1 and j < n2:
            if tab_L[i] <= tab_R[j]
                tab[k] = tab_L[i]
                i += 1
            else:
                tab[k] = tab_R[j]
                j += 1
            k += 1

        while i < n1:
            tab[k] = tab_L[i]
            i += 1
            k += 1

        while j < n2:
            tab[k] = tab_R[j]
            j += 1
            k += 1
