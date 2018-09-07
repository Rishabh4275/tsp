from itertools import permutations
from math import atan2

def angle(p1, p2):
    return abs(atan2(p1[1],p1[0]) - atan2(p2[1],p2[0])) * 57.2958

def dist(p1, p2):
    return (((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5)/vel + angle(p1,p2) * 0.2

def tot_dist(points):
    return sum([dist(point, points[i + 1]) for i, point in enumerate(points[:-1])])

def tsp(points, start=None):
    if start is None:
        start = points[0]
    return min([pm for pm in permutations(points) if pm[0] == start], key=tot_dist)


points = [[100, 3], [32, 12], [34, 34], [67, 100],
          [5, 99], [32, 58], [95, 167], [105, 5]]
vel=float(input("Enter the velocity "))
order=tsp(points)
print("""The order is {} \nThe time taken  is {}.""".format(order, tot_dist(order),))

