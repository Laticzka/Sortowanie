import pgzrun
from pgzero.loaders import sounds

#from pgzero.game import screen
#from pgzero.game import screen
#from pgzero.screen import Screen
#from pygame import Rect
from objects_module import Kulka
from utils import *
from copy import deepcopy
lista = list(map(float, input('Podaj elementy listy: ').split(', ')))  # do zmiany 2 (w aplikacji)
sort_type = input("Wybierz metodę sortowania (bąbelkowe, przez wstawianie, przez scalanie): ")

if sort_type == "bąbelkowe":
    i = 1
    j = i - 1
    bubble_list = create_bubble_list(lista)
    do_wstawienia = deepcopy(bubble_list[j])

if sort_type == "p w":
    i = 1
    j = i - 1

    kulek_lista = create_insertion_sort_list(lista)
    do_wstawienia = deepcopy(kulek_lista[i])

if sort_type == "p s":
    i = 1
    j = i - 1
    a = 0
    odstep = 0
    mid = midA1 = midA2 = 20
    klockow_lista = create_scal_sort_list(lista)
za_duze = False
for b in lista:
    if b >= 100 or i <= -100:
        za_duze = True



# Funkcja rysująca elementy na ekranie
def draw():
    global sort_type, j, bubble_list, za_duze, kulek_lista, klockow_lista, klockow_lista_sorted, do_wstawienia, odstep, a, mid, midA1, midA2, midB1, midB2, midB3, midB4, A1, A2, B1, B2, B3, B4, C1, C2, C3, C4, C5, C6, C7, C8
    screen.clear()
    screen.fill(WHITE)
    if sort_type == "bąbelkowe" or sort_type == "p w":

        screen.draw.text('i = {}'.format(i), center = (150, 400), color = BLACK, fontsize = 30)
        screen.draw.text('j = {}'.format(j), center=(250, 400), color=BLACK, fontsize=30)
        screen.draw.text('do wstawienia = {}'.format(do_wstawienia.value), center=(150, 300), color=BLACK, fontsize=30)
        #sposób na powrót kulki przy sortowaniu bąbekowym po zakończeniu procesu    #lifehack
        if j == 1000:
            screen.draw.filled_rect(Rect((200, 380), (100, 50)),WHITE)
            screen.draw.text('j = 0', center = (250, 400), color = BLACK, fontsize = 30)

    screen.draw.filled_rect(Rect((button_x, button_y), (button_width, button_height)), button_color)
    screen.draw.text(button_text, center = (button_x + button_width / 2, button_y + button_height / 2), color = BLACK, fontsize = 40)

    screen.draw.filled_rect(Rect((menu_button_x, menu_button_y1), (menu_button_width, menu_button_height)), menu_button1_color)
    screen.draw.text(menu_button1_text, center = (menu_button_x + menu_button_width / 2, menu_button_y1 + menu_button_height / 2), color = BLACK, fontsize = 23)
    screen.draw.filled_rect(Rect((menu_button_x, menu_button_y2), (menu_button_width, menu_button_height)), menu_button2_color)
    screen.draw.text(menu_button2_text, center = (menu_button_x + menu_button_width / 2, menu_button_y2 + menu_button_height / 2), color = BLACK, fontsize = 23)
    screen.draw.filled_rect(Rect((menu_button_x, menu_button_y3), (menu_button_width, menu_button_height)), menu_button3_color)
    screen.draw.text(menu_button3_text, center = (menu_button_x + menu_button_width / 2, menu_button_y3 + menu_button_height / 2), color = BLACK, fontsize = 23)


    if za_duze == True:
        screen.draw.text(
            str("Wybierz listę z elementami z przedziału: \n  <-99; 999>"),

            center=(430, 80), color=RED,
            fontsize=50)
    else:
        if sort_type == "p s":
            for nr, b in enumerate(klockow_lista):
                if a >= 0:
                    if nr < len(lista):
                        screen.draw.filled_rect(Rect((b.center[0], b.center[1]+(50*0)), (b.wys, b. szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0]+1/2*b.wys, b.center[1]+1/2*b.szer+(50*0)), color=BLACK, fontsize=b.wys/2)

                if a >= 1:
                    if nr < mid:
                        screen.draw.filled_rect(Rect((b.center[0], b.center[1]+(50*1)), (b.wys, b. szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0]+1/2*b.wys, b.center[1]+1/2*b.szer+(50*1)), color=BLACK, fontsize=b.wys/2)
                    if nr >=  mid:
                        screen.draw.filled_rect(Rect((b.center[0] + 80, b.center[1] + (50 * 1)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + 80, b.center[1] + 1 / 2 * b.szer + (50 * 1)),
                        color=BLACK, fontsize=b.wys / 2)

                if a >= 2:
                    x = 2
                    if nr < midA1:
                        odstep = 0
                        screen.draw.filled_rect(Rect((b.center[0], b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value),
                                         center=(b.center[0] + 1 / 2 * b.wys, b.center[1] + 1 / 2 * b.szer + (50 *x)),
                                         color=BLACK, fontsize=b.wys / 2)
                    if nr >= midA1 and nr < len(A1):
                        odstep = 40
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)
                    if nr >= len(A1) and nr < len(A1) + midA2:
                        odstep = 80
                        screen.draw.filled_rect(Rect((b.center[0] +odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)
                    if nr >= len(A1) + midA2:
                        odstep = 120
                        screen.draw.filled_rect(Rect((b.center[0] +odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)


                if a >= 3:
                    x = 3
                    if nr < midB1:
                        odstep = 0
                        screen.draw.filled_rect(Rect((b.center[0], b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value),
                                         center=(b.center[0] + 1 / 2 * b.wys, b.center[1] + 1 / 2 * b.szer + (50 *x)),
                                         color=BLACK, fontsize=b.wys / 2)
                    if nr >= midB1 and nr < len(B1):
                        odstep = 20
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)
                    if nr >= len(B1) and nr < len(B1) + midB2:
                        odstep = 40
                        screen.draw.filled_rect(Rect((b.center[0] +odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)
                    if nr >=len(B1) + midB2 and nr < len(A1):
                        odstep = 60
                        screen.draw.filled_rect(Rect((b.center[0] +odstep, b.center[1] + (50 * x)), (b.wys, b.szer)), b.color)
                        screen.draw.text(str(b.value), center=(b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)
                    if nr >= len(A1) and nr < len(A1) + midB3:
                        odstep = 80
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)),
                                                b.color)
                        screen.draw.text(str(b.value), center=(
                        b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                                         color=BLACK, fontsize=b.wys / 2)
                    if nr >= len(A1) + midB3 and nr < len(B3) + len(A1):
                        odstep = 100
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)),
                                                b.color)
                        screen.draw.text(str(b.value), center=(
                        b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                                         color=BLACK, fontsize=b.wys / 2)
                    if nr >=  len(B3) + len(A1) and nr < len(A1) + len(B3) + midB4:
                        odstep = 120
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)),
                                                b.color)
                        screen.draw.text(str(b.value), center=(
                        b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                                         color=BLACK, fontsize=b.wys / 2)
                    if nr >= (len(A1) + len(B3) + midB4):
                        odstep = 140
                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)),
                                b.color)
                        screen.draw.text(str(b.value), center=(
                        b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                        color=BLACK, fontsize=b.wys / 2)

                if a >= 4:
                    x = 4
                    odstep = 0
                    for b in klockow_lista:

                        screen.draw.filled_rect(Rect((b.center[0] + odstep, b.center[1] + (50 * x)), (b.wys, b.szer)),
                                                b.color)
                        screen.draw.text(str(b.value), center=(
                            b.center[0] + 1 / 2 * b.wys + odstep, b.center[1] + 1 / 2 * b.szer + (50 * x)),
                                     color=BLACK, fontsize=b.wys / 2)
                        odstep += 10




        elif sort_type == "bąbelkowe":

            for nr, b in enumerate(bubble_list):
                if nr != j :
                    screen.draw.filled_circle(b.center, b.radius, b.color)
                    screen.draw.text(str(b.value), center=b.center, color=BLACK, fontsize=b.radius)
                if j == len(bubble_list)-1:
                    screen.draw.filled_circle(b.center, b.radius, b.color)
                    screen.draw.text(str(b.value), center=b.center, color=BLACK, fontsize=b.radius)
            if j + 1 < len(bubble_list):
                screen.draw.filled_circle((bubble_list[j].center[0], bubble_list[j].center[1] + 80), do_wstawienia.radius, do_wstawienia.color)
                screen.draw.text(str(do_wstawienia.value), center=(bubble_list[j].center[0], bubble_list[j].center[1] + 80), color=BLACK, fontsize=do_wstawienia.radius)


        elif sort_type == "p w":
            for nr, b in enumerate(kulek_lista):
                if nr != j + 1:
                    screen.draw.filled_circle(b.center, b.radius, b.color)
                    screen.draw.text(str(b.value), center = b.center, color = BLACK, fontsize = b.radius)

            if j + 1 < len(kulek_lista):
                screen.draw.filled_circle((kulek_lista[j + 1].center[0], kulek_lista[j + 1].center[1] + 80), do_wstawienia.radius, do_wstawienia.color)
                screen.draw.text(str(do_wstawienia.value),
                                 center = (kulek_lista[j + 1].center[0], kulek_lista[j + 1].center[1] + 80), color = BLACK,
                                 fontsize = do_wstawienia.radius)

        else:
            screen.draw.text(str("Wybierz poprawny sposób sortowania: \n ('bąbelkowe', 'przez wstawianie', 'przez scalanie')"),

                             center=( 430,  80), color=RED,
                             fontsize=50)

# Funkcja obsługująca kliknięcia myszy
def on_mouse_down(pos):
    global j, i, do_wstawienia, odstep, a, mid, midA1, midA2, midB1, midB2, midB3, midB4, A1, A2, B1, B2, B3, B4, C1, C2, C3, C4, C5, C6, C7, C8

    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
        sounds.dalej_sound.play()
        if sort_type == "p s":
            a += 1
            n = len(lista)
            if n > 1:
                mid = len(lista) // 2
                A1 = lista[:mid]
                A2 = lista[mid:]
                print("mid: ", mid, "A1: ", A1, 'A2: ', A2)


            if a == 2:
                if len(A1) > 1:
                    midA1 = len(A1) // 2
                    B1 = lista[:midA1]
                    B2 = lista[midA1:len(A1)]
                print("midA1: ", midA1, "B1: ", B1, 'B2: ', B2)


                if len(A2) > 1:
                    midA2 = len(A2) // 2
                    B3 = lista[len(A1):len(A1)+midA2]
                    B4 = lista[len(A1)+midA2:]
                print("midA2: ", midA2, "B3: ", B3, 'B4: ', B4)

            if  a == 3:
                if len(B1) > 1:
                    midB1 = len(B1) // 2
                    C1 = lista[:midB1]
                    C2 = lista[midB1:len(B1)]

                if len(B2) > 1:
                    midB2 = len(B2) // 2
                    C3 = lista[len(B1):len(B1)+midB2]
                    C4 = lista[len(B1)+midB2: len(B1) +len(B2)]
                if len(B3) > 1:
                     midB3 = len(B3) // 2
                     C5 = lista[len(A1):len(A1)+midB3]
                     C6 = lista[len(A1)+midB3:len(A1)+len(B3)]

                if len(B4) > 1:
                    midB4 = len(B4) // 2
                    C7 = lista[len(A1)+len(B3):len(A1)+len(B3)+midB4]
                    C8 = lista[len(A1)+len(B3)+midB4:]




        #bąbelkowe
        if sort_type == "bąbelkowe":
            if i < len(bubble_list):
                if j < len(bubble_list) - i:
                    if bubble_list[j].value > bubble_list[j+1].value:
                        do_wstawienia.value = bubble_list[j].value
                        do_wstawienia.color = bubble_list[j].color

                        bubble_list[j].value = bubble_list[j+1].value
                        bubble_list[j].color = bubble_list[j+1].color

                        bubble_list[j+1].value = do_wstawienia.value
                        bubble_list[j+1].color = do_wstawienia.color

                        j +=1
                        if j+1 < len(bubble_list):
                            do_wstawienia.value = bubble_list[j].value
                            do_wstawienia.color = bubble_list[j].color
                    else:

                        j += 1
                        if j < len(bubble_list):
                            do_wstawienia.value = bubble_list[j].value
                            do_wstawienia.color = bubble_list[j].color
                else:
                    i += 1
                    j = 0
                    do_wstawienia.value = bubble_list[j].value
                    do_wstawienia.color = bubble_list[j].color
            else:
                j = 1000

    #sortowanie_wstaw
        if sort_type == "p w":
            if i < len(kulek_lista):
                if j >= 0 :
                    if kulek_lista[j].value > do_wstawienia.value:
                        kulek_lista[j+1].color = kulek_lista[j].color
                        kulek_lista[j+1].value = kulek_lista[j].value
                        j -= 1

                    else:
                        kulek_lista[j+1].value = do_wstawienia.value
                        kulek_lista[j+1].color = do_wstawienia.color
                        i += 1
                        j = i - 1
                        if j+1 < len(kulek_lista):
                            do_wstawienia.value = kulek_lista[j+1].value
                            do_wstawienia.color = kulek_lista[j+1].color
                else:
                    kulek_lista[j + 1].value = do_wstawienia.value
                    kulek_lista[j + 1].color = do_wstawienia.color

                    #do_wstawienia.value = kulek_lista[j + 1].value
                    #do_wstawienia.color = kulek_lista[j + 1].color


                    i += 1
                    j = i- 1





# Uruchomienie gry
pgzrun.go()