#!/usr/bin/python3
"""
Module Name: 
doubly_linked_list

Module Description:
This module contains two class to manage a double linked list

Module Classes:
- Node
- LinkedList

Module Attributes:
- None
"""

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data: int, next_node=None, prev_node=None) -> None:
        """
        Initializes a new instance of the Node class.

        Parameters:
        data (int): the value of the node.
        next_node (Node, optional): the next node in the linked list. Defaults to None.
        prev_node (Node, optional): the previous node in the linked list. Defaults to None.

        Returns: None.
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    """
    Represents a doubly linked list
    """
    def __init__(self, head=None, tail=None) -> None:
        """
        Initializes a new instance of the LinkedList class.

        Parameters:
        head (Node, optional): the head node of the linked list. Defaults to None.
        tail (Node, optional): the tail node of the linked list. Defaults to None.

        Returns: None.
        """
        self.head = head
        self.tail = tail

    def append_at_final(self, node_value: int) -> None:
        """
        Inserts a new node at the beginning of the linked list.

        Parameters:
        value (int): the value of the new node to be inserted.

        Returns: None.

        Raises:
        ValueError: if the value passed as parameter is not an integer or float.
        """
        new_node = Node(node_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next_node = self.head
        self.head = new_node
        new_node.next_node.prev_node = new_node

    def append(self, node_value: int) -> None:
        """
        Inserts a new node at the end of the linked list.

        Parameters:
        value (int): the value of the new node to be inserted.

        Returns: None.

        Raises:
        ValueError: if the value passed as parameter is not an integer.
        """
        new_node = Node(node_value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node

    def add(self, node_value):
        """
        Adds a new node with the given value after the head node.

        Parameters:
        value (int): The value of the new node to be inserted.

        Returns: None.
        """
        new_node = Node(node_value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.head.next_node is None:
            # If there is only one node in the list, add new node after the head
            new_node.prev_node = self.head
            self.head.next_node = new_node
            self.tail = new_node
        else:
            # If there are more than one nodes in the list, add new node after the head
            new_node.next_node = self.head.next_node
            new_node.prev_node = self.head
            self.head.next_node.prev_node = new_node
            self.head.next_node = new_node

    def swap(self) -> None:
        """
        Swaps the positions of the head node and its next node.

        Returns: None.
        """
        if self.head.next_node is None:
            # If there is only one node in the list, do nothing
            return
        elif self.head.next_node.next_node is None:
            # If there is only two nodes in the list
            node = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            self.head.next_node = node
            node.prev_node = self.head
            node.next_node = None
        else:
            # If there are more than two nodes in the list
            node = self.head
            self.head = self.head.next_node
            node.next_node = self.head.next_node
            node.prev_node = self.head
            self.head.next_node.prev_node = node
            self.head.next_node = node

    def pop(self) -> int:
        """
        Removes and returns the value of the last node in the linked list.

        Returns:
        int: The value of the last node in the linked list.

        Raises:
        IndexError: If the linked list is empty.
        """
        node_to_pop = self.tail
        number_to_pop = node_to_pop.data
        self.tail = node_to_pop.prev_node
        if self.tail:
            self.tail.next_node = None
        else:
            self.head = None
        del node_to_pop
        return number_to_pop

    def popleft(self) -> int:
        """
        Removes and returns the value of the first node in the linked list.

        Returns:
        int: The value of the first node in the linked list.

        Raises:
        IndexError: If the linked list is empty.
        """
        node_to_pop = self.head
        number_to_pop = node_to_pop.data
        self.head = node_to_pop.next_node
        del node_to_pop
        return number_to_pop

    def print(self) -> None:
        """
        Prints the linked list from the beginning to the end.

        Returns: None.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next_node

    def print_rev(self) -> None:
        """
        Prints the linked list from the end to the beginning.

        Returns: None.
        """
        current = self.tail

        while current:
            print(current.data)
            current = current.prev_node

    def pint(self) -> None:
        """
        Prints the value of the head node.

        Returns: None.
        """
        print(self.head.data)

    def to_dict(self) -> dict:
        """
        Converts the linked list to a dictionary.

        Returns:
        dict: the dictionary representation of the linked list.
        """
        dict_list = []
        current = self.head
        while current:
            dict_list.append(current.data)
            current = current.next_node
        return {"data": dict_list}

    def save(self) -> None:
        """
        Saves the linked list into the storage defined by the user.
        """
        from .__init__ import storage

        dict_list = self.to_dict()
        storage.save(dict_list)

    def reload(self) -> None:
        """
        Reload the information
        """
        from .__init__ import storage
        data = storage.reload()

        if data is not None:
            for value in list(data.values())[0]:
                self.append(value)
