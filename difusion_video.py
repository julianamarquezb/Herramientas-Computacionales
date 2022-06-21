import numpy as np
import matplotlib.pyplot as plt
import subprocess

datos = np.genfromtxt("difusion_gas.csv", delimiter = ",")
f = plt.figure(frameon=False, figsize=(4, 5), dpi=100)
largo, alto = f.canvas.get_width_height()
ax = f.add_axes([0, 0, 1, 1])

def actualizar(frame):
    u = datos[100*frame:100*(frame+1),:]
    u = u.reshape(100,101)
    plt.figure()
    plt.title("Coeficiente de difusión = 0.2")
    plt.xlabel("x (cm)")
    plt.ylabel("y (cm)")
    plt.imshow(u, cmap='Blues', interpolation='bilinear', vmin=0)
    plt.show()
    plt.close()

video = 'difusion.mp4'
info = ('ffmpeg','-y', '-r', '30', '-s', '%dx%d' % (largo, alto), '-pix_fmt', 'argb', '-f', 'rawvideo',  '-i', '-', '-vcodec', 'mpeg4', video)
p = subprocess.Popen(info, stdin=subprocess.PIPE)

for frame in range(len(datos)):
    actualizar(frame)
    plt.draw()

    cout = f.canvas.tostring_argb()

    p.stdin.write(cout)

p.communicate()
