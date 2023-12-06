class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None
    prev = None
    current = second_half

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    first_half = head
    second_half = prev

    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        first_half.next = second_half
        second_half.next = temp1
        first_half = temp1
        second_half = temp2

    return head

def list_to_linked_list(lst):
    if not lst:
        return None
    nodes = [ListNode(val) for val in lst]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

input_list1 = [1, 2, 3, 4]
linked_list1 = list_to_linked_list(input_list1)
reorder_list(linked_list1)
result1 = linked_list_to_list(linked_list1)
print(result1)  

input_list2 = [1, 2, 3, 4, 5]
linked_list2 = list_to_linked_list(input_list2)
reorder_list(linked_list2)
result2 = linked_list_to_list(linked_list2)
print(result2)  
