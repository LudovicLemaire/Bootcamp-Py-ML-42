import sys

if len(sys.argv) > 1:
    revAlpha = ' '.join(sys.argv[1:])[::-1].swapcase()
    print(revAlpha)
