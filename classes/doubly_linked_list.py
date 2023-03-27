#!/usr/bin/python3

class Node():
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


class LinkedList():
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

    def append(self, value: int) -> None:
        """
        Inserts a new node at the beginning of the linked list.

        Parameters:
        value (int): the value of the new node to be inserted.

        Returns: None.

        Raises:
        ValueError: if the value passed as parameter is not an integer or float.
        """
        if not isinstance(value, (int, float)) and value is not None:
            raise ValueError("Value must be an integer")

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next_node = self.head
        self.head = new_node
        new_node.next_node.prev_node = new_node

    def pop(self) -> int:
        node_to_pop = self.tail
        number_to_pop = node_to_pop.data
        self.tail = node_to_pop.prev_node
        del node_to_pop
        return number_to_pop


    def append_at_final(self, value: int) -> None:
        """
        Inserts a new node at the end of the linked list.

        Parameters:
        value (int): the value of the new node to be inserted.

        Returns: None.

        Raises:
        ValueError: if the value passed as parameter is not an integer or float.
        """
        if not isinstance(value, (int, float)) and value is not None:
            raise ValueError("Value must be an integer")

        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return


        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node

    def popleft(self) -> int:
        node_to_pop = self.head
        number_to_pop = node_to_pop.data
        self.head = node_to_pop.next_node
        del node_to_pop
        return number_to_pop
        

    def print(self) -> None:
        """
        Prints the linked list from the beginning to the end.

        Parameters: None.

        Returns: None.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next_node

    def print_rev(self) -> None:
        """
        Prints the linked list from the end to the beginning.

        Parameters: None.

        Returns: None.
        """
        current = self.tail

        while current:
            print(current.data)
            current = current.prev_node
