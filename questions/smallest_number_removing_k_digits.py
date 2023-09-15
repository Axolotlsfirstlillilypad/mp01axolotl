"""
Problem: Remove K Digits to Obtain Smallest Number

Given a non-negative integer represented as a string `num` and an integer `k`, 
the task is to delete `k` digits from `num` to obtain the smallest possible integer. 
Return this minimum possible integer as a string.

Function Signature:
def removeKDigits(num: str, k: int) -> str:

Parameters:
    - num (str): A string representation of the non-negative integer.
    - k (int): An integer representing the number of digits to delete from `num`.
    
Returns:
    - str: A string representation of the minimum possible integer after removing `k` digits.

Examples:

1. Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: The digits removed are 4, 3, and 2 forming the new number 1219 which is the smallest.
    
2. Input: num = "10200", k = 1
    Output: "200"
    Explanation: Removing the leading 1 forms the smallest number 200.
    
3. Input: num = "1901042", k = 4
    Output: "2"
    Explanation: Removing 1, 9, 1, and 4 forms the number 2 which is the smallest possible.

Hints: 
    - Use a stack to keep track of the digits to keep.
    - Remember to remove the leading zeros.

Tags: 
    - Stack
"""


def remove_k_digits(num: str, k: int) -> str:
    i=0
    
    limit=k
    while i <len(num)-1 and limit>0:
        if int(num[i])>int(num[i+1]) :
        #rmb syntax= replace does not actually create new string without a def
            num=num.replace(num[i], "",1)
            #must specify default number to replacae
            limit-=1
            i=-1
            #set it to -1 so our overall increment so we can use the i+=1 at the end to tap into index 0
        elif num=="".join(sorted(num)):
            num=num.replace(max(num), "",1)
            limit-=1
            i=-1

        i+=1
    return str(int(num))




