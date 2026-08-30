class Airplane:
    def __init__(self, plane_type, passengers, max_passengers):
        self.plane_type = plane_type
        self.passengers = passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, value):
        return Airplane(self.plane_type, self.passengers + value, self.max_passengers)

    def __sub__(self, value):
        return Airplane(self.plane_type, self.passengers - value, self.max_passengers)

    def __iadd__(self, value):
        self.passengers += value
        return self

    def __isub__(self, value):
        self.passengers -= value
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

plane1 = Airplane("Boeing", 100, 200)
plane2 = Airplane("Airbus", 150, 250)
print("типы одинаковые?:", plane1 == plane2)
print("plane1 < plane2 по вместимости?:", plane1 < plane2)
plane1 += 20
print("пассажиры plane1 после посадки:", plane1.passengers)