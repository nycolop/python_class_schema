class Usuarios:
    def __init__(self, id, nombre, apellido, puesto, correo_electronico, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña

    def __str__(self):
            return f"ID: {self.id} - Titulo: {self.nombre} - Descripcion: {self.apellido} - Puesto: {self.puesto} - Correo: {self.correo_electronico} - Contraseña: {self.contraseña}"