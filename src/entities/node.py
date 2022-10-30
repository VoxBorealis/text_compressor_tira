class Node:
    """Class responsible for the nodes in the Huffman tree
    """

    def __init__(self, value, left_child=None, right_child=None):
        """Class constructor

        Args:
            value (Tuple): Tuple containing a frequency (int) and a char (str)
            left_child (Node, optional): Left child Node of self.
                Defaults to None.
            right_child (Node, optional): Right child Node of self.
                Defaults to None.
        """
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def is_leaf(self):
        if not self.left_child or not self.right_child:
            return True

    def __eq__(self, other):
        return (self.value[0] == other.value[0])

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.value[0] < other.value[0])

    def __gt__(self, other):
        return (self.value[0] > other.value[0])

    def __le__(self, other):
        return (self.value[0] < other.value[0]) or \
            (self.value[0] == other.value[0])

    def __ge__(self, other):
        return (self.value[0] > other.value[0]) or \
            (self.value[0] == other.value[0])
