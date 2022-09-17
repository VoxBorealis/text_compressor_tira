from queue import PriorityQueue
from entities.node import Node

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


huffman_service = HuffmanService()
