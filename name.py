import sys
import lists

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("No arguments.")