# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def insert(root, item):
    temp = ListNode(item)
    
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
    
    return root
def display(root):
    while (root != None) :
        print(root.val, end = " ")
        root = root.next
        
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
    
    return root
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        pre = dummy
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 is not None else list2
        return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]

l1 = arrayToList(list1, len(list1))
l2 = arrayToList(list2, len(list2))

display(l1)
display(l2)

s = Solution()
print()
print(display(s.mergeTwoLists(l1, l2)))