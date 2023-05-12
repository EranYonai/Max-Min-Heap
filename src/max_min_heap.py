#  Author: Eran Yonai, 318647138
#  Read the README file for more information and sources.

from typing import Optional, List
import sys
import math


class MaxMinHeap:
    """MaxMinHeap is a class that holds max-min heap logic.
    Max-min heap is a data structure which comply with the following logic:
    It's an almost complete binary tree &,
        A. Every node on an even level, is bigger or equal (>=) than it's descendants;
        B. Every node on an un-even level is smaller or equal than it's descendants.
                      50            |0 >=
                    /    \          |
                   15     10        |1 <=
                  / \     / \       |
                25  35  11  12      |2 >=
                / \                 |
               17  18               |3 <=
        as a list: [50,15,10,25,35,11,12,17,18]
    """

    def __init__(self):
        """Initializes empty MaxMinHeap object.
            Use _set_heap to set heap values (for a MaxMinHeap). (already an heap)
            Use build_heap to create heap from a non MaxMinHeap array. (not already an heap)
        """
        self.heapob: List = []
        self.size: int = 0

    def __len__(self) -> int:
        """len(MaxMinHeap) support.

        :return: length of MaxMinHeap object.
        :rtype: int
        """
        return self.size

    def build_heap(self, unsorted_heap: list):
        """Building heap using heapify (top-bottom).
        Complexity: O(n)

        :param unsorted_heap: _description_
        :type unsorted_heap: list
        """
        self.heapob, self.size = unsorted_heap, len(unsorted_heap)
        for i in range(self.size//2 + 1, -1, -1):
            self._heapify(i=i)

    def heap_extract_max(self, to_print: bool = True) -> Optional[int]:
        """Extracts and prints the max value in the heap.
        (Will delete the max value from the heap, (_remove_max),
        and keep maxmin heap property).
        Complexity: O(1) for getting max element.
        Complexity: O(log(n)) for removal of max element.

        :return: max value in heap, if empty returns None
        :rtype: int, optional
        """
        if self.size == 0:
            print("Heap is empty.")
            return  # heap is empty.
        max_element = self.heapob[0]
        if to_print:
            print(f"Maximum element in heap: {self.heapob[0]}")
        self._remove_max()
        return max_element  # the element in root is the max element.

    def heap_extract_min(self, to_print: bool = True) -> Optional[int]:
        """Extracts and print the min value in the heap.
        (Will delete the min value from the heap, (_remove_min)),
        and keep maxmin heap property).
        Complexity: O(1) for getting min element.
        Complexity: O(log(n)) for removal of min element.

        :return: if heap is not empty, returns min value.
        :rtype: Optional[int]
        """
        if self.size == 0:
            print("Heap is empty.")
            return None  # heap is empty, returns -1.
        if self.size == 1:
            min_element = self.heapob[0]
            self.heapob = self.heapob[:-1]
            self.size = len(self.heapob)  # or 0
            if to_print:
                print(f"Minimum element in heap: {min_element}")
            return min_element  # heap length is 1, returning the only element.
        if self.size == 2:
            min_element = self.heapob[1]
            self.heapob = self.heapob[:-1]
            self.size = len(self.heapob)  # or 1
            if to_print:
                print(f"Minimum element in heap: {min_element}")
            # heap length is 2, the only child is the minimum.
            return min_element
        min_element = min(self.heapob[1], self.heapob[2])
        self._remove_min()
        if to_print:
            print(f"Minimum element in heap: {min_element}")
        return min_element  # heap length is 1, returning the only element.

    def heap_insert(self, key: int):
        """heap_insert heap_insert insert a key into the heap. Complexity: O(log(n)).

        :param key: a value to be inserted to the heap.
        :type key: int
        :param A: a specific min_max_heap, defaults to None (will use class's object)
        :type A: list, optional
        """

        self.heapob.append(key)
        self.size = len(self.heapob)  # or +=1
        self._bubble_up(i=self.size - 1)

    def heap_delete(self, i: int):
        """deletes the element in index *i-1!* from the heap.
        Complexity same as _heapify: O(nlogn)

        :param i: index to remove from heap.
        :type i: int
        """
        i -= 1
        if i >= self.size:
            print("Index is not in range of heap.")
            return
        elif i == 0:
            self.heap_extract_max(to_print=False)
        else:
            self.heapob[i] = sys.maxsize
            self._bubble_up(i=i)  # move to root, O(log n)
            self.heap_extract_max(to_print=False)  # O(log n)
            for i in range(self.size-1, self.size // 2 - 1, -1):
                self._bubble_up(i=i)

    def _heapify(self, i: int) -> None:
        """heapify common algorithm for max-min modifications, runs in O(log n)
        builds heap from up to bottom

        :param i: an index
        :type i: int
        """
        if self._level(i) % 2 == 0:  # max level
            self._heapify_max(i=i)
        else:  # min level
            self._heapify_min(i=i)

    def _heapify_max(self, i: int) -> None:
        """help function for heapify.
        assumes that index is a valid index, in an even depth in the heap.
        moves index to a the correct place.

        :param i: index
        :type i: int
        """
        child = False
        if self.__has_children(i=i):
            m = self.__get_left_child(i=i)
            if self.__get_right_child(i=i) < self.size and self.heapob[self.__get_right_child(i=i)] > self.heapob[m]:
                m = self.__get_right_child(i=i)
            child = True
            for j in range(i*4+3, min(i*4+7, self.size)):
                if self.heapob[j] > self.heapob[m]:
                    m = j
                    child = False
            if child:
                if self.heapob[m] > self.heapob[i]:
                    self.__swap_elements(i=i, j=m)
            else:
                if self.heapob[m] > self.heapob[i]:
                    self.__swap_elements(i=i, j=m)
                    if self.heapob[m] < self.heapob[(m-1) // 2]:
                        self.__swap_elements(i=m, j=(m-1)//2)
                    self._heapify_max(i=m)

    def _heapify_min(self, i: int) -> None:
        """help function for heapify.
        assumes that index is a valid index, in an even depth in the heap.
        moves index to a the correct place.

        :param i: _description_
        :type i: int
        """
        child = False
        if self.__has_children(i=i):
            m = self.__get_left_child(i=i)
            if self.__get_right_child(i=i) < self.size and self.heapob[self.__get_right_child(i=i)] < self.heapob[m]:
                m = self.__get_right_child(i=i)
            child = True
            for j in range(i*4+3, min(i*4+7, self.size)):
                if self.heapob[j] < self.heapob[m]:
                    m = j
                    child = False
            if child:
                if self.heapob[m] < self.heapob[i]:
                    self.__swap_elements(i=i, j=m)
            else:
                if self.heapob[m] < self.heapob[i]:
                    self.__swap_elements(i=i, j=m)
                    if self.heapob[m] > self.heapob[(m-1) // 2]:
                        self.__swap_elements(i=m, j=(m-1)//2)
                    self._heapify_min(i=m)

    def _remove_max(self) -> None:
        """removes max element of heap.
        """
        if self.size == 0:
            return
        self.heapob[0] = self.heapob[-1]  # switch last element with root
        self.heapob = self.heapob[:-1]  # remove last element
        self.size = len(self.heapob)  # update size
        self._heapify(i=0)

    def _remove_min(self) -> None:
        """removes min element of heap.
        """
        if self.size == 0:
            return
        if self.size == 1 or self.size == 2:
            self.heapob = self.heapob[:-1]  # removes last element
            self.size = len(self.heapob)
        else:
            i = 1 if self.heapob[1] < self.heapob[2] else 2
            self.heapob[i] = self.heapob[self.size - 1]
            self.heapob = self.heapob[:-1]
            self.size = len(self.heapob)
            self._heapify(i=i)

    def _bubble_up(self, i: int) -> None:
        """uses bubble_up_min and _max for moving up an element in the heap.

        :param i: index
        :type i: int
        """
        if self._level(i=i) % 2 == 0:
            if self.__has_parent(i=i):
                if self.heapob[i] < self.heapob[self.__get_parent(i=i)] and i > 0:
                    self.__swap_elements(i=i, j=self.__get_parent(i=i))
                    self._bubble_up_min(i=self.__get_parent(i=i))
                else:
                    self._bubble_up_max(i=i)
        else:
            if self.__has_parent(i=i):
                if self.heapob[i] > self.heapob[self.__get_parent(i=i)] and i > 0:
                    self.__swap_elements(i=i, j=self.__get_parent(i=i))
                    self._bubble_up_max(i=self.__get_parent(i))
                else:
                    self._bubble_up_min(i=i)

    def _bubble_up_max(self, i: int) -> None:
        """bubble up max moves the newly inserted node to the top of the heap,
        swapping it with its parent if necessary until it is greater than or equal to its parent.

        :param i: index
        :type i: int
        """
        while i > 2:
            grand_parent = self.__get_grandparent(i=i)
            if self.heapob[i] > self.heapob[grand_parent]:
                self.__swap_elements(i=i, j=grand_parent)
                i = grand_parent
            else:
                return

    def _bubble_up_min(self, i: int) -> None:
        """bubble up min moves the newly inserted node to the top of the heap,
        swapping it with its parent if necessary until it is less than or equal to its parent.

        :param i: index
        :type i: int
        """
        while i > 2:
            grand_parent = self.__get_grandparent(i=i)
            if self.heapob[i] < self.heapob[grand_parent]:
                self.__swap_elements(i=i, j=grand_parent)
                i = grand_parent
            else:
                return

    def __swap_elements(self, i: int, j: int) -> None:
        """swaps two elements

        :param i: element 1
        :type i: int
        :param j: element 2
        :type j: int
        """
        self.heapob[i], self.heapob[j] = self.heapob[j], self.heapob[i]

    def __has_children(self, i: int) -> bool:
        """returns if a node has at least 1 child.

        :param i: index
        :type i: int
        :rtype: bool
        """
        return self.size > i * 2 + 1 or self.size > i * 2 + 2

    def __get_left_child(self, i: int) -> int:
        """gets left child of the node if exists.

        :param i: index
        :type i: int
        :return: left child or -1 if does not exist.
        :rtype: int
        """
        left_child = i * 2 + 1
        return left_child if self.size > left_child else -1

    def __get_right_child(self, i: int) -> int:
        """gets right child of the node if exists.

        :param i: index
        :type i: int
        :return: right child or -1 if does not exist.
        :rtype: int
        """
        right_child = i * 2 + 2
        return right_child if self.size > right_child else -1

    def __get_parent(self, i: int) -> int:
        """gets parent of a node

        :param i: index
        :type i: int
        :return: returns the parent node index, -1 if it's the root.
        :rtype: int
        """
        return (i-1) // 2 if (i-1) != 0 else 0

    def __has_parent(self, i: int) -> bool:
        """returns if a node has parent.

        :param i: index
        :type i: int
        :return: true if node has a parent
        :rtype: bool
        """
        return self.__get_parent(i=i) != -1

    def __get_grandparent(self, i: int) -> int:
        """gets grand-parent of a node.

        :param i: index
        :type i: int
        :return: grand-parent index, -1 if does not exit.
        :rtype: int
        """
        return self.__get_parent(i=self.__get_parent(i=i))

    @staticmethod
    def _level(i: int) -> int:
        """returns the level (height, depth) of a node.

        :param i: index
        :type i: int
        :return: level of the node.
        :rtype: int
        """
        return math.floor(math.log2(i+1))

    def _set_heap(self, heap: list) -> None:
        """manually sets heap, don't use!, force injecting.

        :param heap: list to inject.
        :type heap: list
        """
        self.heapob = heap.copy()
        self.size = len(self.heapob)
