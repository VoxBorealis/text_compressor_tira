import unittest
from services.file_service import FileService

class FakeFileRepository:
    def __init__(self, files=None):
        default_files = ["first file", "second file"]
        self.files = files or default_files

    def list_all_files(self):
        return self.files

class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService(FakeFileRepository())

    def test_get_list_of_files_is_equal_to_repository_list(self):
        files = self.file_service.get_list_of_files()
        self.assertEqual(self.file_service._file_repository.files, files)
