# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:08:31 2023

@author: May50x
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    s = s.split(':')
    mid=s[2][2:]
    first_hour = int(s[0])
    
    if first_hour == 12 and mid == 'AM':
        elementos = ['00',s[1],s[2][:2]]
        time = ':'.join(elementos)
        
    elif first_hour != 12 and mid =='PM':
        first_hour += 12
        elementos = [str(first_hour),s[1],s[2][:2]]
        time = ':'.join(elementos)
    
    else:
        elementos = [s[0],s[1],s[2][:2]]
        time = ':'.join(elementos)
    
    return time
    

s = input()

result = timeConversion(s)

print(result + '\n')

