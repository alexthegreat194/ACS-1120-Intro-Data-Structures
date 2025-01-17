#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        
        if self.is_empty():
            return 0
        
        nodes = 0
        current = self.head
        while current is not None:
            current = current.next
            nodes += 1
            
        return nodes


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        # TODO: Else append node after tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def _previous(self, node):
        '''Returns the previous node given a node'''
        current = self.head
        while current is not None:
            if current.next is node:
                return current
            current = current.next
        raise ValueError(f'Node {node} not exist')

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        if not self.find(item) or self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        
        if self.head.data == item and self.tail.data == item:
            self.head = None
            self.tail = None
            return
        
        if self.head.data == item:
            self.head = self.head.next
            return
        
        if self.tail.data == item:
            self.tail = self._previous(self.tail)
            self.tail.next = None
            return
        
        current = self.head
        while current is not None:
            if current.data == item:
                self._previous(current).next = current.next
                return
            current = current.next
        
        raise Exception('Something aint right')

    def find_if_matches(self, matching_function):
        """Return an item from this linked list if it is present."""
        node = self.head
        while node is not None:
            if matching_function(node.data): 
                return node.data
            node = node.next
        return None 

if __name__ == "__main__":
    ll = LinkedList(['A', 'B', 'C'])
    ll.delete('B')
    print(ll)