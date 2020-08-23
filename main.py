from matplotlib.animation import FuncAnimation
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import operator
import itertools


fig, ax = plt.subplots()

plt.xlim([-100, 1100])
plt.ylim([-100, 1100])

plt.autoscale(enable=False)

iteration = ax.text(1200, 1200, '', ha='right', va='top', fontsize=10)

size = 300
x_random = np.random.randint(low=0, high=1000, size=size)
y_random = np.random.randint(low=0, high=1000, size=size)


# c1_random = np.random.randint(low=0, high=size)
cx_1 = np.random.randint(low=0, high=1000)
cy_1 = np.random.randint(low=0, high=1000)


# c2_random = np.random.randint(low=0, high=size)
cx_2 = np.random.randint(low=0, high=1000)
cy_2 = np.random.randint(low=0, high=1000)

# c3_random = np.random.randint(low=0, high=size)
cx_3 = np.random.randint(low=0, high=1000)
cy_3 = np.random.randint(low=0, high=1000)


initialized = False
iteration_number = 1

c1_points = []
c2_points = []
c3_points = []


def get_distance(pointA, pointB):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(pointA, pointB)]))


def get_color(point):
    distances = [
        (get_distance(point, (cx_1, cy_1)), 'lightcoral'),
        (get_distance(point, (cx_2, cy_2)), 'skyblue'),
        (get_distance(point, (cx_3, cy_3)), 'springgreen')
    ]

    distances.sort(key=operator.itemgetter(0))

    nearest = distances[0]
    return nearest[1]


def get_centroid(points):
    x, y = zip(*points)
    centroid_x = sum(x) / len(points)
    centroid_y = sum(y) / len(points)
    return(centroid_x, centroid_y)


def animate(i):
    global initialized
    global iteration_number
    global c1_points, c2_points, c3_points
    global cx_1, cx_2, cx_3
    global cy_1, cy_2, cy_3

    iteration.set_text('Iteration:' + str(iteration_number))

    if (initialized == False):
        if (i == 0):
            ax.scatter(x_random, y_random, c="black")

        if (i != 0):
            ax.scatter([cx_1], [cy_1], c="red")
            ax.scatter([cx_2], [cy_2], c="blue")
            ax.scatter([cx_3], [cy_3], c="green")

        initialized = True

    # red, blue, green
    if (i == 1):
        ax.scatter([cx_1], [cy_1], c="red")
        ax.scatter([cx_2], [cy_2], c="blue")
        ax.scatter([cx_3], [cy_3], c="green")
        return

    # lightcoral, skyblue, springgreen

    if ((i % 2) == 0 and i != 0):
        points = zip(x_random, y_random)
        points_with_colors = [
            (
                point,
                get_color(point)
            )
            for point in points]

        c1_points_with_colors = list(
            filter(lambda x: x[1] == 'lightcoral', points_with_colors)
        )

        c2_points_with_colors = list(
            filter(lambda x: x[1] == 'skyblue', points_with_colors)
        )

        c3_points_with_colors = list(
            filter(lambda x: x[1] == 'springgreen', points_with_colors)
        )

        c1_points = list(point for point, color in c1_points_with_colors)
        c1_x, c1_y = zip(*c1_points)
        ax.scatter(c1_x, c1_y, c="lightcoral")
        ax.scatter([cx_1], [cy_1], c="red")

        c2_points = list(point for point, color in c2_points_with_colors)
        c2_x, c2_y = zip(*c2_points)
        ax.scatter(c2_x, c2_y, c="skyblue")
        ax.scatter([cx_2], [cy_2], c="blue")

        c3_points = list(point for point, color in c3_points_with_colors)
        c3_x, c3_y = zip(*c3_points)
        ax.scatter(c3_x, c3_y, c="springgreen")
        ax.scatter([cx_3], [cy_3], c="green")
        return

    if (i % 2 > 0):
        iteration_number += 1
        ax.scatter([cx_1], [cy_1], c="lightcoral")
        ax.scatter([cx_2], [cy_2], c="skyblue")
        ax.scatter([cx_3], [cy_3], c="springgreen")

        # get new centroids
        cx_1, cy_1 = get_centroid(c1_points)
        cx_2, cy_2 = get_centroid(c2_points)
        cx_3, cy_3 = get_centroid(c3_points)

        initialized = False


ani = FuncAnimation(fig=fig, func=animate, frames=range(100),
                    interval=1000, repeat=False)


# f = ax.scatter(x_random, y_random, c="black")


# plt.scatter(x_random, y_random, c="orange")

plt.show()
