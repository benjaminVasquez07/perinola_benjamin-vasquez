from random import choices
class Perinola:
    def __init__(self):
        self.apuesta = 'Pon 1'
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):
        carasDado=("Pon 1","Pon 2","Toma 1","Toma 2","Todos Toman","Ponen Todos")
        self.cara_visible = choices(carasDado)
        return self.cara_visible