# I have not given or received any unauthorized assistance on this assignment

import utility, EllipseClass
import random


def overlap(one, two):
    """returns area of overlap for 2 ellipses based on monte carlo simulation"""
    xvals = one.minmaxx(), two.minmaxx()
    minx = 0  # minimum x-val for box
    if xvals[0][0] < xvals[1][0]:
        minx = xvals[0][0]
    else:
        minx = xvals[1][0]

    maxx = 0  # maximum x-val for box
    if xvals[0][1] > xvals[1][1]:
        maxx = xvals[0][1]
    else:
        maxx = xvals[1][1]

    yvals = one.minmaxy(), two.minmaxy()
    miny = 0  # minimum y-val for box
    if yvals[0][0] < yvals[1][0]:
        miny = yvals[0][0]
    else:
        miny = yvals[1][0]

    maxy = 0  # maximum y-val for box
    if yvals[0][1] > yvals[1][1]:
        maxy = yvals[0][1]
    else:
        maxy = yvals[1][1]

    rangex = utility.distance((maxx, 0), (minx, 0))
    rangey = utility.distance((0, maxy), (0, miny))
    areaofbox = rangex * rangey

    random_points = 0
    inboth = 0

    while random_points < 10000:
        randx = random.randrange(100000) / 100000
        randy = random.randrange(100000) / 100000
        randpointx = (randx * rangex) + minx
        randpointy = (randy * rangey) + miny
        if one.inside_edge((randpointx, randpointy)) and two.inside_edge((randpointx, randpointy)):
            inboth += 1
        random_points += 1
    pointsinboth = inboth / 10000  # ratio of points in both to total random points
    overlaparea = round(pointsinboth * areaofbox, 3)
    return overlaparea
