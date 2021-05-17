from Camera import z_i
from Plane import tencam
from RaidPlan import RaidPlan
from User import User


def main():
    user = User(0.25, 60, 30, 19090, 17219)
    raidPlan = RaidPlan(z_i, tencam)
    raidPlan.camera.user = user
    return raidPlan.flyTime()


if __name__ == "__main__":
    print(main())









