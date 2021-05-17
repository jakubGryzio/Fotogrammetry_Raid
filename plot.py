import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Camera import z_i
from User import User

user = User()
fig, ax = plt.subplots()
wsp_x = [0, user.Dx]
wsp_y = [0, user.Dy]
row = z_i.getRowNumber()
rowPhotosNumber = z_i.getRowPhotosNumber()
Bx = int(z_i.getBx())
By = int(z_i.getBy())
ax.add_patch(patches.Rectangle((0, 0),
                               user.Dx, user.Dy,
                               fc='none',
                               ec='r',
                               lw=2))
plt.xlim([-3000, user.Dx + 3000])
plt.ylim([-3000, user.Dy + 3000])
for y in range(0, user.Dy, By):
    plt.plot(wsp_x, [y, y], color='b', lw=0.3)
for x in range(0, user.Dx, Bx):
    plt.plot([x, x], wsp_y, color='b', lw=0.3)
for y in range(user.Dy // row // 2, user.Dy, By):
    for x in range(int(-1.5 * Bx), user.Dx + int(1.5 * Bx), Bx):
        circle = plt.Circle((x, y), 70, color='black')
        ax.add_patch(circle)

plt.show()
