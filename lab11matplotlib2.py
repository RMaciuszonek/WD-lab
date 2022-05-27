import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

def p1():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    print(type(ax))
    t = np.linspace(0, 2*np.pi, 100)
    z = t
    x = np.sin(t)*np.cos(t)
    y = np.tan(t)
    ax.plot(x, y, z, label='zadanie 1')
    plt.show()


def p2():
    np.random.seed(19680801)
    def randrange(n, vmin, vmax):
        return (vmax - vmin)*np.random.rand(n) + vmin
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = 100
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    ax.set_zlabel('Z label')
    plt.show()


def p3():
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    np.random.seed(19680801)
    def randrange(n, vmin, vmax):
        return (vmax - vmin)*np.random.rand(n) + vmin
    n = 100
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    ax.set_zlabel('Z label')
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data()
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.show()


def p4():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, 1, 100)
    y = np.sin(x*2*np.pi) / 2 + 0.5
    ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')
    colors = ('r', 'g', 'b', 'k')
    np.random.seed(19680801)
    x = np.random.sample(20 * len(colors))
    y = np.random.sample(20 * len(colors))
    c_list = []
    for c in colors:
        c_list.extend([c] * 20)
    ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elev=20., azim=-35)
    plt.show()


def lab11matplotlib2():
    p1()
    p2()
    p3()
    p4()


if __name__ == '__main__':
    lab11matplotlib2()
