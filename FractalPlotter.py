#!/usr/bin/python3

from numpy import arange
import matplotlib.pyplot as plt

def iterator(complexValue, complexConstant):
    nextComplex = complexValue**2 + complexConstant
    return nextComplex

def safeArange(start, stop, step):
    unsafeArange = arange(start / step, stop / step)
    return step * unsafeArange

def setCreator(xMin, xMax, xStep, yMin, yMax, yStep, complexConstant, absLimit, countLimit, fractalType):
    fractal = []
    xAxis = safeArange(xMin, xMax + xStep, xStep)
    yAxis = safeArange(yMax, yMin - yStep, -1*yStep)
    for y in yAxis:
        row = []
        for x in xAxis:
            z = complex(x, y)
            if fractalType == "Julia set":
                constant = complexConstant
            elif fractalType == "Mandelbrot set":
                constant = z
            nextComplex = iterator(z, constant)
            count = 1
            done = False
            while not done:
                nextComplex = iterator(nextComplex, constant)
                count += 1
                if abs(nextComplex) > absLimit:
                    row.append(count)
                    done = True
                elif count == countLimit:
                    row.append(0)
                    done = True
        fractal.append(row)
    return fractal

def fractalPlotter(fractal):
    plt.figure()
    plt.pcolormesh(fractal)
    plt.show()
    plt.close()

def fractalSaver(x, y, a, c):
    for i in range(len(x)):    
        fractalSet = setCreator(-1.5, 1.5, x[i], -1, 1, y[i], complex(-0.4, 0.6), a[i], c[i], "Julia set")
        plt.figure()
        plt.pcolormesh(fractalSet)
        plt.savefig("%s_x_%s_y_%s_a_%s_c_%s.png" % (str(i), str(x[i]), str(y[i]), str(a[i]), str(c[i])))
        plt.close()

#fractalSet = setCreator(-1.5, 1.5, 0.025, -1, 1, 0.025, complex(-0.4, 0.6), 25, 20, "Julia set")
#fractalPlotter(fractalSet)

xyList = [0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001]
acList = [10, 14, 18, 22, 26, 30, 34, 38, 42]
fractalSaver(xyList, xyList, acList, acList)