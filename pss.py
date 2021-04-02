#issubclass(int, int)
#Utiliza pass
class circle:
    def __init__(self, radio):
        self.radio = radio

class colored_circle(circle):
    def __init__(self, radio, color):
        super().__init__(radio)
        self.colore = color

print(issubclass(colored_circle, circle))

class dinero:
    pass

class billetera(dinero):
    pass

print(issubclass(billetera,dinero))
