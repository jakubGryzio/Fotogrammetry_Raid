class Plane:
    def __init__(self, name, min_speed, max_speed, ceil, fly_time):
        self.name = name
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.ceil = ceil
        self.fly_time = fly_time

    def getSpeed(self):
        return self.min_speed, self.max_speed


cessna_402 = Plane("Cessna 402", 132, 428, 8200, 5)
cessna_t206h = Plane("Cessna T206H NAV III", 100, 280, 4785, 5)
vulcan = Plane("Vulcan Air P86 Observer 2", 135, 275, 6100, 6)
tencam = Plane("Tencam MMA", 120, 267, 4572, 6)
