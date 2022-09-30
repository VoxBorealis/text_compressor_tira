from logging import root
import unittest
from pathlib import Path
from services.huffman_service import HuffmanService

class TestHuffmanService(unittest.TestCase):
    def setUp(self):
        self.file = Path(__file__).parents[1].joinpath('data').joinpath('test.txt')
        self.huffman_service = HuffmanService(self.file)
        self.freq_list = self.huffman_service._calculate_frequency()
        self.root = self.huffman_service._build_tree(self.freq_list)
        self.code_table = {}
        self.huffman_service._build_code_table(self.root, "", self.code_table)
    
    def test_calculate_frequency(self):
        test_list = []
        test_list.append((4, "a"))
        test_list.append((3, "b"))
        test_list.append((2, "c"))
        test_list.append((1, "d"))

        self.assertEqual(test_list, self.freq_list)
    
    def test_build_tree(self):
        self.assertEqual(self.root.value[0], 10)
        self.assertEqual(self.root.left_child.value[0], 4)
        self.assertEqual(self.root.right_child.value[0], 6)
        self.assertEqual(self.root.left_child.right_child, None)

    def test_build_code_table(self):
        my_code_table = {
            'a': '0',
            'b': '10',
            'd': '110',
            'c': '111'
        }

        self.assertEqual(self.code_table, my_code_table)
    
    def test_encode_contents(self):
        encoded_but_str = self.huffman_service._encode_contents(self.code_table)
        my_str = "0000101010111111110"

        self.assertEqual(encoded_but_str, my_str)
