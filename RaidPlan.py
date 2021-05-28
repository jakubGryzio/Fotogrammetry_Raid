import math


class RaidPlan:
    camera = None
    plane = None

    def __init__(self, camera, plane):
        self.camera = camera
        self.plane = plane

    def interval(self):
        Bx = self.camera.getBx()
        min_speed, max_speed = self.plane.getSpeed()
        return (Bx / min_speed) * (36 / 10), (Bx / max_speed) * (36 / 10)

    def flyTime(self):
        photosNumber = self.camera.getRowPhotosNumber()
        rowNumber = self.camera.getRowNumber()
        max_interval, min_interval = self.interval()
        time = (photosNumber - 1) * min_interval * rowNumber + (140 * (rowNumber - 1))
        print(time)
        return math.floor(time / 3600), math.floor((time - math.floor((time / 3600)) * 3600) / 60), \
               math.floor((time - math.floor((time / 3600)) * 3600) - math.floor(
                   (time - math.floor((time / 3600)) * 3600) / 60) * 60)
