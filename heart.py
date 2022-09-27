from matplotlib import pyplot

a = 10
xs = [i / a for i in range(-a, a + 1)]
ys = [3 / 4 * (x ** 2) ** (1 / 3) + (1 - x ** 2) ** 0.5 for x in xs] + [3 / 4 * (x ** 2) ** (1 / 3) - (1 - x ** 2) ** 0.5 for x in xs]
xs *= 2
print(xs)
pyplot.scatter(xs, ys, color='red', marker='$♥$')
pyplot.title("С")
pyplot.grid()
pyplot.show()
