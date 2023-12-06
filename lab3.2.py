class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result

input_list = [1, 1, 2]
linked_list = list_to_linked_list(input_list)
result_linked_list = delete_duplicates(linked_list)
result_list = linked_list_to_list(result_linked_list)
print(result_list)
