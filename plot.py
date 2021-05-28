import math
from io import BytesIO

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def flyPlot(user, camera):
    fig, ax = plt.subplots(figsize=(12, 7))
    wsp_x = [0, user.Dx]
    wsp_y = [0, user.Dy]
    camera.user = user
    row = camera.getRowNumber()
    rowPhotosNumber = camera.getRowPhotosNumber()
    Bx = int(camera.getBx())
    By = int(camera.getBy())
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
        for x in range(math.ceil(-1.5 * Bx), user.Dx + math.ceil(1.5 * Bx), Bx):
            circle = plt.Circle((x, y), 70, color='black')
            ax.add_patch(circle)
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img, transparent=True, bbox_inches='tight', pad_inches=0)
    img.seek(0)
    return img