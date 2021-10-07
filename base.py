#!/usr/bin/python3

from typing import Mapping

import sys

def file_to_array (filename) :
    names = []
    with open(filename) as file :
        for line in file :
            names.append(line.split(sep=',')[0])
    return names

 

def main():

    arr = file_to_array(sys.argv[1])
    for i in arr : 
        print(i)

if __name__ == "__main__":
    main()
