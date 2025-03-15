#86. Partition List
'''
https://leetcode.com/problems/partition-list/

Thought process:
keep track of the latest smallest node and the latest largest node and toggle between the two
latestSmall node is set to dummy at first and large is set to None
when we find the node greater than x, we set latest large value to this node and move on
if we find something smaller than x, we append that next to our current small value, update the current small value to new one and go on
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        if not head:
            return None
        mostRecentLargeValue = None
        mostRecentSmallValue = dummy
        curr = head
        while(curr):
            if curr.val<x:
                if mostRecentLargeValue == None:
                    mostRecentSmallValue = curr
                    curr = curr.next
                else:
                    smallNext = mostRecentSmallValue.next
                    mostRecentSmallValue.next = curr
                    mostRecentSmallValue = mostRecentSmallValue.next
                    currNext = curr.next
                    curr.next = smallNext
                    curr = currNext
                    mostRecentLargeValue.next = curr
            else:
                mostRecentLargeValue = curr
                curr = curr.next
        return dummy.next