from services.file_service import (
    file_service as default_file_service
)
from math import ceil, floor


class LZWService:
    """Class responsible for the logic of the Lempel-Ziv-Welch
    compression algorithm.
    """

    def __init__(self, file_service=default_file_service):
        """Class constructor

        Args:
            file_service (FileService, optional): File Service, gives
                                                  functions for file handling.
        Defaults to default_file_service.
        """
        self._file_service = file_service

    def compress(self, file):
        """Main funtion of the Lempel-Ziv-Welch compression algorithm.
        Initializes a dictionary containing all the ASCII symbols. As it
        processes the input, it will update the dictionary with new words.

        Args:
            file (file): Input file
        Returns:
            boolean: True if compression successful
        """
        BYTE_LEN = 12
        MAX_DICT_SIZE = pow(2, BYTE_LEN)  # 4096
        content = self._file_service.get_file_contents(file)
        result = []
        code_dict_size = 256
        code_dict = {chr(i): i for i in range(code_dict_size)}
        prev = ""
        for c in content:
            if code_dict_size >= MAX_DICT_SIZE:
                code_dict_size = 256
                code_dict = {chr(i): i for i in range(code_dict_size)}
            if prev + c in code_dict:
                prev = prev + c
            else:
                result.append(code_dict[prev])
                code_dict[prev + c] = code_dict_size
                code_dict_size += 1
                prev = c
        if prev:
            result.append(code_dict[prev])
        bytes = self._format_int_list_to_bytes(result, BYTE_LEN)

        return self._file_service.write_bin_file_from_bytes(file, bytes)

    def decompress(self, file):
        """Lempel-Ziv-Welch decoding algorithm.
        Initializes the code dictionary with all ASCII symbols and
        expands it as it reads the input. Using the dictionary, the algorithm
        decodes the content of a binary file into a string
        and writes a text file.

        Args:
            file (file): An LZW encoded binary file

        Returns:
            boolean: True if decompression successful
        """
        BYTE_LEN = 12
        MAX_DICT_SIZE = pow(2, BYTE_LEN)  # 4096

        content = self._file_service.get_bin_file_contents(file)
        data_list = self._format_bytes_to_int_list(content, BYTE_LEN)

        code_dict_size = 256
        code_dict = {i: chr(i) for i in range(code_dict_size)}
        result = ""
        prev = chr(data_list.pop(0))
        result += prev
        for key in data_list:
            if code_dict_size >= MAX_DICT_SIZE:
                code_dict_size = 256
                code_dict = {i: chr(i) for i in range(code_dict_size)}

            if key in code_dict:
                value = code_dict[key]
            elif key == code_dict_size:
                value = prev + prev[0]
            else:
                return False
            result += value
            code_dict[code_dict_size] = prev + value[0]
            code_dict_size += 1

            prev = value

        return self._file_service.write_text_file(file, result)

    def _format_bytes_to_int_list(self, content, BYTE_LEN):
        """Formats bytes of certain length into an int list format.

        Args:
            content (bytes): Input bytes
            BYTE_LEN (int): Number of bits in the bytes

        Returns:
            list: list containing integers
        """
        bits = bin(int.from_bytes(content, 'big'))[2:].zfill(len(content) * 8)
        n_extended_bytes = floor(len(bits) / BYTE_LEN)
        bits = bits[-n_extended_bytes * BYTE_LEN:]
        data_list = [int(bits[i*BYTE_LEN:(i+1)*BYTE_LEN], 2)
                     for i in range(n_extended_bytes)]

        return data_list

    def _format_int_list_to_bytes(self, content, BYTE_LEN):
        """Formats an int list into bytes of certain length.

        Args:
            content (list): list containing integers
            BYTE_LEN (int): Number of bits in the bytes

        Returns:
            bytes: Output bytes
        """
        bits = ''.join([bin(i)[2:].zfill(BYTE_LEN) for i in content])
        bytes = int(bits, 2).to_bytes(ceil(len(bits) / 8), 'big')

        return bytes


lzw_service = LZWService()
