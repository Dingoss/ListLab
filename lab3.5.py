class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    node.val = node.next.val
    
    node.next = node.next.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Приклад:
head1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
print("Початковий зв'язаний список:")
print_linked_list(head1)


node_to_delete1 = head1.next
delete_node(node_to_delete1)
print("Після видалення вузла:")
print_linked_list(head1)

head2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
print("\nПочатковий зв'язаний список:")
print_linked_list(head2)

node_to_delete2 = head2.next.next
delete_node(node_to_delete2)
print("Після видалення вузла:")
print_linked_list(head2)
