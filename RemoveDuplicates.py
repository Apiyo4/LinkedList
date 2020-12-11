# Remove Dups: Write code to remove duplicates from an unsorted linked list.
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node 
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, new_node):
        self.new_node = new_node
class ListNode:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail
    
    def remove_node(self, incoming_value):
        current = self.head
        value = self.head.next_node.value

        while current:
            if value == incoming_value:
                pass
