class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  
            
        tail.next = list1 if list1 else list2
        return dummy.next

def build_linked_list(arr):
    """Converts a standard Python list into a Linked List."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Helper to cleanly print the linked list values."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


s = Solution()

l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])


result_head = s.mergeTwoLists(l1, l2)


print_linked_list(result_head)  
