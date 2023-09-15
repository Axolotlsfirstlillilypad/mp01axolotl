"""
Problem: Remove Groups of Identical Characters

Given a string `s` and an integer `k`, the task is to remove groups of consecutive, identical characters 
from the string such that each group contains exactly `k` characters. Continue removing such groups 
until no more removals can be made. Return the resulting string after all possible removals.

Function Signature:
def removeGroups(s: str, k: int) -> str:

Inputs:
    - s (str): A string containing any characters.
    - k (int): The size of groups of identical characters to be removed.

Returns:
    - str: The modified string after removing groups of consecutive, identical characters.

Examples:

1. Input: s = "abbbaaca", k = 3
   Output: "ca"
   Explanation: Initially, the string contains "bbb". Removing it results in "aaaca". 
   Next, "aaa" is removed to leave "ca".

2. Input: s = "abbaccaa", k = 3
   Output: "abbaccaa"
   Explanation: The string doesn't have any group of 3 consecutive identical characters.

3. Input: s = "abbacccaa", k = 3
   Output: "abb"
   Explanation: "ccc" is removed first to yield "abbaaa". Then, "aaa" is removed, resulting in "abb".

Hints:
    - Consider iterating through the string to identify and remove the qualifying groups.
    - Use a loop to ensure that removals continue until no more can be made.

Tags:
    - String
"""


def remove_groups(s: str, k: int) -> str:
    record=[]
    i=0
    #checks if all indices are the same letter, then we really do not need to even process. If the length is not the same return 
    #the string
    if s == s[0]*len(s) and len(s)!=k:
        s=s
    else:
        while i < len(s):
            #must append list beforehand so that the latest iteration's character is recorded in the list,
            #otherwise the list will not be updated before processing
            record.append(s[i])
            if i<len(s)-1:
                if s[i+1]!= s[i] :
                    if len(record)==k:
                        #for some reason this avoids index error
                        s=s.replace(s[i]*k,"",1)
                        i=-1
                    record=[]
                    # case below needed to explain what happens when the triplet contains the very last index
            elif i==len(s)-1:
                if len(record)==k :
                        s=s.replace(s[i]*k,"",1)
                        i=-1
                        record=[]
            #what to do if there is nothing left in s to return  e.g"aabbcc"
            if len(s)==0:
                s=""
                break
            #Corrects a situation where removing chars leads to the entire string now having the same character.
            elif s == s[0]*len(s) and len(s)!=k:
                s=s
                break
            #increment the loop to avoid infinite iteration
            else:
                
                i+=1
    return s

