#!/usr/bin/env python3


def main():
    i = 1
    j = 1
    while i < 11:
        while j < 11:
            print('{:4d}'.format(i*j),end = '')
            j+=1
        print("")
        j = 1
        i+=1

if __name__ == "__main__":
    main()
