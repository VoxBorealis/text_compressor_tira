import time
import os
from pathlib import Path
from tabulate import tabulate
from services.huffman_service import huffman_service
from services.lzw_service import lzw_service
from services.file_service import file_service

_FILE_DIR_PATH = Path(__file__).parents[0].\
    joinpath('data').joinpath('performance_data')


def performance_test():
    """Prints the testing results in a github markdown table format
    """
    huffman_data = run_huffman()
    lzw_data = run_lzw()
    clear_directory()
    head = ["Name", "Compression Time (ms)", "Decompression Time (s)",
            "Size (bytes)", "Compressed Size %"]
    print(tabulate(huffman_data, headers=head, tablefmt="github"))
    print("---------------------")
    print(tabulate(lzw_data, headers=head, tablefmt="github"))


def run_huffman():
    """Runs the Huffman compression and decompression on all of the
    performance testing data and returns the testing results in a list

    Returns:
        list: list of lists containing the results for each file
    """
    files = []
    results = []
    for file in _FILE_DIR_PATH.iterdir():
        if file.name.endswith(".bin") or "compressed" in file.name:
            continue
        files.append(file)

    def sort_func(file):
        return file.stat().st_size

    files.sort(key=sort_func)

    for file in files:
        start_time = time.perf_counter()
        huffman_service.compress(file)
        end_time = time.perf_counter()
        compression_time = format((end_time - start_time) * 1000, ".2f")
        size_reduction = file_service.get_size_difference(file, "huffman")

        start_time = time.perf_counter()
        huffman_service.decompress(file_service.
                                   get_bin_file_from_original(file))
        end_time = time.perf_counter()
        decompression_time = format((end_time - start_time) * 1000, ".2f")
        size = file.stat().st_size
        results.append((file.name, compression_time,
                        decompression_time, size, size_reduction))

    return results


def run_lzw():
    """Runs the LZW compression and decompression on all of the
    performance testing data and returns the testing results in a list

    Returns:
        list: list of lists containing the results for each file
    """
    files = []
    results = []
    for file in _FILE_DIR_PATH.iterdir():
        if file.name.endswith(".bin") or "compressed" in file.name:
            continue
        files.append(file)

    def sort_func(file):
        return file.stat().st_size

    files.sort(key=sort_func)

    for file in files:
        start_time = time.perf_counter()
        lzw_service.compress(file)
        end_time = time.perf_counter()
        compression_time = format((end_time - start_time) * 1000, ".2f")
        size_reduction = file_service.get_size_difference(file, "lzw")

        start_time = time.perf_counter()
        lzw_service.decompress(file_service.get_bin_file_from_original(file))
        end_time = time.perf_counter()
        decompression_time = format((end_time - start_time) * 1000, ".2f")
        size = file.stat().st_size
        results.append((file.name, compression_time,
                        decompression_time, size, size_reduction))

    return results


def clear_directory():
    """Deletes binary and decompressed files after testing is done
    """
    for file in _FILE_DIR_PATH.parent.iterdir():
        if "performance_data" in file.name or \
                file.name.endswith(".gitignore"):
            continue
        os.remove(file)


if __name__ == "__main__":
    performance_test()
