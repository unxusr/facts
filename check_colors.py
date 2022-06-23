from colour import Color
import sys


def check_color(phrase):
    colors = []
    try:
        Color(phrase)
        colors.append(phrase)
        return phrase
    except ValueError:
        return False


if '__main__' == '__main__':
    s = sys.argv[1]
    print(check_color(s))
    color = [i for i in s.split(' ') if check_color(i)]
    for i in color:
        print(f"Found a color: {i}")

