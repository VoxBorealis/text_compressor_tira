import json
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
        """Returns a list of all the files in the designated directory.

        Returns:
            list: A list of the text files in the data directory
        """
        files = []
        for file in self._dir_path.iterdir():
            files.append(file)

        return files

    def list_txt_files(self):
        """Returns a list of all the text files in the designated directory.

        Returns:
            list: A list of the text files in the data directory
        """
        files = []
        for file in self._dir_path.iterdir():
            if file.name.endswith('.txt') and \
                    "compressed" not in file.name:
                files.append(file)

        return files

    def list_bin_files(self):
        """Returns a list of all the binary files in the designated directory.

        Returns:
            list: A list of the bin files in the data directory
        """
        files = []
        for file in self._dir_path.iterdir():
            if file.name.endswith('.bin'):
                files.append(file)

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

    def get_bin_file_contents(self, file):
        """Returns the contents of a binary file

        Args:
            file (file): A binary file

        Returns:
            bytes: contents of the bin file in a bytes object
        """
        with open(file, 'rb') as bin_file:
            bytes_content = bin_file.read()

        return bytes_content

    def write_code_table(self, file_name, code_table):
        """Writes a .json file containing the code table
        from the Huffman Encoding

        Args:
            file_name (str): Name of the file to be written
            code_table (dict): A dictionary containing the Huffman Encoding

        Returns:
            boolean: True if the writing was successful
        """
        try:
            path_name = _FILE_DIR_PATH.joinpath(file_name)
            with open(path_name, 'w') as json_file:
                json_file.write(json.dumps(code_table))
            return True
        except Exception:
            return False

    def open_code_table(self, file_name):
        """Returns the Huffman Encoding code table

        Args:
            file_name (str): Name of the file

        Returns:
            dict: Huffman Encoding code table
        """
        path_name = _FILE_DIR_PATH.joinpath(file_name)
        with open(path_name) as json_file:
            code_table = json.load(json_file)

        return code_table

    def write_text_file(self, content, file_name):
        """Writes a text file from the contents of the given string

        Args:
            content (str): A string variable
            file_name (str): Name of the new file eg. (example.txt)

        Returns:
            boolean: True if writing was successful
        """
        path_name = _FILE_DIR_PATH.joinpath(file_name)
        try:
            with open(path_name, 'w') as text_file:
                text_file.write(content)
            return True
        except Exception:
            return False

    def write_bin_file(self, file_name, encoded_but_str):
        """Writes a binary file from the contents of a string
        that represents the bits

        Args:
            file_name (str): Name of the file that will be created,
                             e.g ('example.bin')
            encoded_but_str (str): A string variable containing "fake bits"
        """
        path_name = _FILE_DIR_PATH.joinpath(file_name)

        try:
            with open(path_name, 'wb') as fh:
                fh.write(self._to_Bytes(encoded_but_str))
            return True
        except Exception:
            return False

    def _to_Bytes(self, data):
        """Converts a string containing fake bits, into real bytes

        Args:
            data (str): A string that represents bits

        Returns:
            bytes: An array of bytes
        """
        b = bytearray()
        for i in range(0, len(data), 8):
            b.append(int(data[i:i+8], 2))

        return bytes(b)

    def write_bin_file_from_bytes(self, data, file_name):
        path_name = _FILE_DIR_PATH.joinpath(file_name)
        try:
            with open(path_name, 'wb') as fh:
                fh.write(data)
            return True
        except Exception:
            return False

    def get_bin_file_from_original(self, file):
        bin_file = _FILE_DIR_PATH.joinpath(file.name[:-4] + ".bin")
        return bin_file

    def get_json_file_from_original(self, file):
        json_file = _FILE_DIR_PATH.joinpath(file.name[:-4] + ".json")
        return json_file


file_repository = FileRepository(_FILE_DIR_PATH)
