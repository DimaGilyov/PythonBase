class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass_asphalt(self):
        """
         Method for calculating the mass of asphalt
        :return: result in tons
        """
        return (self._length * self._width * 25 * 5) / 1000


road_1 = Road(5000, 20)
print(f"Расчет массы асфальта: {road_1.calculate_mass_asphalt()} т")
