#!/usr/bin/env python3

def positive_list(L):
    L1 = []
    L1 = list(filter(lambda x : x > 0, L))
    return L1

def main():
    print(positive_list([2,-2,0,1,-7]) )
    pass

if __name__ == "__main__":
    main()
