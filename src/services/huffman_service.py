from queue import PriorityQueue


class HuffmanService:
    """Class responsible for the logic of the Huffman compression
    """

    def __init__(self, file=None):
        """Class constructor

        Args:
            file (.txt, optional): text file chosen by the user to be
            compressed. Defaults to None.
        """
        self.file = file

    def compress(self):
        """The main function of the Huffman compression.
        Compresses the given file..WIP

        Args:
            file (.txt): A .txt file that will be compressed
        """
        sorted = self._calculates_frequency()
        tree = self._build_tree(sorted)

    def _calculates_frequency(self):
        """Calculates the frequency of each character using a dictionary and
        returns an array of Tuples (count (int), character (string))

        Returns:
            list: List of each character found in the .txt file and their
            frequency as Tuples (count (int), char (string)).
        """
        char_dict = {}
        with open(self.file) as f:
            contents = f.read()
            print(contents)
            for char in contents:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] = char_dict[char] + 1
        char_freq_list = []

        for c in char_dict.items():
            char_freq_list.append((c[1], c[0]))

        return char_freq_list

    def _build_tree(self, char_freq):
        tree = PriorityQueue()
        for c in char_freq:
            tree.put(Node(c))

        print("--------------")

        while not tree.empty:
            print(tree.get().value)

        return tree


class Node:
    """Class responsible for the nodes in the Huffman tree
    """

    def __init__(self, value, left_child=None, right_child=None):
        """Class constructor

        Args:
            value (Tuple): Tuple containing a char and their frequency
            left_child (Node, optional): Left child Node of self.
                Defaults to None.
            right_child (Node, optional): Right child Node of self.
                Defaults to None.
        """
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

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


huffman_service = HuffmanService()
