#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i = 0
    j = 0
    while i < len(L1) or j < len(L2):
        if i == len(L1):
            L.append(L2[j])
            j += 1
        elif j == len(L2):
            L.append(L1[i])
            i += 1
        elif(L1[i] < L2[j]):
            L.append(L1[i])
            i += 1
        elif(L1[i] > L2[j]):
            L.append(L2[j])
            j += 1
    return L

def main():
    L1 = [1,3,4,10]
    L2 = [5,7,8,9]
    print(merge(L1,L2))
    pass

if __name__ == "__main__":
    main()
