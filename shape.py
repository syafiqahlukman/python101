# Function to draw a right-angled triangle
def draw_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

# Set the height of the triangle
triangle_height = 5

# Draw the triangle
draw_triangle(triangle_height)