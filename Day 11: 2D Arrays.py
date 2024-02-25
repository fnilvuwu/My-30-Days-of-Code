#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # the smallest possible value is -9*7 = 63
    max_sum = -63

    for i in range(4):
        for j in range(4):
            current_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if current_sum > max_sum:
                max_sum = current_sum
                
    print(max_sum)