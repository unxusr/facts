from colour import Color
import sys

def check_color(color):
    colors = []
    try:
        Color(color)
        colors.append(color)
        return color
    except ValueError:
        return False
    print(colors)
    #return f"Colors Detected {colors}"


if '__main__' == '__main__':
    s = sys.argv[1]
    print(check_color(s))
    color = [i for i in s.split(' ') if check_color(i)]
    for i in color:
        print("Found a color:", i)

