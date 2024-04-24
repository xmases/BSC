def bezier_curve(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y

p0 = (0, 0)
p1 = (200, 500)
p2 = (500, 500)

for i in range(11):
    t = i / 10
    point = bezier_curve(p0, p1, p2, t)
    print(point)
