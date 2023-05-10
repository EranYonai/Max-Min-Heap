#  Max-Min-Heap implementation in Python
This project was tested and written in Python 3.9+ according to PEP8 code writing style.
A max-min heap is an almost complete binary tree, in which each node at **even depth is bigger than (or equal) to every children** of it, and each node at **odd depth is lower than (or equal) to every children**  of it.
I wrote MaxMinHeap class, using OOP practices. I think it is a better implementation than the one suggested.
* Supports cli commands.
* Input can be loaded from a .txt file, in which the following pattern will be parsed: '[1,2,3,4]'.
### Notes:
- Help methods will be with _ or __ prefix.
- Sources:
    1. https://en.wikipedia.org/wiki/Min-max_heap
    2. Implementation of a Min-max heap following Atkinson, Sack, Santoro, and Strothotte (1986): https://doi.org/101145/6617.6621