class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists

    return lists[0]

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Приклади використання:
lists1 = [ListNode(1, ListNode(4, ListNode(5))),
          ListNode(1, ListNode(3, ListNode(4))),
          ListNode(2, ListNode(6))]

result1 = merge_k_lists(lists1)
print_linked_list(result1)

lists2 = []
result2 = merge_k_lists(lists2)
print_linked_list(result2)

lists3 = [ListNode()]
result3 = merge_k_lists(lists3)
print_linked_list(result3)
