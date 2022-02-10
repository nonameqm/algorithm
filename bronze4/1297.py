import math


d, h, w=map(int, input().split())

height, width = d*h/math.sqrt(h*h+w*w), d*w/math.sqrt(h*h+w*w)

print(int(height), int(width))