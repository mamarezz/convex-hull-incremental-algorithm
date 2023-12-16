import matplotlib.pyplot as plt

# Point class definition
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Function to compute convex hull
def computeConvexHull(points):
    # Sort points based on x-coordinate
    points.sort(key=lambda point: point.x)

    # Initialize upper and lower hulls
    upperHull = []
    lowerHull = []

    # Compute upper hull
    for point in points:
        while len(upperHull) >= 2 and isCounterClockwiseTurn(upperHull[-2], upperHull[-1], point):
            upperHull.pop()
        upperHull.append(point)

    # Compute lower hull
    for point in reversed(points):
        while len(lowerHull) >= 2 and isCounterClockwiseTurn(lowerHull[-2], lowerHull[-1], point):
            lowerHull.pop()
        lowerHull.append(point)

    # Combine upper and lower hulls to get convex hull
    convexHull = upperHull + lowerHull[1:-1]

    return convexHull

# Function to check if a turn is counterclockwise
def isCounterClockwiseTurn(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y) < 0

# Example usage
points = [Point(0, -4), Point(1, 3), Point(2, 1), Point(3, 3), Point(4, -6), Point(5, 0)]
convexHull = computeConvexHull(points)

# Add a new point
# new_point = Point(2, -6)
# points.append(new_point)

# convexHull = computeConvexHull(points)


# Extract x and y coordinates for plotting
x_coords = [point.x for point in points]
y_coords = [point.y for point in points]

# Extract x and y coordinates for convex hull
convex_x = [point.x for point in convexHull]
convex_y = [point.y for point in convexHull]

# Plot the points and convex hull
plt.scatter(x_coords, y_coords, label='Points')
plt.plot(convex_x + [convex_x[0]], convex_y + [convex_y[0]], label='Convex Hull', color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
