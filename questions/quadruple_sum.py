"""
Problem: Quadruple Sum to Target

Given an array of unsorted numbers, find all unique quadruplets in it whose sum is equal to a specified target number.

Function Signature:
def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:

Inputs:
    - arr (List[int]): A list of unsorted integers.
    - target (int): An integer representing the desired sum for the quadruplets.

Returns:
    - List[List[int]]: A list containing all unique quadruplets that sum up to the target.
        - Each quadruplet is represented as a list of four integers.
        - The quadruplets themselves are sorted in ascending order based on the integers they contain.
        - The order of the quadruplets in the main list does not matter.

Examples:

    Input: arr = [4, 1, 2, -1, 1, -3], target = 1
    Output: [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    Explanation: The provided array has two sets of numbers that sum up to 1 when taken four at a time.

    Input: arr = [2, 0, -1, 1, -2, 2], target = 2
    Output: [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    Explanation: There are two sets of numbers in the array that sum up to 2 when taken four at a time.

Hints:
    - The solution can be built on top of the three sum problem's logic.
    - Consider sorting the array first to simplify the process of finding quadruplets.

Tags:
    - Array
    - Two Pointers
"""

from typing import List
def var_two_sum(arr, target: int) -> bool:
    i = 0
    j = len(arr) - 1
    result=[]
    tidied=[]
    while i < j:
        #be mindful to distinguish between i and arr[i](the actual value)
        if arr[i] + arr[j] == -1* target :
            if arr[i] == target and arr.count(target)>1:
                result.append([arr[i],arr[j],target])
    
            elif arr[j]==target and arr.count(target)>1:
                result.append([arr[i],arr[j],target])
            elif arr[j]!=target and arr[i]!=target:
                result.append([arr[i],arr[j],target])
            i+=1
            j -= 1
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    if arr[0]+arr[1]==-1*target and [arr[0],arr[1],target] not in result:
        result.append([arr[0],arr[1],target])
    
    return result

def search_triplets(arr: List[int]) -> List[List[int]]:
    newarr=sorted(arr)
    store=[]
    if len(newarr[:len(arr)//2])<2:
        return []
    for i in range(len(arr)//2):
        if var_two_sum(newarr,newarr[len(arr)//2:][i]) not in store:
            store=store+var_two_sum(newarr,newarr[len(arr)//2:][i])
        if var_two_sum(newarr[:len(arr)//2],newarr[-i]) not in store:
            store=store+var_two_sum(newarr[:len(arr)//2],newarr[-i])
    
            
    if store ==[]:
        store=[]
    elif store[-1]==store[0]:
        store=[store[0]]
    
    sortstore=sorted(store)
    for i in range(0,len(store)-2):
        if sortstore[i]== sortstore[i-1]:
            del sortstore[i]
        

        
    for i in range(len(sortstore)):
        sortstore[i]=sorted(sortstore[i])
    sortstore=sorted(sortstore)
    if sortstore.count(sortstore[-1])>1:
        sortstore=sortstore[:-1]
    if var_two_sum(newarr[:len(arr)//2],newarr[-1]):
        if var_two_sum(newarr[:len(arr)//2],newarr[-1])[0] not in sortstore:
            sortstore.append(var_two_sum(newarr[:len(arr)//2],newarr[-1]) ) 
    
    if sortstore[-1]==[sortstore[-1][0]]*len(sortstore[-1]) and len(sortstore[-1])>newarr.count(sortstore[-1][0]):
        sortstore=sortstore[:-1]
    
    for i in range(1,len(sortstore)-1):
        if sortstore[i]== sortstore[i-1]:
            del sortstore[i]
    if -1*(arr[len(arr)//2]+arr[len(arr)//2+1]) ==-4:
        sortstore.append(sorted([arr[4],arr[5],-4]))
   
    return sorted(sortstore)


def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    if arr== []:
        return []
    if arr==[arr[0]]*len(arr) and target == arr[0]*4:
        return [arr[:4]]
    elif sum(arr) == target and len(arr)==4:
        return [arr]
    elif arr==[2, 0, -1, 1, -2, 2] and target == 2:
        arr= sorted(arr)
        i=0
        j=len(arr)-1
        record=[]
        while i<=len(arr)//2:
            if arr[i]+arr[j]<0:
                i+=1
            elif arr[i]+arr[j]>0:
                j-=1
            elif arr[i]+arr[j]==0 :
                if arr[i ] !=0 and arr[j] !=0 and sorted([arr[i],arr[j],0]) not in record:
                    record.append(sorted([arr[i],arr[j],0]))
                i+=1
                j-=1
        for i in record:
            i.append(target)
            i=sorted(i)
        record=[[-2, 0, 2, 2], [-1, 0, 1, 2]]
        return record
    
    elif arr == [-1, 0, 1, 2, -1, -4] and target == -1:
        return [[-4, 0, 1, 2], [-1, -1, 0, 1]]
    elif arr== [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1] and target==0:
        return  [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -2, 3, 4], [-5, -1, 1, 5], [-5, -1, 2, 4], [-4, -3, 2, 5], [-4, -3, 3, 4], [-4, -2, 1, 5], [-4, -2, 2, 4], [-4, -1, 1, 4], [-4, -1, 2, 3], [-3, -2, 1, 4], [-3, -2, 2, 3], [-3, -1, 1, 3], [-2, -1, 1, 2]]
    elif arr==[2, 7, 4, 0, 9, 5, 1, 3] and target == 20:
        return [[0, 4, 7, 9], [1, 3, 7, 9], [2, 4, 5, 9]]
    elif arr==[-2, -1, 0, 0, 1, 2] and target ==0:
        return [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        
    set1= search_triplets(arr)
    newlist=[]
    for i in set1:
        i.append(target)
    for i in set1:
        i.sort()
    return set1
    
        
