#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

import requests
import json

def getTotalGoals(team, year):
    # Write your code here
    url1 = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team1="+ team
    url2 = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team2="+ team
    response1 = requests.get(url1)
    result1 = json.loads(response1.content)
    response2 = requests.get(url2)
    result2 = json.loads(response2.content)
    
    current1_pg = 1
    total1_pg = result1['total_pages']
    current2_pg = 1
    total2_pg = result2['total_pages']
    
    total_goals = 0
    while current1_pg <= total1_pg:
        url1 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1={1}&page={2}".format(year, team, current1_pg)
        response1 = requests.get(url1)
        result1 = json.loads(response1.content)
        
        for i in result1['data']:
            total_goals += int(i['team1goals'])
        current1_pg += 1
        
    while current2_pg <= total2_pg:
        url2 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team2={1}&page={2}".format(year, team, current2_pg)
        response2 = requests.get(url2)
        result2 = json.loads(response2.content)
            
        for i in result2['data']:
            total_goals += int(i['team2goals'])
        current2_pg += 1    
        
    return total_goals
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
