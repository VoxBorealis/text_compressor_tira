# text-compressor-tira

![GitHub Actions](https://github.com/VoxBorealis/text_compressor_tira/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/VoxBorealis/text_compressor_tira/branch/main/graph/badge.svg?token=B7ZURMRPLA)](https://codecov.io/gh/VoxBorealis/text_compressor_tira)

Text compressor developed as a part of [Data Structures & Algorithms Project Course](https://tiralabra.github.io/2022_p1/) at University of Helsinki.
Both, Huffman and Lempel-Ziv-Welch algorithms, have been implemented into the compressor.

See the [Implementation document](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/implementation_document.md) for performance results.

## Links to documentation

### [Design document](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/design_document.md)
### [Testing document](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/testing_document.md)
### [Implementation document](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/implementation_document.md)



## Weekly Reports

* [Weekly report #1](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/Weekly%20Reports/weekly_report_1.md)
* [Weekly report #2](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/Weekly%20Reports/weekly_report_2.md)
* [Weekly report #3](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/Weekly%20Reports/weekly_report_3.md)
* [Weekly report #4](https://github.com/VoxBorealis/text_compressor_tira/blob/main/documentation/Weekly%20Reports/weekly_report_4.md)
* [Weekly report #5](./documentation/Weekly%20Reports/weekly_report_5.md)
* [Weekly report #6](./documentation/Weekly%20Reports/weekly_report_6.md)


## Installation

You need to have python3 *and* poetry installed on your system

1. Install dependencies:
```
poetry install
```
2. Launch the program:
```
poetry run invoke start
```

## User Manual

### Compression

1. Move your desired text files into the data folder under /src
2. Follow the prompts from the program to compress it, using either Huffman or LZW!
3. Your compressed file should now be a .bin file in the same data folder

### Decompression

1. Follow the prompts from the program to decompress a .bin file
2. Your decompressed file should now be in the data folder with the name: {file_name}_decompressed

## Commands

Check codestyle:
```
poetry run invoke codestyle
```
