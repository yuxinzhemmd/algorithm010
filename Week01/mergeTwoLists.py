# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #1.迭代，一个节点一个节点的比较，O（n+m）
        thread = ListNode(-1)
        pre = thread
        while(l1 and l2):
            if(l1.val < l2.val):
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next
        pre.next = l1 if l1 is not None else l2
        return thread.next

        #2.递归，O（n+m）
        # if l1 == None or l2 == None:
        #     return l1 if l1 is not None else l2
        # if(l1.val < l2.val):
        #     l1.next = self.mergeTwoLists(l1.next,l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1,l2.next)
        #     return l2