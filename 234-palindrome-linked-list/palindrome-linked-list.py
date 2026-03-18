# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head):
        arr = []

        # store values
        while head:
            arr.append(head.val)
            head = head.next

        # check palindrome
        return arr == arr[::-1]