from itertools import permutations
from math import atan2
from copy import deepcopy

def angle(p1, p2):
    return abs(atan2(p1[1],p1[0]) - atan2(p2[1],p2[0])) * 57.2958

def dist(p1, p2):
    return (((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5)/vel + angle(p1,p2) * 0.2

def tot_dist(points):
    return sum([dist(point, points[i + 1]) for i, point in enumerate(points[:-1])])

def tsp(points, start=None):
    if start is None:
        start = points[0]
        pointused=deepcopy(points)
        pointused.append(points[0])
        path=pointused
        distused=tot_dist(pointused)
    for pm in permutations(points):
        pm = list(pm)
        if pm[0]==start:
            pm.append(start)
            if tot_dist(pm) < distused:
                path=pm
                distused=tot_dist(pm)
            print(pm)
            print(tot_dist(pm))
    return path

num_times=[]
points=[]
num_points=int(input("Enter the number of points"))
for x in range(num_points):
    pnt=[]
    pnt.append(float(input("Enter the x co-ordinate")))
    pnt.append(float(input("Enter the y co-ordinate")))
    points.append(pnt)
vel=float(input("Enter the velocity "))
order=tsp(points)
print("""The order is {} \nThe time taken  is {}.""".format(order, tot_dist(order),))
input()
