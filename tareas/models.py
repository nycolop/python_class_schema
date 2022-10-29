class Tareas:
    def __init__(self, id, titulo, descripcion, fecha_limite, asignado_id, prioridad_id):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.asignado_id = asignado_id
        self.prioridad_id = prioridad_id

    def __str__(self):
        return f"ID: {self.id} - Titulo: {self.titulo} - Descripcion: {self.descripcion} - Fecha límite: {self.fecha_limite} - Asignado: {self.asignado_id} - Prioridad: {self.prioridad_id}"