class Kulka:
    def __init__(self, center, radius, value, color):
        self.center = center
        self.radius = radius
        self.value = value
        self.color = color

class Klocek:
    def __init__(self, center, wys, szer, value, color):
        self.center = center
        self.wys = wys
        self.szer = szer
        self.value = value
        self.color = color
    def __str__(self):
        return  str(self.value)+ str(self.color)