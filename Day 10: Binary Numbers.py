#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    max_consecutive_ones = 0
    consecutive_ones = 0

    while n != 0:
        if n & 1 == 1:
            consecutive_ones += 1
            max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
        else:
            consecutive_ones = 0
        n >>= 1  # Right shift n by 1 bit

    print(max_consecutive_ones)
    
    
    
    
    
    
    
