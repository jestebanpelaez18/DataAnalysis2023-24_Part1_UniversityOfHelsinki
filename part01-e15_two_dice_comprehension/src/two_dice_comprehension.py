#!/usr/bin/env python3

def main():
    L = [ (i,j) for i in range(1,7) for j in range(1,7) if i+j == 5]
    it = 0
    while(it < len(L)):
        print(L[it])
        it += 1
    pass

if __name__ == "__main__":
    main()
