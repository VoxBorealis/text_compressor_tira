from queue import PriorityQueue
from entities.node import Node
from services.file_service import file_service

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
    
    def decode(self, file):
        with open(file, 'rb') as fh:
            content = fh.read()
        print(int(content, 16))

    def compress(self):
        """The main function of the Huffman compression.
        Compresses the given file..WIP

        Args:
            file (.txt): A .txt file that will be compressed
        """
        char_freq = self._calculate_frequency()
        tree = self._build_tree(char_freq)
        code_table = {}
        self._encode_characters(tree, "", code_table)
        print(code_table)
        print(self._encode_contents(code_table))

    def _encode_contents(self, encoded_chars):
        return file_service.write_bin_file(
            self.file, encoded_chars
        )

    def _calculate_frequency(self):
        """Calculates the frequency of each character using a dictionary and
        returns an array of Tuples (count (int), character (string))

        Returns:
            list: List of each character found in the .txt file and their
            frequency as Tuples (count (int), char (string)).
        """
        char_dict = {}

        file_as_str = file_service.get_file_contents(self.file)
        for char in file_as_str:
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

        root = None
        debug_i = 0
        while not tree.empty():
            left = tree.get()
            right = tree.get()
            parent = Node((left.value[0] + right.value[0], "node"))
            parent.left_child = left
            parent.right_child = right
            print(f'i: {debug_i}, parent = {parent.value} left child: {parent.left_child.value}, right child: {parent.right_child.value}')
            debug_i = debug_i+1
            if not tree.empty():
                tree.put(parent)
            else:
                root = parent

        print(f'root: {root.value}')

        return root

    def _encode_characters(self, node, code, dict):
        """Assigns each character in the tree a code using a recursive depth-first-search algorithm.
            code string = "" at start.
            When traversing to left child, add "0"; when traversing to right, add "1".
            Upon encountering a leaf node, assign that char the code string that has been formed so far.

        Args:
            node (Node): A node of the Huffman Tree
            code (String): A string variable that is updated as the tree is traversed
            dict (dict): A dictionary of characters and their codes.
        """
        if node is None:
            return
        if node.is_leaf():
            dict[node.value[1]] = code
            return
        self._encode_characters(node.left_child, code + "0", dict)
        self._encode_characters(node.right_child, code + "1", dict)


huffman_service = HuffmanService()
