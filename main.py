class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def atributos(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        return color, ruedas, puertas


class Coche(Vehiculo):
    velocidad_max = None
    cilindrada = None

    def mecanica(self, velocidad, cilindrada):
        self.velocidad_max = velocidad
        self.cilindrada = cilindrada


Mazda_RX7 = Coche()
Mazda_RX7.atributos('rojo', 4, 2)
Mazda_RX7.mecanica(240, 1.4)

print('El Mazda RX-7 cuenta con', Mazda_RX7.puertas, 'puertas, es de color', Mazda_RX7.color, 'y tiene una cilindrada de', Mazda_RX7.cilindrada, 'con velocidad maxima de hasta', Mazda_RX7.velocidad_max, 'Km/h')
