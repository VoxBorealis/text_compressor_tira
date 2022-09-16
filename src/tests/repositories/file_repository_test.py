import unittest
from repositories.file_repository import file_repository
from pathlib import Path

class TestFileRepository(unittest.TestCase):
    def setUp(self):
        file_repository._dir_path = Path(__file__).parent.joinpath('data')

    def test_list_all_files(self):
        files = file_repository.list_all_files()
        self.assertEqual(len(files), 1)


