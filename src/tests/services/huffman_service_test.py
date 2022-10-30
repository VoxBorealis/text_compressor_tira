import unittest
from pathlib import Path
from services.huffman_service import HuffmanService


class FakeFileService():

    def __init__(self):
        self.path = Path(__file__).parents[1].joinpath('data')

    def write_code_table(self, file, code_table):
        if file == "":
            return False
        return True

    def get_code_table(self, file):
        my_code_table = {
            '0': 'a',
            '10': 'b',
            '110': 'd',
            '111': 'c'
        }
        return my_code_table

    def get_file_contents(self, file):
        if file == "fail":
            return file
        file = self.path.joinpath(file)
        with open(file) as f:
            contents = f.read()

        return contents

    def write_bin_file_from_bytes(self, file, bytes):
        return bytes

    def write_text_file(self, file, result):
        if file == "":
            return False
        return result

    def write_bin_file(self, file, encoded_but_str):
        if file == "fail":
            return False
        return encoded_but_str

    def get_bin_file_contents(self, file):
        if type(file) is bytes or file == "":
            return file
        file = self.path.joinpath(file)
        with open(file, 'rb') as bin_file:
            bytes_content = bin_file.read()

        return bytes_content


class TestHuffmanService(unittest.TestCase):
    def setUp(self):
        self.file = "test.txt"
        self.huffman_service = HuffmanService(FakeFileService())

    def test_calculate_frequency(self):
        test_list = []
        test_list.append((4, "a"))
        test_list.append((3, "b"))
        test_list.append((2, "c"))
        test_list.append((1, "d"))

        freq_list = self.huffman_service._calculate_frequency(self.file)

        self.assertEqual(test_list, freq_list)

    def test_build_tree(self):
        freq_list = self.huffman_service._calculate_frequency(self.file)
        root = self.huffman_service._build_tree(freq_list)

        self.assertEqual(root.value[0], 10)
        self.assertEqual(root.left_child.value[0], 4)
        self.assertEqual(root.right_child.value[0], 6)
        self.assertEqual(root.left_child.right_child, None)

    def test_build_code_table(self):
        freq_list = self.huffman_service._calculate_frequency(self.file)
        root = self.huffman_service._build_tree(freq_list)
        code_table = {}
        self.huffman_service._build_code_table(root, "", code_table)
        my_code_table = {
            'a': '0',
            'b': '10',
            'd': '110',
            'c': '111'
        }

        self.assertEqual(code_table, my_code_table)

    def test_encode_contents(self):
        my_code_table = {
            'a': '0',
            'b': '10',
            'd': '110',
            'c': '111'
        }
        encoded_but_str = self.huffman_service._encode_contents(my_code_table,
                                                                self.file)
        my_str = "0000101010111111110"

        self.assertEqual(encoded_but_str, my_str)

    def test_compression_returns_true_when_writes_successful(self):
        self.assertTrue(self.huffman_service.compress(self.file))

    def test_compression_returns_false_when_writes_fail(self):
        self.assertFalse(self.huffman_service.compress("fail"))

    def test_decode_bytes(self):
        bytes_content = bytes(b'\n\xbf\x06')
        my_code_table = {
            '0': 'a',
            '10': 'b',
            '110': 'd',
            '111': 'c'
        }
        decoded_string = self.huffman_service._decode_bytes(bytes_content,
                                                            my_code_table)

        self.assertEqual(decoded_string, "aaaabbbccd")

    def test_decompression_returns_correct_value(self):
        self.assertEqual("aaaabbbccd", self.huffman_service.
                         decompress(b'\n\xbf\x06'))
