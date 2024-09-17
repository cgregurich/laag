import matplotlib.pyplot as plt

class Matrix:
    def __init__(self, data):
        self.data = data

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def translate(point, dx, dy):
    return Point(point.x + dx, point.y + dy)

def configure_plt():
    plt.plot()
    plt.xticks(range(-5, 6, 1))
    plt.yticks(range(-5, 6, 1))

    ax = plt.gca()
    ax.spines['left'].set_position('zero')    # y-axis
    ax.spines['bottom'].set_position('zero')  # x-axis
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('equal', adjustable='box')

def plot_data(*args):
    """
    args should be a list of lists of Point objects
    """
    print(args)
    for list_of_points in args:
        x = [p.x for p in list_of_points]
        y = [p.y for p in list_of_points]
        plt.plot(x, y, marker='o')


points = [
    Point(1, 3),
    Point(1, 0),
    Point(-2, -1),
    Point(-1, 1),
]
points.append(points[0]) # add the first point to end of list so all points connect fully

dx = 1
dy = 1
translated_points = [translate(point, dx, dy) for point in points]

plot_data(points, translated_points)
configure_plt()

plt.grid(True)
plt.show()