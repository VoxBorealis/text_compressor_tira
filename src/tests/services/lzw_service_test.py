import unittest
from services.lzw_service import LZWService
from pathlib import Path


class FakeFileService():

    def __init__(self):
        self.path = Path(__file__).parents[1].joinpath('data')

    def get_file_contents(self, file):
        file = self.path.joinpath(file)
        with open(file) as f:
            contents = f.read()

        return contents

    def write_bin_file_from_bytes(self, file, bytes):
        return bytes

    def write_text_file(self, file, result):
        return result

    def get_bin_file_contents(self, file):
        if type(file) is bytes:
            return file
        file = self.path.joinpath(file)
        with open(file, 'rb') as bin_file:
            bytes_content = bin_file.read()

        return bytes_content


class TestLZWService(unittest.TestCase):
    def setUp(self):
        self.lzw_service = LZWService(FakeFileService())

    def test_compress_returns_correct_bytes(self):
        result = self.lzw_service.compress("test.txt")
        self.assertEqual(result, b'\x06\x11\x00\x06\x10b\x100c\x060d')

    def test_decompress_returns_correct_text(self):
        result = self.lzw_service.decompress("test.bin")
        self.assertEqual(result, "aaaabbbccd")

    def test_compression_and_decompression_works_correctly_together(self):
        compressed = self.lzw_service.compress("longer.txt")
        decompressed = self.lzw_service.decompress(compressed)
        self.assertEqual(decompressed, self.lzw_service.
                         _file_service.get_file_contents("longer.txt"))

    def test_decompress_returns_false_with_false_input(self):
        # bytes from 'aaaabbbccd' but added byte '12c'
        result = self.lzw_service.decompress(
            b'\x06\x11\x00\x06\x10b\x100c\x060d\12c')
        self.assertFalse(result)
