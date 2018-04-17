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

fractalSet = setCreator(-1, -0.5, 0.001, -0.5, 0.5, 0.001, complex(-0.56, 0.165), 200, 750, "Mandelbrot set")
fractalPlotter(fractalSet)
