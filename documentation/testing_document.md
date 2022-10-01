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

#### File Service:


## Performance testing