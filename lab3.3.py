class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

def list_to_linked_list(lst, pos):
    if not lst:
        return None
    nodes = [ListNode(val) for val in lst]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]

input_list1 = [3, 2, 0, -4]
pos1 = 1
linked_list1 = list_to_linked_list(input_list1, pos1)
result1 = has_cycle(linked_list1)
print(result1) 

input_list2 = [1, 2]
pos2 = 0
linked_list2 = list_to_linked_list(input_list2, pos2)
result2 = has_cycle(linked_list2)
print(result2)

input_list3 = [1]
pos3 = -1
linked_list3 = list_to_linked_list(input_list3, pos3)
result3 = has_cycle(linked_list3)
print(result3) 
