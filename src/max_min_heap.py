#  Author: Eran Yonai, 318647138
#  Read the README file for more information and sources.

from typing import Optional, List
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
        Complexity: ()

        :param unsorted_heap: _description_
        :type unsorted_heap: list
        """
        self.heapob, self.size = unsorted_heap, len(unsorted_heap)
        for i in range(self.size//2, -1, -1):
            self._heapify(i=i)

    def heap_extract_max(self) -> Optional[int]:
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
            return None  # heap is empty, returns -1.
        max_element = self.heapob[0]
        print(f"Maximum element in heap: {self.heapob[0]}")
        self._remove_max()
        return max_element  # the element in root is the max element.

    def heap_extract_min(self) -> Optional[int]:
        """Extracts and print the min value in the heap.
        (Will delete the min value from the heap, (_remove_min)),
        and keep maxmin heap property).
        Complexity: O(1) for getting max element.
        Complexity: O(log(n)) for removal of max element.

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
            print(f"Minimum element in heap: {min_element}")
            return min_element  # heap length is 1, returning the only element.
        if self.size == 2:
            min_element = self.heapob[1]
            self.heapob = self.heapob[:-1]
            self.size = len(self.heapob)  # or 1
            print(f"Minimum element in heap: {min_element}")
            return min_element  # heap length is 2, the only child is the minimum.
        min_element = min(self.heapob[1], self.heapob[2])
        self._remove_min()
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

    def heap_delete(self, i: int, A: Optional[List] = None):
        pass

    def _heapify(self, i: int) -> None:
        if self._level(i) % 2 == 0:  # max level
            self._heapify_max(i=i)
        else:  # min level
            self._heapify_min(i=i)

    def _heapify_max(self, i: int) -> None:
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
        if self.size == 0:
            return
        self.heapob[0] = self.heapob[-1]  # switch last element with root
        self.heapob = self.heapob[:-1]  # remove last element
        self.size = len(self.heapob)  # update size
        self._heapify(i=0)

    def _remove_min(self) -> None:
        if self.size == 0:
            return
        if self.size == 1 or self.size == 2:
            self.heabob = self.heapob[:-1]  # removes last element
            self.size = len(self.heabob)
        else:
            i = 1 if self.heapob[1] < self.heapob[2] else 2
            self.heapob[i] = self.heapob[self.size - 1]
            self.heapob = self.heapob[:-1]
            self.size = len(self.heapob)
            self._heapify(i)

    def _bubble_up(self, i: int) -> None:
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
        while i > 2:
            grand_parent = self.__get_grandparent(i=i)
            if self.heapob[i] > self.heapob[grand_parent]:
                self.__swap_elements(i=i, j=grand_parent)
                i = grand_parent
            else:
                return

    def _bubble_up_min(self, i: int) -> None:
        while i > 2:
            grand_parent = self.__get_grandparent(i=i)
            if self.heapob[i] < self.heapob[grand_parent]:
                self.__swap_elements(i=i, j=grand_parent)
                i = grand_parent
            else:
                return

    def __swap_elements(self, i: int, j: int) -> None:
        self.heapob[i], self.heapob[j] = self.heapob[j], self.heapob[i]

    def __has_children(self, i: int) -> bool:
        return self.size > i * 2 + 1 or self.size > i * 2 + 2

    def __get_left_child(self, i: int) -> int:
        left_child = i * 2 + 1
        return left_child if self.size > left_child else -1

    def __get_right_child(self, i: int) -> int:
        right_child = i * 2 + 2
        return right_child if self.size > right_child else -1

    def __get_parent(self, i: int) -> int:
        return (i-1) // 2

    def __has_parent(self, i: int) -> int:
        return self.__get_parent(i=i) != -1

    def __get_grandparent(self, i: int) -> int:
        return self.__get_parent(i=(i-1)//2)

    def __has_grandparent(self, i: int) -> bool:
        return self.__get_grandparent(i=i) != -1

    @staticmethod
    def _level(i: int) -> int:
        return math.floor(math.log2(i+1))

    def _set_heap(self, heap: list) -> None:
        self.heapob = heap.copy()
        self.size = len(self.heapob)

