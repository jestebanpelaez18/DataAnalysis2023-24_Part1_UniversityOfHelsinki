#!/usr/bin/env python3
def triple(i):
        triple = i*3
        return triple
def square(i):
        sq = i**2
        return sq
def main():
    for i in range(1,11):
        trip = triple(i)
        sqr = square(i)
        if (sqr > trip):
            break
        else:      
            print(f"triple({i})=={trip} square({i})=={sqr}")

if __name__ == "__main__":
    main()
