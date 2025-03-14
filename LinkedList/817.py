#817. Linked List Components
'''
https://leetcode.com/problems/linked-list-components/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        setNums = set(nums)
        curr = head
        comp = 0
        isInLL = 0
        while(curr):
            if curr.val in setNums:
                if isInLL == 0:
                    comp+=1
                    isInLL = 1
            else:
                isInLL = 0
            curr = curr.next
        return comp