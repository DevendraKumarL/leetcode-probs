# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
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