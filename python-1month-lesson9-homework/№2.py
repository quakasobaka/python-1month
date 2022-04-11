class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self.length * self.width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {round(asphalt_mass)} т асфальта')


r = Road(20, 5000)
r.asphalt_mass()