## Unit testing

Test coverage can be found here at [Codecov](https://app.codecov.io/gh/VoxBorealis/text_compressor_tira)

Unit testing tool: pytest

Run tests:
```bash
poetry run invoke test
```

Get coverage locally (html):
```
poetry run invoke coverage-report
```

### What was tested & how.

#### Huffman Service:

Testing was mainly achieved by creating inputs with known results, and comparing the results with the Huffman Service functions.
Example: The testing file is "aaaabbbccd", so I manually created a character frequenct list: [(4, 'a'), (3, 'b'), (2, 'c'), (1, 'd')] and ran the calculate_frequency() function on the file. This way I can then compare the results between the function and my manually created list to ensure the function returns a correct value. 

Testing for other functions was performed in a similiar fashion.

#### LZW Service:

Testing differentiated a bit from Huffman Service because there were fewer functions. Most of the logic is done inside the
compress and decompress functions.

Testing data is located at src/tests/data.
The data is fetched using a FakeFileService class and we perform the LZW functions on this data, confirming on each step,
that the correct results are outputted.

#### File Service:

Many of the functions here are just calls to the repository functions so they are not tested.
However there are some functions where I tested that the correct file names are being given to file_repository.

## Performance testing

I created a separate program (src/performance_test.py) to perform the performance testing. It compresses and decompresses the testing data and prints tables that show the amount of time on each file and the size reduction.

The testing data is mostly from the [Canterbury Corpus](https://corpus.canterbury.ac.nz/descriptions/#cantrbry), I noticed that [tuukkalai](https://github.com/tuukkalai/tiralabra) had used this data, so I decided to use mostly the same as him for further comparison purposes.

The results can be seen in the implementation document.

For any additional performance testing, create a 'performance_data' folder in 'src/data/' with the desired testing data and run performance_test.py