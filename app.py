from tareas.models import Tareas
from prioridades.models import Prioridades
from usuarios.models import Usuarios
from datetime import datetime

fecha_limite = datetime(2022, 11, 1)

tareas = Tareas(1, 'Maquetar página home', "Realizar la página de home con CSS y HTML", fecha_limite, 1, 1)
prioridades = Prioridades(1, "Alta", "Rojo")
usuarios = Usuarios(1, "Pepe", "Gutierrez", "Ejecutivo", "pepeguitierrez@gmail.com", "pepito1234")

print(usuarios)
print(prioridades)
print(tareas)