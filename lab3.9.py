class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    before.next = after_head.next
    after.next = None  

    return before_head.next

# Приклад:
head1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))) 
result1 = partition(head1, 3)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next

print()

head2 = ListNode(2, ListNode(1))
result2 = partition(head2, 2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
