
class HuffmanService:
    """Class responsible for the logic of the Huffman compression
    """

    def __init__(self, file = None):
        """Class constructor
        """
        self.file = file
    
    def compress(self):
        """The main function of the Huffman compression. Compresses the given file..WIP

        Args:
            file (_.txt_): _A .txt file that will be compressed_
        """
        sorted = self._frequency_sort()
        print(sorted)

    def _frequency_sort(self):
        """Sorts all the characters from a text file in a dictionary based on their frequency

        Args:
            file (_.txt_): __

        Returns:
            _type_: _description_
        """
        char_dict = {}
        with open(self.file) as f:
            contents = f.read()
            print(contents)

        return char_dict

    
huffman_service = HuffmanService()
    