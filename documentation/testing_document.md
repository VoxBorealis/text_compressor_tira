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
Example: The testing "file" is "aaaabbbccd", so I manually created a character frequenct list: [(4, 'a'), (3, 'b'), (2, 'c'), (1, 'd')] and ran the calculate_frequency() function on the file. This way I can then compare the results between the function and my manually created list to ensure the function returns a correct value. 

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