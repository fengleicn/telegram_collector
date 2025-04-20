import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "h:")
for k, v in opts:
    print(v)