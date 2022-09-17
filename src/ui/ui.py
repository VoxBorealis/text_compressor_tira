from services.huffman_service import huffman_service
from services.file_service import file_service

COMMANDS = {
    "0": "0 quit",
    "1": "1 compress with Huffman"
}


class UI:
    """Class responsible for the applications user interface
    """

    def __init__(self):
        """Class constructor
        """
        pass

    def start(self):
        """Starts the UI and prompts the user with available commands
        """
        print("Text compressor...")
        for c in COMMANDS:
            print(COMMANDS[c])
        while True:
            command = input("command:")

            if command not in COMMANDS:
                print("invalid command")

            if command == "0":
                break
            elif command == "1":
                chosen_file = self._ask_user_for_file()
                huffman_service.file = chosen_file
                huffman_service.compress()

    def _ask_user_for_file(self):
        """Prompts the user to choose a file from a list

        Returns:
            .txt: text file chosen by the user to be compressed
        """
        print("Which file would you like to compress?")
        files = file_service.get_list_of_files()
        selected_file = files[int(input("select file (0-9):"))]

        return selected_file


ui = UI()
