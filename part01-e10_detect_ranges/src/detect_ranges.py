#!/usr/bin/env python3

def detect_ranges(L):
    L2 = sorted(L)
    LF = []
    i = 0
    while(i < len(L2)):
        if(L2[i] + 1 in L2):
            j = i
            while L2[j] + 1 in L2:
                j += 1
            LF.append((L2[i],L2[j] + 1))
            i = j
        else:
            LF.append(L2[i])
        i += 1
    return LF

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(sorted(L))
    print(result)

if __name__ == "__main__":
    main()
