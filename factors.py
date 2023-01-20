#!/usr/bin/env python3

import sys


def factorize(n):

    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return (i, n//i)
    return (n, 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                n = int(line)
                p, q = factorize(n)
                print(f"{n}={p}*{q}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
