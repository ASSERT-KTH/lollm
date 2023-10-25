import random

nombres = ['Andres', 'Juan', 'Carlos', 'Ricardo', 'Luis', 'Jose', 'Diego', 'Miguel', 'Gabriel', 'Fernando', 'Santiago']
apellidos = ['Rodriguez', 'Garcia', 'Martinez', 'Lopez', 'Gonzalez', 'Perez', 'Sanchez', 'Ramirez', 'Torres', 'Rojas']
apodos = ['El rapidito', 'El matador', 'El mago', 'El inmortal', 'El titán', 'La muralla', 'La bala', 'El pulpo', 'El crack', 'El campeón']
equipos = ['Boca Juniors', 'River Plate', 'Independiente', 'Racing', 'San Lorenzo', 'Americade Cali', 'Nacional de Uruguay', 'Colo Colo', 'Universidad de Chile', 'Santos']
nacionalidades = ['Argentina', 'Brasil', 'Colombia', 'Chile', 'Uruguay', 'Bolivia', 'Ecuador', 'Paraguay', 'Perú', 'Venezuela']
estadisticas_divertidas = ['Ha comido 1000 empanadas en su vida', 'Es el campeón de tango en su barrio', 'Colecciona medias de fútbol', 
                           'Le tiene miedo a los perros', 'Tiene un tatuaje de su mascota en el brazo', 'Una vez se perdió volviendo del estadio']

def genera_jugador():
    nombre = random.choice(nombres) + ' ' + random.choice(apellidos)
    apodo = random.choice(apodos)
    equipo = random.choice(equipos)
    nacionalidad = random.choice(nacionalidades)
    estadistica_divertida = random.choice(estadisticas_divertidas)

    jugador = {
        'nombre': nombre,
        'apodo': apodo,
        'equipo': equipo,
        'nacionalidad': nacionalidad,
        'estadistica_divertida': estadistica_divertida
    }

    return jugador

# Genere y muestre 10 jugadores
for _ in range(10):
    jugador = genera_jugador()
    print(jugador)