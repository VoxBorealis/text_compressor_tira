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
        files = self._file_repository.list_all_files()
        return files
    
    def get_file_contents(self, file):
        """Returns the contents of the file as a string

        Args:
            file (file): A PosixPath of a .txt file

        Returns:
            str: Contents of the file as a string
        """
        return self._file_repository.get_file_contents(file)

    def write_bin_file(self, file, code_table):
        file_name = file.name[0:-4] + ".bin"
        print(file_name)
        file_as_str = self._file_repository.get_file_contents(file)
        return self._file_repository.write_bin_file(file_name, file_as_str, code_table)

file_service = FileService()
