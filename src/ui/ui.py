import time
from services.huffman_service import huffman_service
from services.lzw_service import lzw_service
from services.file_service import file_service

COMMANDS = {
    "0": "0 quit",
    "1": "1 compress with Huffman",
    "2": "2 decompress Huffman",
    "3": "3 compress with LZW",
    "4": "4 decompress with LZW",
    "ls": "ls show all files & sizes"
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
                start_time = time.perf_counter()
                huffman_service.file = chosen_file
                if huffman_service.compress():
                    end_time = time.perf_counter()
                    self.io_send(f'Successfully compressed {chosen_file.name} \N{grinning face} \
                        \nexecution time: {end_time - start_time:0.6f}s')
                else:
                    print("Error")
            elif command == "2":
                chosen_file = self._ask_user_for_file(command)
                start_time = time.perf_counter()
                if huffman_service.decompress(chosen_file):
                    end_time = time.perf_counter()
                    self.io_send(f'Successfully decompressed {chosen_file.name} \N{grinning face} \
                        \nexecution time: {end_time - start_time:0.6f}s')
                else:
                    print("Error")
            elif command == "3":
                chosen_file = self._ask_user_for_file(command)
                lzw_service.compress(chosen_file)
            
            elif command == "4":
                chosen_file = self._ask_user_for_file(command)
                start_time = time.perf_counter()
                lzw_service.decompress(chosen_file)
                end_time = time.perf_counter()
                self.io_send(f'Successfully decompressed {chosen_file.name} \N{grinning face} \
                    \nexecution time: {end_time - start_time:0.6f}s')

            elif command == "ls":
                self._print_all_files_and_sizes()

    def _ask_user_for_file(self, command):
        """Prompts the user to choose a file from a list

        Returns:
            .txt: text file chosen by the user to be compressed
        """
        if command in ["1", "3"]:
            print("Which file would you like to compress?")
            files = file_service.get_list_of_txt_files()
        if command in ["2", "4"]:
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
        
    def io_send(self, message):
        print(f'---------------------------------\
            \n{message} \n---------------------------------')


ui = UI()
