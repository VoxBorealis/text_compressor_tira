import os
from pathlib import Path

_FILE_DIR_PATH = Path(__file__).parents[1].joinpath('data')

class FileRepository:
    """Class responsible for managing the text files
    """

    def __init__(self, dir_path):
        """Class constructor

        Args:
            dir_path (str): The path to the directory where the text files are saved
        """
        self._dir_path = dir_path

    def list_all_files(self):
        files = []
        for i, file in enumerate(self._dir_path.iterdir()):
            files.append(file)
            print(f'{i}: {file.name} - size: {file.stat().st_size} bytes')

        return files
    

file_repository = FileRepository(_FILE_DIR_PATH)
