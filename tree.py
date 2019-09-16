# This is a simple program to create a tree

def main():
    lines = int(input("How big would you like your tree to be: "))
    length = (lines * 2) - 1
    spaces = (length - 1) // 2
    i = 1

    while i <= lines:
        print(" " * (spaces - i + 1), "#" * (2 * i - 1))
        i = i + 1
    print(" " * (int(lines) - 1), "#")

main()
