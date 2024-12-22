import math

# Function to calculate Euclidean distance
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Getting two points from the user
x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())

points = [(x1, y1), (x2, y2)]

# Calculating distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Finding the minimum distance
min_distance = min(distances)

# Printing the results
print("Points:", points)
print("Distances:", distances)
print("Minimum Distance:", min_distance)