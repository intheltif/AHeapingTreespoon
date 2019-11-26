from Heap import Heap
import sys

# Value to represent a successful exit
SUCCESS = 0


def main():

    heap = Heap()
    heap.go(str(sys.argv[1]))

    print('Running completed')


if __name__ == '__main__':
    main()
    exit(SUCCESS)

