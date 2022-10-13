from repositories.file_repository import (
    file_repository as default_file_repository
)


class FileService:
    """Class responsible for the logic of file handling
    """

    def __init__(self, file_repository=default_file_repository):
        """Class constructor.

        Args:
            file_repository (_type_, optional): _description_.
                Defaults to default_file_repository.
        """
        self._file_repository = file_repository

    def get_list_of_files(self):
        """Returns a list of all the files in the designated directory

        Returns:
            list: A list of all the files in the data directory
        """
        return self._file_repository.list_all_files()
    
    def get_list_of_txt_files(self):
        """Returns a list of all the text files in the designated directory

        Returns:
            list: A list of all the text files in the data directory
        """
        return self._file_repository.list_txt_files()
    
    def get_list_of_bin_files(self):
        """Returns a list of all the bin files in the designated directory

        Returns:
            list: A list of all the bin files in the data directory
        """
        return self._file_repository.list_bin_files()
    
    def get_file_contents(self, file):
        """Returns the contents of the file as a string

        Args:
            file (file): A PosixPath of a .txt file

        Returns:
            str: Contents of the file as a string
        """
        return self._file_repository.get_file_contents(file)
    
    def get_bin_file_contents(self, file):
        """Returns the contents of a binary file

        Args:
            file (file): A binary file

        Returns:
            bytes: contents of the bin file in a bytes object
        """
        return self._file_repository.get_bin_file_contents(file)

    def write_bin_file(self, file, encoded_but_str):
        """Writes a binary file from the contents of the given string variable.
        The name of the new file will be that of the given file.

        Args:
            file (file): A file used for getting a name for the file
            eg. example.txt -> example.bin
            encoded_but_str (str): A string variable containing "fake bits"

        Returns:
            boolean: True if writing was successful
        """
        file_name = file.name[0:-4] + ".bin"
        return self._file_repository.write_bin_file(file_name, encoded_but_str)
    
    def write_bin_file_from_bytes(self, file, data):
        file_name = file.name[0:-4] + ".bin"
        return self._file_repository.write_bin_file_from_bytes(data, file_name)

    def write_text_file(self, file, content):
        """Writes a text file from the contents of the given
        string variable. The name of the new file will be that of the given file.

        Args:
            file (file): A file used for getting a name for the file
            eg. example.bin -> example.txt
            content (str): A string variable

        Returns:
            boolean: True if writing was successful
        """
        file_name = file.name[0:-4] + "_decompressed.txt"
        return self._file_repository.write_text_file(content, file_name)
    
    def write_code_table(self, file, code_table):
        """First, swaps the keys and values in the code table,
        e.g. ('a': '0' -> '0': 'a'). Then writes the dict as json.

        Args:
            file (file): The text file, used to get the name for the new file
            code_table (dict): Dictionary containing key, value pairs of all the symbols and their respective codes.

        Returns:
            boolean: True if writing was successful
        """
        file_name = file.name[0:-4] + ".json"
        code_table_swapped = {v: k for k, v in code_table.items()}
        return self._file_repository.write_code_table(file_name, code_table_swapped)
    
    def get_code_table(self, file):
        """Returns the Huffman Encoding code table
        with the name of the given file.

        Args:
            file (file): A file object for fetching the correct code table

        Returns:
            dict: Huffman Encoding code table
        """
        file_name = file.name[0:-4] + ".json"
        return self._file_repository.open_code_table(file_name)
    
    def get_size_difference(self, file, type):
        """Returns the size reduction from compression

        Args:
            file (file): original file

        Returns:
            float: size reduction in percentage
        """
        compressed_size = self._file_repository.\
            get_bin_file_from_original(file).stat().st_size

        if type == "huffman":
            code_table_size = self._file_repository.\
                get_json_file_from_original(file).stat().st_size
            compressed_size += code_table_size
        return round(compressed_size / file.stat().st_size * 100, 2)
        

file_service = FileService()
