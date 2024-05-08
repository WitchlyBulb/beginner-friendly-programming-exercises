"""ex.4
You now own some property and you want to calculate the total area of the property.

Create a program that:
1) Reads the width and height
2) Prints the area

* Example: width = 5, height = 2
* Output: total_area = 10  """

def dimensions_of_property(shape, base, height):
    if shape == "Triangle":
        area = 0.5 * base * height
    elif shape == "Rectangle":
        area = base * height
    elif shape == "Square":
        area = base * height
    elif shape == "Parallelogram":
        area = base * height
    else:
        area = print("System cannot determine area for that shape")
    return area

property_shape = "Rectangle"
b = 7
h = 8

result = dimensions_of_property(property_shape, b, h)     
print(result)