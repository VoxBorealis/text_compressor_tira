# Design document

Course info: Python, CS bsC, English

The goal is to develop a *Python* program that will take as an input a text file, and compress it to 40-60% of it's original size.
Naturally, the compressed file should be decompressable to it's original form **losslessly**.

## Algorithms and Data Structures

To accomplish this, I will be using two lossless data compression algorithms ([Huffman](https://en.wikipedia.org/wiki/Huffman_coding) & [Lempel Ziv](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)). Only one is necessary, but for the sake of the project's scope, I will be examining the differences between the two.

As for data structures, I will be using a binary tree for the Huffman Tree, arrays...(WIP)

## Time - & Space complexity

For the Huffman algorithm, a time complexity of O(nlogn) and space complexity of O(n) is desired.

For the Lempel-Ziv-Welch algoritm, a time complexity of O(n) is desired.


### Sources

Wikipedia: [Huffman](https://en.wikipedia.org/wiki/Huffman_coding), [Lempel Ziv](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)