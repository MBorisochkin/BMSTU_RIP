from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Sqaure
import easyhelloworld


def main():
    r = Rectangle("синего", 3, 3)
    c = Circle("зелёного", 3)
    s = Sqaure("красного", 3)

    print(r)
    print(c)
    print(s)

    print()
    easyhelloworld.print_helloworld()


if __name__ == '__main__':
    main()
