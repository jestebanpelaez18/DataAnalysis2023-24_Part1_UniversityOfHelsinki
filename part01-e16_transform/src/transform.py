#!/usr/bin/env python3

def transform(s1, s2):
    L = []
    L1 = list(map(int,s1.split()))
    L2 = list(map(int,s2.split()))
    L = [a*b for a,b in zip(L1,L2)]
    return L

def main():
    print(transform("1 5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
