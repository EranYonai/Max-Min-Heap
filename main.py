#  Author: Eran Yonai, 318647138
#  This task will be written in Python, 3.9 according to PEP8 code writing style.
#  (that's why method's names are lower-case), i'll use typing as possible.
#  I wrote MaxMin as a class, I think it is a better implementation than the one suggested in the task.
#  And in the forum, Yael Borner said that it is okay to implement in OOP.
#  - Help functions will be with _ prefix.
#  - Sources:
#   1. https://en.wikipedia.org/wiki/Min-max_heap
#   2. Implementation of a Min-max heap following Atkinson, Sack, Santoro, and
#       Strothotte (1986): https://doi.org/10.1145/6617.6621

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

    def heapify(self, i: int):
        pass

    def build_heap(self, unsorted_heap: list):
        # self.heapob, self.size = unsorted_heap, len(unsorted_heap)
        # for i in range(math.floor(self.size/2), 0, -1):
        #     self._trickle_down(i=i)
        self.size = len(unsorted_heap)
        self.heapob = unsorted_heap
        for i in range(self.size//2, -1, -1):
            self._trickle_down(i=i)

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
        self.size += 1
        self._bubble_up(self.size)

    def heap_delete(self, i: int, A: Optional[List] = None):
        pass

    @staticmethod
    def _level(i: int) -> int:
        return math.floor(math.log2(i+1))

    def _set_heap(self, heap: list) -> None:
        self.heapob = heap.copy()
        self.size = len(self.heapob)

    def _trickle_down(self, i: int) -> None:
        if self._level(i) % 2 == 0:  # max level
            self._trickle_down_max(i=i)
        else:  # min level
            self._trickle_down_min(i=i)

    def _trickle_down_max(self, i: int) -> None:
        child = False
        if self.size > i * 2 + 1:  # element i has children
            m = i * 2 + 1
            if i * 2 + 2 > self.size and self.heapob[i*2+2] > self.heapob[m]:
                m = i * 2 + 2
            child = True
            for j in range(i*4+3, min(i*4+7, self.size)):
                if self.heapob[j] > self.heapob[m]:
                    m = j
                    child = False
            if child:
                if self.heapob[m] > self.heapob[i]:
                    self.heapob[i], self.heapob[m] = self.heapob[m], self.heapob[i]  # switch values
            else:
                if self.heapob[m] > self.heapob[i]:
                    self.heapob[i], self.heapob[m] = self.heapob[m], self.heapob[i]
                    if self.heapob[m] < self.heapob[(m-1) // 2]:
                        self.heapob[m], self.heapob[(m-1)//2] = self.heapob[(m-1)//2], self.heapob[m]
                    self._trickle_down_max(i=m)

    def _trickle_down_min(self, i: int) -> None:
        child = False
        if self.size > i * 2 + 1:  # element i has children
            m = i * 2 + 1
            if i * 2 + 2 < self.size and self.heapob[i*2+2] < self.heapob[m]:
                m = i * 2 + 2
            child = True
            for j in range(i*4+3, min(i*4+7, self.size)):
                if self.heapob[j] < self.heapob[m]:
                    m = j
                    child = False
            if child:
                if self.heapob[m] < self.heapob[i]:
                    self.heapob[i], self.heapob[m] = self.heapob[m], self.heapob[i]  # switch values
            else:
                if self.heapob[m] < self.heapob[i]:
                    self.heapob[i], self.heapob[m] = self.heapob[m], self.heapob[i]
                    if self.heapob[m] > self.heapob[(m-1) // 2]:
                        self.heapob[m], self.heapob[(m-1)//2] = self.heapob[(m-1)//2], self.heapob[m]
                    self._trickle_down_min(i=m)

    def _remove_max(self) -> None:
        if self.size == 0:
            return
        self.heapob[0] = self.heapob[-1]  # switch last element with root
        self.heapob = self.heapob[:-1]  # remove last element
        self.size = len(self.heapob)  # update size
        self._trickle_down(i=0)

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
            self._trickle_down(i)
    
    def _bubble_up(self, i: int) -> None:
        pass
    
    def _bubble_up_max(self, i: int) -> None:
        pass
    
    def _bubble_up_min(self, i: int) -> None:
        pass


class InputHandler:
    @staticmethod
    def read_file(file_path: str) -> list:
        with open(file_path, 'r') as f:
            file_content = f.readlines()
        return InputHandler._parse_file(file_data=str(file_content))

    @staticmethod
    def _parse_file(file_data: str) -> list:
        return []  # TODO: parse file format


class UserHandler:
    """UserHandler: the program will show the user an option menu.
    In it, only the relevant methods will be shown to the user:
        - Build heap or Quit
        -> After a heap is built, all of the methods will show (+quit, print), but for build_heap.
        Only after deleting the heap (heap_delete), build_heap method will show.
    """
    def __init__(self) -> None:
        self.max_min_heap = MaxMinHeap()

    def print_heap(self):
        pass

    def _prompt_input_file(self) -> str:
        return ''

    def start(self):
        pass


class TestClass:
    @staticmethod
    def test_build_heap():
        import random
        fail_count = 0
        total_runs = 500
        for i in range(total_runs):
            random_list = []
            for i in range(random.randint(1, 10)):
                random_list.append(random.randint(0, 500))
            test_heap = MaxMinHeap()
            test_heap.build_heap(unsorted_heap=random_list)
            # print(f"List before building heap: {random_list}\nMaxMinHeap: {test_heap.heapob}")
            if not (TestClass._is_max_min_heap(test_heap)):
                print(f"Failed to build heap with array: {test_heap.heapob}, heap: {test_heap.heapob}")
                fail_count += 1
                if len(test_heap.heapob) != test_heap.size:
                    print(f"Wrong size!, heapleb: {len(test_heap.heapob)}, size: {test_heap.size}")
        if fail_count > 0:
            print(f"Fail/Total: {fail_count}/{total_runs}")
        else:
            print(f"All {total_runs} attempts PASSED.")

    @staticmethod
    def _is_max_min_heap(heap: MaxMinHeap):
        for index, value in enumerate(heap.heapob):
            if heap._level(index) % 2 == 0:  # max level
                for j in range(2 * index + 1, min(2 * index + 3, heap.size)):
                    # checking children to be smaller
                    if heap.heapob[j] > value:
                        # print(heap.heapob, j, index, heap.heapob[j], heap.heapob[index], heap._level(index))
                        return False
                for j in range(4 * index + 3, min(4 * index + 7, heap.size)):
                    # checking grand-children to be smaller
                    if heap.heapob[j] > value:
                        # print(heap.heapob, j, index, heap.heapob[j], heap.heapob[index], heap._level(index))
                        return False
            else:  # min level
                for j in range(2 * index + 1, min(2 * index + 3, heap.size)):
                    # checking children to be bigger
                    if heap.heapob[j] < value:
                        # print(heap.heapob, j, index, heap.heapob[j], heap.heapob[index], heap._level(index))
                        return False
                for j in range(4 * index + 3, min(4 * index + 7, heap.size)):
                    # checking grand-children to be bigger
                    if heap.heapob[j] < value:
                        # print(heap.heapob, j, index, heap.heapob[j], heap.heapob[index], heap._level(index))
                        return False
        return True


def main():
    pass


if __name__ == "__main__":
    # Start UserHandler
    x = MaxMinHeap()
    # x.build_heap([214,133,298])
    TestClass.test_build_heap()