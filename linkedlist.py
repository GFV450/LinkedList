#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None

        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        items_list = []
        node = self.head

        while node is not None:
            items_list.append(node.data)
            node = node.next

        return items_list

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)

        if self.tail is not None:
            tail_node = self.tail
            self.tail.next = tail_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)

        if self.head is not None:
            head_node = self.head
            self.head.next = head_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current_node = self.head

        if current_node.data == item:

            if current_node.data == self.tail.data:
                self.head = None
                self.tail = None
            else:
                self.head = current_node.next

        while current_node.next is not None:
            if current_node.next.data == item:

                if current_node.next == self.tail:
                    self.tail = current_node
                    current_node.next = None
                else:
                    current_node.next = current_node.next.next
            else:
                current_node = current_node.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current_node = self.head

        while current_node.data is not None:
            if quality(current_node.data) is True:
                return current_node.data
            else:
                current_node = current_node.next


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
