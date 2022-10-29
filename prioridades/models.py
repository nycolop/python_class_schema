class Prioridades():
    def __init__(self, id, titulo, color):
        self.id= id
        self.titulo= titulo
        self.color= color

    def __str__(self):
        return f"ID: {self.id} - Titulo: {self.titulo} - Color: {self.color}"