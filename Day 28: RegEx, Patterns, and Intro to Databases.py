#!/bin/python3

import math
import os
import random
import re
import sys

def extract_gmail_users(data):
    gmail_users = []
    for row in data:
        match = re.match(r'\b[a-zA-Z0-9._%+-]+@gmail\.com\b', row[1])
        if match:
            gmail_users.append(row[0])
    return sorted(gmail_users)

if __name__ == '__main__':
    N = int(input().strip())
    data = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        data.append((firstName, emailID))
        
    for name in extract_gmail_users(data):
        print(name)
