from Heap import Heap
import sys

# Value to represent a successful exit
SUCCESS = 0


def main():
    """
    Entrypoint to our software
    """
    heap = Heap()
    if len(sys.argv) != 2:
        print('usage: python Driver.py <text_file>')
    else:
        heap.go(str(sys.argv[1]))


if __name__ == '__main__':
    main()
    exit(SUCCESS)

