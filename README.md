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

---

## Usage:
1. Install environment `pip install -r requirements.txt`
2. Run driver `python3 driver_RUNME.py`

---
## Output example of tests:
```
❯ python src/driver_RUNME.py
Heap is empty, build heap in order to see extended menu.
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
Enter your choice: 3
Running tests... it might take some time, depends on your hardware.
Tests are randomizing lists [1-512 length], with integers [-2000-2000], running 1000 times each.
Testing Build Heap
Testing Heap Insert
Testing Extract min/max (no printing), extracting every element from heap... (and testing heap integrity after each attempt.)
Testing Heap Delete, removing every element from the heap... (and testing heap integrity after each attempt.)
Done!
Build test results: All 1000 attempts PASSED.
Insert test results: All 1000 attempts PASSED.
Extract test results: All 1000*<generated heap size> attempts PASSED.
Delete test results: All 100*<generated heap size> attempts PASSED.
```

## Output example of general usage:
```
❯ python src/driver_RUNME.py
Heap is empty, build heap in order to see extended menu.
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
Enter your choice: 2
1 to build with cli, 2 to heap from file: 1
To stop inserting elements, write a not integer, to print write print
Please enter an element for insertion: 50
50
Heap size: 1
Please enter an element for insertion: 300
 300
 /
50
Heap size: 2
Please enter an element for insertion: 20
  300
  / \
 /   \
50   20
Heap size: 3
Please enter an element for insertion: -200
    300
    / \
   /   \
 -200  20
 /
50
Heap size: 4
Please enter an element for insertion: 532
     532
     / \
    /   \
  -200  20
  / \
 /   \
50   300
Heap size: 5
Please enter an element for insertion: e
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 5
Maximum element in heap: 532
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 6
Minimum element in heap: -200
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 4
  300
  / \
 /   \
50   20
Heap size: 3
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 7
Enter value to insert: 500
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 4
     500
     / \
    /   \
   50   20
  /
300
Heap size: 4
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 8
Enter an index of an item to delete (1 is the root): 1
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 4
  300
  / \
 /   \
20   50
Heap size: 3
--------
Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.
	        4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.

Enter your choice: 1
Bye Bye...
```