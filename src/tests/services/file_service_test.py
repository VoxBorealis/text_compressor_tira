import unittest
from services.file_service import FileService


class FakeStat:
    def __init__(self, size):
        self.st_size = size


class FakeFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def stat(self):
        return FakeStat(self.size)


class FakeFileRepository:
    def __init__(self, files=None):
        self.files = []
        self.files.append(FakeFile("test.txt", 100))
        self.files.append(FakeFile("test.bin", 50))

    def list_all_files(self):

        return self.files

    def write_bin_file(self, file_name, encoded_but_str):
        return file_name

    def write_code_table(self, file_name, code_table):
        if code_table == {}:
            return file_name
        return code_table

    def get_bin_file_from_original(self, file):
        return self.files[1]

    def get_json_file_from_original(self, file):
        return self.files[1]


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService(FakeFileRepository())
        self.test_file = self.file_service._file_repository.files[0]

    def test_get_list_of_files_is_equal_to_repository_list(self):
        files = self.file_service.get_list_of_files()
        self.assertEqual(self.file_service._file_repository.files, files)

    def test_write_bin_file_gives_correct_name(self):
        file_name = self.file_service.write_bin_file(self.test_file, "0")
        self.assertEqual(file_name, "test.bin")

    def test_write_code_table_gives_correct_name(self):
        file_name = self.file_service.write_code_table(self.test_file, {})
        self.assertEqual(file_name, "test.json")

    def test_write_code_table_swaps_dict_correctly(self):
        code_table = {"a": "0", "b": "1"}
        code_table_swapped = self.file_service.write_code_table(self.test_file,
                                                                code_table)
        self.assertEqual(code_table_swapped, {"0": "a", "1": "b"})

    def test_get_size_difference_return_correct_with_huffman(self):
        size = self.file_service.get_size_difference(self.test_file, "huffman")
        self.assertEqual(size, 100)

    def test_get_size_difference_return_correct_with_lzw(self):
        size = self.file_service.get_size_difference(self.test_file, "lzw")
        self.assertEqual(size, 50)
