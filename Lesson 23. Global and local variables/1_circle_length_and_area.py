def circle_length(radius):
    return 2 * PI * float(radius)


def circle_area(radius):
    return PI * (float(radius) ** 2)


def main():
    radius = input()
    print(circle_length(radius), circle_area(radius))


PI = 3.14159
# print(circle_length(5))
# print(circle_area(10))
# main()
