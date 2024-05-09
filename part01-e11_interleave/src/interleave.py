#!/usr/bin/env python3

def interleave(*lists):
    L2= []
    L2 = list(zip(*lists))
    L = []
    j = 0
    while j < len(L2):
        for i in L2[j]:
            L.append(i)
        j += 1
    return L

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
