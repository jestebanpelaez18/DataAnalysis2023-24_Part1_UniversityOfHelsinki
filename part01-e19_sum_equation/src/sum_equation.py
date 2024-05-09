#!/usr/bin/env python3

def sum_equation(L):
    from functools import reduce
    result = reduce(lambda x,y:x+y, L, 0)
    s = [str(x) for x in L]
    if(len(s) == 0):
        s = "0"
    else:
        s = " + ".join(s)
    s1 = s + " = " + str(result)
    return s1

def main():
    print(sum_equation([1,2,3]))
    print(sum_equation([]))
    pass

if __name__ == "__main__":
    main()
