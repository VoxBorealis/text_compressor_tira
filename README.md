# text-compressor-tira

![GitHub Actions](https://github.com/VoxBorealis/text_compressor_tira/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/VoxBorealis/text_compressor_tira/branch/main/graph/badge.svg?token=B7ZURMRPLA)](https://codecov.io/gh/VoxBorealis/text_compressor_tira)

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

## How to use

The program only accepts .txt files at this point. 
1. Move your desired text file into the data folder under /src
2. Follow the prompts from the program to compress it!