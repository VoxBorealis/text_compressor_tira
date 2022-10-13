import time
from pathlib import Path
#from services.huffman_service import huffman_service
from services.lzw_service import lzw_service
#from services.file_service import file_service

_FILE_DIR_PATH = Path(__file__).parents[0].joinpath('data')
file1 = _FILE_DIR_PATH.joinpath("2mb sample text.txt")


def performance_test():
    print(run_lzw(3))

def run_huffman():
    pass

def run_lzw(passes):
    
    file1_compress_time = 0

    for i in range(passes):
        print(f'i: {i}')
        start_time = time.perf_counter()
        lzw_service.compress(file1)
        end_time = time.perf_counter()
        file1_compress_time += end_time - start_time
    
    file1_compress_time = file1_compress_time / passes


    return file1_compress_time

if __name__ == "__main__":
    performance_test()