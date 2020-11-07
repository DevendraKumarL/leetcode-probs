'''
    Problem:
    Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

    Example 1:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Solution1: (Slow & not well written):
        -have a 3rd new empty list l3
        -loop through l1 and l2 until we reach end of one of the lists using pointers starting at head
        -compare item in l1 and l2
            -if l1==l2, add both to l3
            -else if l1<l2, add from l1 to l3, move forward pointer in l1
            -else, add from l2 to l3, move forward pointer in l2
        -then loop on l1 until we reach end and items to l3
        -then loop on l2 until we reach end and items to l3
        -l3 is the new merged sorted list
     
    Solution2: (Fast & simpler):
        -have a 3rd new empty list l3
        -loop through l1 and l2 until we reach end of one of the lists
        -compare item in l1 and l2
            -if l1<l2, assign l1 to l3.next, move forward l1 to l1.next
            -else, assign l2 to l3.next, move forward l2 to l2.next
        -now l3.next = l1 == EndOfList ? l2 : l1
        -return l3.next the merged list
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        mergedList = ListNode()
        p3 = None
        while (p1 != None and p2 != None):
            if (p1.val == p2.val):
                n2 = ListNode(p2.val)
                n1 = ListNode(p1.val, n2)
                if p3 == None:
                    p3 = n1
                    mergedList = p3
                else:
                    p3.next = n1
                p3 = n2
                p1 = p1.next
                p2 = p2.next
            elif (p1.val < p2.val):
                n1 = ListNode(p1.val)
                if p3 == None:
                    p3 = n1
                    mergedList = p3
                else:
                    p3.next = n1
                p3 = n1
                p1 = p1.next
            else:
                n1 = ListNode(p2.val)
                if p3 == None:
                    p3 = n1
                    mergedList = p3
                else:
                    p3.next = n1
                p3 = n1
                p2 = p2.next
        while (p1 != None):
            n1 = ListNode(p1.val)
            if p3 == None:
                p3 = n1
                mergedList = p3
            else:
                p3.next = n1
            p3 = n1
            p1 = p1.next
        while (p2 != None):
            n1 = ListNode(p2.val)
            if p3 == None:
                p3 = n1
                mergedList = p3
            else:
                p3.next = n1
            p3 = n1
            p2 = p2.next
        return mergedList

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        ml = ListNode()
        p3 = ml
        while (l1 != None and l2 != None):
            if (l1.val < l2.val):
                p3.next = l1
                l1 = l1.next
            else:
                p3.next = l2
                l2 = l2.next
            p3 = p3.next
        if l1 == None:
            p3.next = l2
        else:
            p3.next = l1
        return ml.next;