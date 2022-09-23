from pathlib import Path

_FILE_DIR_PATH = Path(__file__).parents[1].joinpath('data')


class FileRepository:
    """Class responsible for managing the text files
    """

    def __init__(self, dir_path):
        """Class constructor

        Args:
            dir_path (str): The path to the directory
            where the text files are saved
        """
        self._dir_path = dir_path

    def list_all_files(self):
        """Returns a list of all the files in the designated directory

        Returns:
            _array_: An array of the files
        """
        files = []
        for i, file in enumerate(self._dir_path.iterdir()):
            files.append(file)
            print(f'{i}: {file.name} - size: {file.stat().st_size} bytes')

        return files
        
    def get_file_contents(self, file):
        """Returns the contents of the file as a string

        Args:
            file (file): A PosixPath of a .txt file

        Returns:
            str: Contents of the file as a string
        """
        with open(file) as f:
            contents = f.read()
        
        return contents

    def write_bin_file2(self, file_name, file_as_str, code_table):
        path_name = _FILE_DIR_PATH.joinpath(file_name)
        try:
            with open(path_name, 'wb') as file_handler:
                for c in file_as_str:
                    
                    file_handler.write(code_table[c].encode())
            return True
        except:
            return False

    def write_bin_file(self, file_name, file_as_str, code_table):
        path_name = _FILE_DIR_PATH.joinpath(file_name)
        encoded_but_str = ""
        for c in file_as_str:
            encoded_but_str = encoded_but_str + code_table[c]
        
        with open(path_name, 'wb') as fh:
            fh.write(self._to_Bytes(encoded_but_str))

    def _to_Bytes(self, data):
        b = bytearray()
        for i in range(0, len(data), 8):
            b.append(int(data[i:i+8], 2))
        return bytes(b)
        

file_repository = FileRepository(_FILE_DIR_PATH)
