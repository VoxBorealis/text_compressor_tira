from services.huffman_service import huffman_service
from services.file_service import file_service

COMMANDS = {
    "0": "0 quit",
    "1": "1 compress with Huffman",
    "2": "2 decompress Huffman",
    "3": "3 show all files & sizes"
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
                chosen_file = self._ask_user_for_file(command)
                huffman_service.file = chosen_file
                if huffman_service.compress():
                    print(f'Successfully compressed {chosen_file.name} \N{grinning face}')
                else:
                    print("Error")
            elif command == "2":
                chosen_file = self._ask_user_for_file(command)
                if huffman_service.decompress(chosen_file):
                    print(f'Succesfully decoded {chosen_file.name}')
                else:
                    print("Error")
            elif command == "3":
                self._print_all_files_and_sizes()

    def _ask_user_for_file(self, command):
        """Prompts the user to choose a file from a list

        Returns:
            .txt: text file chosen by the user to be compressed
        """
        if command == "1":
            print("Which file would you like to compress?")
            files = file_service.get_list_of_txt_files()
        if command == "2":
            print("Which file would you like to decode?")
            files = file_service.get_list_of_bin_files()

        for i, file in enumerate(files):
            print(f'{i}: {file.name} - size: {file.stat().st_size} bytes')

        selected_file = files[int(input("select file (0-9):"))]

        return selected_file

    def _print_all_files_and_sizes(self):
        files = file_service.get_list_of_files()
        for i, file in enumerate(files):
            print(f'{i}: {file.name} - size: {file.stat().st_size} bytes')


ui = UI()
