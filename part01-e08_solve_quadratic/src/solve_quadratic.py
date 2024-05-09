#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    x1 = (-b + math.sqrt((b**2 - 4 * a * c)))/ (2 * a)
    x2 = (-b - math.sqrt((b**2 - 4 * a * c))) / (2 * a)
    return (x1,x2)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    print(solve_quadratic(-2.000000, 2.000000, 1.000000))

if __name__ == "__main__":
    main()
