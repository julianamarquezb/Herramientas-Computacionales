import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

datos = np.genfromtxt("difusion_gas.csv", delimiter = ",")
i = -1

def cuenta(i):
    i += 1
    return int(i)

def frame(f):
    u = datos[100*f:100*(f+1),:]
    u = u.reshape(100,101)
    return u

def animar():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    im = ax.imshow(frame(f), cmap='Blues', interpolation='bilinear', vmin=0)
    im.set_clim([0, 1])
    fig.set_size_inches([5, 5])

    plt.tight_layout()

    def actualizar(n):
        f = cuenta(i)
        tmp = frame(f)
        im.set_data(tmp)
        return im

    animacion = animation.FuncAnimation(fig, actualizar, 150, interval=30)
    writer = animation.writers['ffmpeg'](fps=30)

    animacion.save('difusion_gas.mp4', writer=writer, dpi=72)
    return animacion

animar()
