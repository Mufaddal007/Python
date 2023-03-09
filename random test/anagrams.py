#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    arr1=[]
    arr2=[]
    fin=[]
    for x in dictionary:
        i=list(x)
        i.sort()
        
        arr1.append(i)
        
    for x in query:
        i=list(x)
        i.sort()
        
        arr2.append(i)
    for x in arr2:
        c=arr1.count(x)
        fin.append(str(c))
    return fin
   

dictionary_count = int(input().strip())

dictionary = []

for _ in range(dictionary_count):
    dictionary_item = input()
    dictionary.append(dictionary_item)

query_count = int(input().strip())

query = []

for _ in range(query_count):
    query_item = input()
    query.append(query_item)

result = stringAnagram(dictionary, query)

# function to check if two strings are 
# anagram or not 
def check(s1, s2): 
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)): 
		print("The strings are anagrams.") 
	else: 
		print("The strings aren't anagrams.")		 
		
# driver code 
s1 ="listen"
s2 ="silent"
check(s1, s2) 
