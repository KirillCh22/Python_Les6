import sys
from module_for_check_queen import are_queens_safe


def main():
    positions = [(int(sys.argv[i]), int(sys.argv[i+1])) for i in range(1, len(sys.argv), 2)]

    if are_queens_safe(positions):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()