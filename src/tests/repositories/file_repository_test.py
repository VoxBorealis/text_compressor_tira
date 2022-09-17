from pathlib import Path
import unittest
from repositories.file_repository import FileRepository


class TestFileRepository(unittest.TestCase):
    def setUp(self):
        #file_repository._dir_path = Path(__file__).parents[1].joinpath('data')
        test_path = Path(__file__).parents[1].joinpath('data')
        self.file_repository = FileRepository(test_path)

    def test_list_all_files(self):
        files = self.file_repository.list_all_files()
        self.assertEqual(len(files), 1)
