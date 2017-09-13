import sys

def add(a, b):
    print(a + b)


if __name__ == "__main__":
    a, b = sys.argv[1], sys.argv[2]
    add(a,b)
