from Heap import Heap
import sys

"""
Driver.py

The driver for our heap application

Author: Evert Ball
Author: Chris Wolf
Version: 1.0.0 (December 6, 2019)
"""

def main():
    """
    Entrypoint to our software
    """
    heap = Heap()
    if len(sys.argv) != 2:
        print('usage: python Driver.py <text_file>')
    else:
        heap.go(str(sys.argv[1]))

# Runs main
if __name__ == '__main__':
    main()
    exit(0)

