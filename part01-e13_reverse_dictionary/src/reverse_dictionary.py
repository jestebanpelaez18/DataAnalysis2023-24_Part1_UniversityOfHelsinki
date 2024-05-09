#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    for key,value in d.items():
        for item in value:
            if item not in rd:
                rd[item] = [key]
            else:
                rd[item].append(key)
    return rd

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    rd =  reverse_dictionary(d)
    print(rd)

if __name__ == "__main__":
    main()
