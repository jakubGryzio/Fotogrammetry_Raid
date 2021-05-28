from flask import Flask, render_template, request, redirect, url_for, session, send_file

from Camera import z_i, leica, falcon, eagle
from Plane import cessna_402, cessna_t206h, vulcan, tencam
from RaidPlan import RaidPlan
from User import User
from plot import flyPlot

app = Flask(__name__)
app.secret_key = 'secret_key'


def checkCameraValueToObject(key):
    cameras = {"z_i": z_i, "leica": leica, "falcon": falcon, "eagle": eagle}
    return cameras[key]


def checkPlaneValueToObject(key):
    planes = {"cessna": cessna_402, "n16": cessna_t206h, "vulcan": vulcan, "tencam": tencam}
    return planes[key]


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        session['camera'] = request.form.getlist('camera')[0]
        session['plane'] = request.form.getlist('plane')[0]
        return redirect(url_for('parameters'))
    return render_template('index.html')


@app.route('/parameters', methods=['POST', 'GET'])
def parameters():
    if request.method == 'POST':
        session['dx'] = request.form.get('dx')
        session['dy'] = request.form.get('dy')
        session['gsd'] = request.form.get('gsd')
        session['p'] = request.form.get('p')
        session['q'] = request.form.get('q')
        return redirect(url_for('visualization'))
    return render_template('parameters.html')


@app.route('/visualization')
def visualization():
    camera = checkCameraValueToObject(session.get('camera'))
    plane = checkPlaneValueToObject(session.get('plane'))
    gsd, p, q, dx, dy = session.get('gsd'), session.get('p'), session.get('q'), session.get('dx'), session.get('dy')
    user = User(float(gsd), float(p), float(q), int(dx), int(dy))
    camera.user = user
    W = round(camera.getW(), 2)
    Lx = round(camera.getLx(), 2)
    Ly = round(camera.getLy(), 2)
    Bx = round(camera.getBx(), 2)
    By = round(camera.getBy(), 2)
    print(camera.p, camera.q)
    raidPlan = RaidPlan(camera, plane)
    raidPlan.camera.user = user
    h, min, sec = raidPlan.flyTime()
    return render_template('visualization.html', w=W, lx=Lx, ly=Ly, bx=Bx, by=By, h=h, min=min, sec=sec)


@app.route('/visualization.png')
def plot():
    gsd, p, q, dx, dy = session.get('gsd'), session.get('p'), session.get('q'), session.get('dx'), session.get('dy')
    user = User(float(gsd), float(p), float(q), int(dx), int(dy))
    camera = checkCameraValueToObject(session.get('camera'))
    img = flyPlot(user, camera)
    return send_file(img, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run(debug=True)
