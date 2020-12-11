#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (34.73%)
# Likes:    9931
# Dislikes: 2499
# Total Accepted:    1.7M
# Total Submissions: 4.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = ListNode()
        nx = ans
        pre = 0

        while l1 != None or l2 != None:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + pre

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            pre = v//10
            v %= 10
            
            nx.val = v
            bfr = nx
            nx.next = ListNode()
            nx = nx.next

        nx.val = pre
        if nx.val == 0:
            bfr.next = None

        return ans

# @lc code=end

