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
    
    def compress(self):
        """The main function of the Huffman Encoding

        Returns:
            boolean: True if successfully compressed
        """
        char_freq = self._calculate_frequency()
        tree = self._build_tree(char_freq)
        code_table = {}
        self._build_code_table(tree, "", code_table)
        return self._encode_contents(code_table)

    def decode(self, file):
        """Decodes the contents of a binary file and writes
        a new text file.

        Args:
            file (file): A binary file
        
        Returns:
            boolean: True if successfully decompressed
        """
        code_table = file_service.get_code_table(file)
        with open(file, 'rb') as fh:
            content = fh.read()
        decoded_string = ""
        buffer = ""
        for byte in content[:-1]:
            byte_as_str = (format(byte, '08b'))
            for bit in byte_as_str:
                buffer = buffer + bit
                try:
                    decoded_string = decoded_string + code_table[buffer]
                    buffer = ""
                except:
                    pass
        #last byte is computed separately
        last_byte = bin(content[-1])[2:]
        for bit in last_byte:
            buffer = buffer + bit
            try:
                decoded_string = decoded_string + code_table[buffer]
                buffer = ""
            except:
                pass
        
        return file_service.write_text_file(file, decoded_string)

    def _encode_contents(self, code_table):
        """Encodes the content of the original file into a binary file
        using the code table, also saves the code table to a JSON file.

        Args:
            code_table (dict): Huffman Encoding code table

        Returns:
            boolean: True if encoding successful
        """
        if file_service.write_code_table(self.file, code_table):
            encoded_but_str = ""
            for c in file_service.get_file_contents(self.file):
                encoded_but_str = encoded_but_str + code_table[c]

            return file_service.write_bin_file(
                self.file, encoded_but_str
            )
        else:
            return False

    def _calculate_frequency(self):
        """Calculates the frequency of each character using a dictionary and
        returns a list of Tuples (count (int), character (string))

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
        """Builds the Huffman tree.

        Args:
            char_freq (list): A List of each character found in the .txt file and their
            frequency as Tuples (count (int), char (string)).

        Returns:
            Node: Root Node of the Huffman Tree
        """
        tree = PriorityQueue()
        for c in char_freq:
            tree.put(Node(c))

        root = None
        while not tree.empty():
            left = tree.get()
            right = tree.get()
            parent = Node((left.value[0] + right.value[0], "node"))
            parent.left_child = left
            parent.right_child = right
            if not tree.empty():
                tree.put(parent)
            else:
                root = parent

        return root

    def _build_code_table(self, node, code, dict):
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
        self._build_code_table(node.left_child, code + "0", dict)
        self._build_code_table(node.right_child, code + "1", dict)
    

huffman_service = HuffmanService()
