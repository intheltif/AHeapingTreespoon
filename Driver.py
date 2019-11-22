# Driver class
from Heap import Heap

import sys

if __name__ == '__main__':
    heap = Heap()
    heap.go(sys.argv[1])

    print('Computation is finished')
