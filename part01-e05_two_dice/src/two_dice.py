#!/usr/bin/env python3

def main():
    i = 1
    j = 1
    while i < 7:
        while j < 7:
            if i+j == 5:
                print(f"({i},{j})") 
            j += 1
        j = 1
        i += 1  

if __name__ == "__main__":
    main()
