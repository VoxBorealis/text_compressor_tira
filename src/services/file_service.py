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


file_service = FileService()
