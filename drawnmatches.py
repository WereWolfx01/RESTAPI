#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
import requests
import json

def getNumDraws(year):
    total_draws = 0
    
    for i in range(0,12):
        url = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(year, i)
        response = requests.get(url)
        result = json.loads(response.content)
        total_draws += result['total']
        
    return total_draws
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
