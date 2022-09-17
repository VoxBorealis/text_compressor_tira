import unittest
from pathlib import Path
from services.huffman_service import HuffmanService

class TestHuffmanService(unittest.TestCase):
    def setUp(self):
        self.file = Path(__file__).parents[1].joinpath('data').joinpath('test.txt')
        self.huffman_service = HuffmanService(self.file)
    
    def test_calculate_frequency(self):
        test_list = []
        test_list.append((4, "a"))
        test_list.append((3, "b"))
        test_list.append((2, "c"))
        test_list.append((1, "d"))

        char_freq_list = self.huffman_service._calculate_frequency()
        self.assertEqual(test_list, char_freq_list)
