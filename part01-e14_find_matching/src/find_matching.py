#!/usr/bin/env python3

def find_matching(L, pattern):
    l = []
    i = 0
    for count, ele in enumerate(L):
        if(pattern in ele):
            l.append(count)
    return l

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

    pass

if __name__ == "__main__":
    main()
