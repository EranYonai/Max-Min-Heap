from max_min_heap import MaxMinHeap
from test_heap import TestClass
from dataclasses import dataclass
import sys

from drawtree import draw_level_order


class InputHandler:
    @staticmethod
    def read_file_and_parse(file_path: str) -> list:
        with open(file_path, 'r') as f:
            file_content: list = f.readlines()
        return InputHandler._parse_file(file_data=file_content)

    @staticmethod
    def _parse_file(file_data: list) -> list:
        file_data = [line.rstrip('\n').remove('[').remove(']') for line in file_data]
        file_data = [line.split(',') for line in file_data]
        return file_data

    @staticmethod
    def get_first_input(file_data: list) -> list:
        return file_data[0]


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
    
    def _get_user_input(self, prompt):
        user_input = input(prompt).strip()
        try:
            m = int(user_input)
            return m
        except:
            return user_input

    def _build_cli_heap(self):
        pass

    def _operate_on_heap(self, action):
        if action == Actions.EXIT:
            pass
        elif action == Actions.BUILD_HEAP:
            self._build_cli_heap()
        elif action == Actions.PRINT_HEAP:
            draw_level_order(str(self.max_min_heap.heapob))
        elif action == Actions.HEAPEX_MAX:
            if self.max_min_heap.size < 1:
                print("Heap is empty, can't extract.")
            else:
                self.max_min_heap.heap_extract_max()
        elif action == Actions.HEAPEX_MIN:
            if self.max_min_heap.size < 1:
                print("Heap is empty, can't extract.")
            else:
                self.max_min_heap.heap_extract_min()
        elif action == Actions.HEAP_INS:
            key = self._get_user_input("Enter value to insert: ")
            if self._is_str(key):
                print("Invalid index '%s' - not a number." % key)
            elif key == sys.maxsize:
                print("Invalid number: The number %d shouldn't be used. Enter a smaller number" % key)
            else:
                self.__heap.heapInsert(key)
        elif action == Actions.HEAP_DEL:
            idx = self.__getUserInt("Put index of an item to delete: ")
            if IsStr(idx):
                print("Invalid index '%s' - not a number." % idx)
            elif not self.__heap.validIdx(idx):
                print("Invalid index %d - not in range." % idx)
            else:
                self.__heap.heapDelete(idx)
        elif action == Actions.HEAPSORT:
            self._userHeapsort()

        return len(self.__heap) > 0

    def start(self):
        pass
    
    def _print_base_menu(self):
        print("""Options menu:
                1) Exit.
                2) Build Heap.
                """)
    
    def _print_extended_menu(self):
        print("""3) Print Heap.
                4) Extract Max.
                5) Extract Min.
                6) Insert.
                7) Delete.
                8) Heap-Sort.
                    """)
        print("Type 'help' to show the menu again.")

    @staticmethod
    def _is_str(action):
        return type(action) == str


@dataclass
class Actions:
    EXIT = 1
    BUILD_HEAP = 2
    PRINT_HEAP = 3
    HEAPEX_MAX = 4  # EX=EXTRACT
    HEAPEX_MIN = 5
    HEAP_INS = 6
    HEAP_DEL = 7
    HEAPSORT = 8
    NUM_ACTIONS = 8

if __name__ == "__main__":
    # Start UserHandler
    x = MaxMinHeap()
    # for element in [5, 300, 74, 219, 200, 147, 169, 459, 141, 289]:
    #     x.heap_insert(element)
    # print(TestClass._is_max_min_heap(x))
    build_test_results = TestClass.test_build_heap()
    insert_test_results = TestClass.test_insert_heap()
    print(f"Build test results: {build_test_results}")
    print(f"Insert test results: {insert_test_results}")
