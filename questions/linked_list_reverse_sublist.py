"""
Problem: Reverse Sub-list

Reverse a subsection of a singly linked list, given the head of the list and two positions 'p' and 'q'.

Function Signature:
def reverse_sublist(head: ListNode, p: int, q: int) -> ListNode:

Inputs:
    - head (ListNode): The head node of the singly linked list, with each node containing an integer value.
    - p (int): Starting position (1-based) of the sublist that needs to be reversed.
    - q (int): Ending position (1-based) of the sublist that needs to be reversed.
    
Returns:
    - ListNode: The head of the modified linked list after reversing the sublist.

Notes:
    - The linked list will have at least one element.
    - Both 'p' and 'q' will be valid positions in the linked list, with 1 <= p < q <= length of the linked list.

Examples:

1. Input: [1 -> 2 -> 3 -> 4 -> 5], p = 2, q = 4
   Output: [1 -> 4 -> 3 -> 2 -> 5]
   Explanation: The sublist from position 2 to 4 ([2 -> 3 -> 4]) is reversed to become [4 -> 3 -> 2].

2. Input: [1 -> 2 -> 3 -> 4 -> 5], p = 1, q = 5
   Output: [5 -> 4 -> 3 -> 2 -> 1]
   Explanation: The entire list is reversed.

3. Input: [1 -> 2], p = 1, q = 2
   Output: [2 -> 1]
   Explanation: The whole list with two elements is reversed.

Hints:
    - To reverse the sublist, you may need to first navigate to the 'p-1'th node.
    - Remember to adjust the 'next' pointers appropriately to ensure the reversed sublist integrates correctly with the rest of the list.

Tags:
    - LinkedList
    - Two Pointers
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_sublist(head: ListNode, p: int, q: int) -> ListNode:
    if (p == q):
        return head
    if p==1:
        pred=None
    i=1
    member=head
    while(member and i<q+1):
        if i<p:
            pred=member
            
        elif i == p:
            start=member
        elif i==q:
            end=member
            succ=member.next
    
        member=member.next
        i+=1
    
    
    
    end.next=None
    prec = None
    
    curr = start
   
    while (curr):
        temp = curr.next
        curr.next = prec
        #copy error
        prec = curr
        curr = temp
        
    #BRACKET
    if pred:
        pred.next = end
   
    # If starting position was head
    else:
        head = end
   
    start.next = succ
    member=head

    return head
        
    
    
    
