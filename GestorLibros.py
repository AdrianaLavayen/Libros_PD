import sys
sys.stdout.reconfigure(encoding='utf-8')
from abc import ABC, abstractmethod 

class Libro (ABC):
    def __init__(self, titulo, autor, anio, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio 
        self.descripcion = descripcion 
        self.terminado = False 
    @abstractmethod 
    def mostrar(self):
        pass

#Factory Method
class LibroIndependiente(Libro):
    def __init__(self, titulo, autor, anio, descripcion):
        super().__init__(titulo, autor, anio, descripcion)
    def mostrar(self):
        estado = "Terminado" if self.terminado else "Pendiente"
        print(f"[{estado}] {self.titulo} - {self.autor} ({self.anio})")
        print(f" Descripcion: {self.descripcion}")

class LibroSaga(Libro):
    def __init__(self, titulo, autor, anio, descripcion, saga):
        super().__init__(titulo, autor, anio, descripcion)
        self.saga = saga
    def mostrar(self):
        estado = "Terminado" if self.terminado else "Pendiente"
        print(f"[{estado}] {self.titulo} - {self.autor} ({self.anio}) [Saga: {self.saga}]")
        print(f" Descripcion: {self.descripcion}")

#Factory Method
class LibroFactory:
    @staticmethod
    def crear(titulo, autor, anio, descripcion, saga = None):
        if saga:
            return LibroSaga(titulo, autor, anio, descripcion, saga)
        return LibroIndependiente(titulo, autor, anio, descripcion)

#Builder
class LibroBuilder:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.anio = None
        self.descripcion = None
        self.saga = None
    def set_titulo(self, titulo):
        self.titulo = titulo
        return self
    def set_autor(self, autor):
        self.autor = autor
        return self
    def set_anio(self, anio):
        self.anio = anio
        return self
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
        return self
    def set_saga(self, saga):
        self.saga = saga
        return self 
    def build(self):
        return LibroFactory.crear(
            self.titulo, 
            self.autor,
            self.anio,
            self.descripcion,
            self.saga
        )

#Decorator
class LibroDecorator(Libro):
    def __init__(self, libro):
        self.libro = libro
    @property
    def titulo(self):
        return self.libro.titulo
    @property
    def terminado(self):
        return self.libro.terminado
    def mostrar(self):
        self.libro.mostrar()

#Decorator
class PuntuacionDecorator(LibroDecorator):
    def __init__(self, libro, puntuacion):
        super().__init__(libro)
        self.puntuacion = puntuacion
    def mostrar(self):
        self.libro.mostrar()
        print(f" Puntuacion: {'☆' * self.puntuacion} ({self.puntuacion}/5)")

#Decorator
class ReseñaDecorator(LibroDecorator):
    def __init__(self, libro, reseña):
        super().__init__(libro)
        self.reseña = reseña
    def mostrar(self):
        self.libro.mostrar()
        print(f" Reseña: {self.reseña}")

#Observer
class RegistroObserver(ABC):
    @abstractmethod
    def actualizar(self, libro):
        pass

class AvisoObserver(RegistroObserver):
    def actualizar(self, libro):
        print(f"\n '{libro.titulo}' ha sido terminado")
        print(f" Agregar puntuacion y reseña")

###############
class Registro:
    def __init__(self):
        self.libros = []
        self.observadores = []
    #Observer
    def agregar_observador(self, observador):
        self.observadores.append(observador)
    def notificar_observadores(self, libro):
        for observador in self.observadores:
            observador.actualizar(libro)
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'"{libro.titulo}" agregado al registro')
    def terminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.terminado = True
                self.notificar_observadores(libro)
                return
        print(f'No se encontro "{titulo}" en el registro')
    #Decorator
    def puntuar_libro(self, titulo, puntuacion):
        for i, libro in enumerate(self.libros):
            if libro.titulo == titulo:
                if not libro.terminado:
                    print(f'"{titulo}"aun no ha sido terminado')
                    return
                self.libros[i] = PuntuacionDecorator(libro, puntuacion)
                print(f'"{titulo}" ha sido puntuado')
                return
        print(f'No se encontro "{titulo}" en el registro')
    def reseñar_libro(self, titulo, reseña):
        for i, libro in enumerate(self.libros):
            if libro.titulo == titulo:
                if not libro.terminado:
                    print(f'"{titulo}"aun no ha sido terminado')
                    return
                self.libros[i] = ReseñaDecorator(libro, reseña)
                print(f'"{titulo}" ha sido reseñado')
                return
        print(f'No se encontro "{titulo}" en el registro')
    
    def mostrar_libros(self):
        print("\n--- Libros ---")
        for libro in self.libros:
            libro.mostrar()
            print()
        print("---------------------------------------------\n")

def main():
    registro = Registro()
    registro.agregar_observador(AvisoObserver())

    libro1 = LibroBuilder()\
    .set_titulo("Cartas desde la tierra")\
    .set_autor("Mark Twain")\
    .set_anio(1962)\
    .set_descripcion("Satan se ve obligado a escribir cartas a casa desde su exilio en la Tierra.")\
    .build()
    libro2 = LibroBuilder()\
    .set_titulo("Caraval")\
    .set_autor("Stephanie Garber")\
    .set_anio(2016)\
    .set_descripcion("Scarlett y su hermana Tella reciben invitaciones para Caraval, un espectaculo magico.")\
    .set_saga("Trilogia Caraval")\
    .build()
    libro3 = LibroBuilder()\
    .set_titulo("Boulevard")\
    .set_autor("Flor M Salvador")\
    .set_anio(2022)\
    .set_descripcion("Narra la historia de Luke y Hasley, dos adolescentes con pasados dificiles.")\
    .build()
    libro4 = LibroBuilder()\
    .set_titulo("Lagrimas en H Mart")\
    .set_autor("Michelle Zauner")\
    .set_anio(2021)\
    .set_descripcion("Conmovedora memoria de Michelle Zauner sobre su relacion con su madre fallecida.")\
    .build()
    libro5 = LibroBuilder()\
    .set_titulo("La guerra de la Amapola")\
    .set_autor("R.F. Kuang")\
    .set_anio(2018)\
    .set_descripcion("Rin, una huerfana de guerra que logra ingresar a una prestigiosa academia militar y debe frenar la invasion de una nacion.")\
    .set_saga("La guerra dde la Amapola")\
    .build()
    libro6 = LibroBuilder()\
    .set_titulo("La republica del dragon")\
    .set_autor("R.F. Kuang")\
    .set_anio(2019)\
    .set_descripcion("Sangrienta guerra civil y politica donde la protagonista busca venganza mientras intenta forjar una nueva nacion libre y democratica.")\
    .set_saga("La guerra de la Amapola")\
    .build()

    registro.agregar_libro(libro1)
    registro.agregar_libro(libro2)
    registro.agregar_libro(libro3)
    registro.agregar_libro(libro4)
    registro.agregar_libro(libro5)
    registro.agregar_libro(libro6)

    registro.mostrar_libros()

    registro.terminar_libro("Cartas desde la tierra")
    registro.terminar_libro("Caraval")
    registro.terminar_libro("Boulevard")
    registro.terminar_libro("Lagrimas en H Mart")

    registro.puntuar_libro("Cartas desde la tierra", 5)
    registro.reseñar_libro("Cartas desde la tierra", "Sentido del humor y sacrasmo 10/10, si yo fuera del 1909 tambien habria pensado que era herejia xd")
    registro.puntuar_libro("Caraval", 2)
    registro.reseñar_libro("Caraval", "Solo logro recordar las cosas malas, se siente como mi infancia.")
    registro.puntuar_libro("Boulevard", 1)
    registro.reseñar_libro("Boulevard", "Se llora mas por las faltas ortograficas que por el final")
    registro.puntuar_libro("Lagrimas en H Mart", 4)
    registro.puntuar_libro("La guerra de la Amapola", 4)

    registro.mostrar_libros()

main()