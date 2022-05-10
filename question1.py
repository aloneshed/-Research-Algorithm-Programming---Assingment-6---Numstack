import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

"""
sources:
https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html
https://github.com/erelsgl-at-ariel/research-5782/blob/main/06-python-numstack/code/2.matplotlib.ipynb
https://stackoverflow.com/questions/40580025/np-array-intersection-attributeerror-module-object-has-no-attribute-piece
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html
"""


def plotIntersection(linspace, func1, func2):
    range_from = (linspace[0])
    range_to = (linspace[-1])
    xvals_intersects = [] # list of x value intersection
    intersects = [] # list of (x,y) intersection
    for x0 in np.arange(range_from, range_to):
        x_result = fsolve(lambda x: func1(x) - func2(x), x0) # x value of optional intersection
        if (np.isclose(func1(x_result), func2(x_result)) # if the result of x is close in both function (that mean it is not min or max)
                and not any(np.isclose(x_result, xvals_intersects))): # and the list of x value intersection does not already contain the result
            xvals_intersects.append(x_result) # add the x result to the list
    for xval in xvals_intersects:
        yval = func1(xval) # finding the y value of each x value
        intersects.append([xval, yval])
    plt.plot(linspace, func1(linspace)) # plot func1
    plt.plot(linspace, func2(linspace)) # plot func2
    plt.grid()
    for x, y in intersects:
        plt.scatter(x, y) # plot the intersections
    plt.show()
    return xvals_intersects


if __name__ == '__main__':
    f1 = lambda x: x ** 2
    g1 = lambda x: x + 10
    plotIntersection(np.linspace(-10, 10, 1000), f1, g1)

    f2 = lambda x: np.sin(x)
    g2 = lambda x: 0.2 * x
    plotIntersection(np.linspace(-10, 10, 1000), f2, g2)

    f3 = lambda x: np.sin(x)
    g3 = lambda x: np.cos(x)
    plotIntersection(np.linspace(-10, 10, 1000), f3, g3)

    f4 = lambda x: x ** 3
    g4 = lambda x: x + 20
    plotIntersection(np.linspace(-10, 10, 1000), f4, g4)

    f5 = lambda x: x ** 4
    g5 = lambda x: x ** 2
    plotIntersection(np.linspace(-20, 20, 1000), f5, g5)


