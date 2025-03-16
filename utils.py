from copy import deepcopy
from objects_module import Kulka, Klocek

# from main import lista


# do zmiany 1
kolory_elementow = [(171, 202, 125), (5, 235, 31), (202, 33, 88), (26, 10, 210), (199, 28, 99), (120, 19, 67),
                    (207, 214, 233), (245, 122, 57), (214, 132, 229), (7, 141, 19), (171, 202, 125), (5, 235, 31),
                    (202, 33, 88), (26, 10, 210), (199, 28, 99), (120, 19, 67), (207, 214, 233), (245, 122, 57),
                    (214, 132, 229), (7, 141, 19)]
kolory_babelkow = [
    (100, 149, 237),  # Cornflower Blue
    (70, 130, 180),  # Steel Blue
    (95, 158, 160),  # Cadet Blue
    (72, 209, 204),  # Medium Turquoise
    (30, 144, 255),  # Dodger Blue
    (0, 140, 255),  # Darker Sky Blue
    (0, 120, 200),  # Custom Darker Blue
    (25, 100, 180),  # Deep Sea Blue
    (50, 90, 160),  # Muted Blue
    (40, 80, 150),  # Midnight Soft Blue
    (173, 216, 230),  # Light Blue
    (176, 224, 230),  # Powder Blue
    (135, 206, 250),  # Light Sky Blue
    (135, 206, 255),  # Sky Blue
    (0, 191, 255),  # Deep Sky Blue
    (176, 226, 255),  # Light Steel Blue
    (198, 226, 255),  # Light Cornflower Blue
    (202, 225, 255),  # Alice Blue
    (240, 248, 255),  # Almost White-Blue
]
kolory_kulek = [
    (219, 112, 147),  # Pale Violet Red
    (199, 21, 133),  # Medium Violet Red
    (178, 58, 135),  # Darker Pink
    (208, 32, 144),  # Vivid Pink
    (255, 20, 147),  # Deep Pink
    (190, 85, 135),  # Soft Dark Pink
    (175, 80, 120),  # Faded Pink
    (160, 70, 110),  # Darker Cotton Candy
    (150, 60, 100),  # Muted Raspberry Pink
    (140, 50, 90),
    (255, 160, 176),  # Baby Pink
    (255, 153, 204),  # Pastel Pink
    (255, 105, 180),  # Hot Pink
    (255, 240, 245),  # Lavender Blush
    (255, 220, 230),  # Very Light Pink
    (255, 210, 220),  # Cotton Candy Pink
    (255, 200, 215),  # Soft Pink
]
kolory_klockow = [
    (255, 140, 0),  # Dark Orange
    (210, 105, 30),  # Chocolate
    (205, 133, 63),  # Peru
    (184, 134, 11),  # Dark Goldenrod
    (218, 165, 32),  # Goldenrod
    (255, 120, 60),  # Muted Orange
    (230, 110, 50),  # Sunset Orange
    (200, 90, 40),  # Deep Carrot Orange
    (180, 80, 30),  # Rustic Orange
    (160, 70, 20),  # Burnt Orange
    (255, 250, 220),  # Almost White Orange
    (255, 200, 150),  # Light Peach
    (255, 180, 120),  # Apricot
    (255, 165, 100),  # Peach Orange
    (255, 190, 140),  # Soft Orange
    (255, 215, 160),  # Light Golden Orange
    (255, 223, 186),  # Very Light Orange
    (255, 228, 181),  # Moccasin
    (255, 240, 200),  # Papaya Whip
    (255, 245, 210),  # Creamy Orange
    (255, 250, 220)
]
# Rozmiary ekranu
WIDTH = 1000
HEIGHT = 600

# Kolory podstawowe komponentów na scenie
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

BACKGROUND = (255, 255, 255)
# Parametry przycisku "Dalej"
button_width = 200
button_height = 100
button_x = WIDTH - button_width
button_y = HEIGHT - button_height
button_color = RED
button_text = "Dalej --->"

menu_button_width = 200
menu_button_height = 26
menu_button_x = WIDTH - button_width - menu_button_width - 7
menu_button_y1 = HEIGHT - button_height
menu_button_y2 = menu_button_y1 + menu_button_height + 7
menu_button_y3 = menu_button_y2 + menu_button_height + 7

menu_button1_color = (153, 228, 234)
menu_button2_color = (214, 139, 181)
menu_button3_color = (225, 160, 122)
menu_button1_text = "Bąbelkowe"
menu_button2_text = "Przez wstawianie"
menu_button3_text = "Przez scalanie"


def create_bubble_list(lista):
    global radius_kulki, odstep_kulki
    radius_kulki = 30
    odstep_kulki = 20
    if len(lista) > 12:
        radius_kulki = 20
        odstep_kulki = 15
    bl = []  # lista bąbelków
    for i, e in enumerate(lista):
        bl.append(
            Kulka((i * (int(odstep_kulki + 2 * radius_kulki)) + 50, 60), int(radius_kulki), e, kolory_babelkow[i]))
    return bl


def create_insertion_sort_list(lista):
    global radius_kulki, odstep_kulki
    radius_kulki = 30
    odstep_kulki = 20
    if len(lista) > 12:
        radius_kulki = 20
        odstep_kulki = 15
    kl = []  # lista kulek
    for i, e in enumerate(lista):
        kl.append(Kulka((i * (odstep_kulki + 2 * radius_kulki) + 50, 60), radius_kulki, e, kolory_kulek[i]))
    print(kl)
    return kl


def create_scal_sort_list(lista):
    kl = []  # lista klocków
    for i, e in enumerate(lista):
        kl.append(Klocek((i * (2 * 22) + 10, 30), 40, 40, e, kolory_klockow[i]))
    return kl


def sort_list(lista):
    sort_lista = []
    lista_copy = deepcopy(lista)
    while lista_copy:
        min_value = min(lista_copy, key=lambda e: e.value)  # Znajduje klocek z najmniejszą wartością
        sort_lista.append(min_value)
        lista_copy.remove(min_value)  # Usuwa znaleziony element
    return sort_lista


