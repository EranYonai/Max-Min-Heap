from max_min_heap import MaxMinHeap
from test_heap import TestClass
from dataclasses import dataclass
from typing import Union
import sys

from drawtree import draw_level_order


class InputHandler:
    @staticmethod
    def read_file_and_parse(file_path: str) -> list:
        file_path = file_path.strip()
        with open(file_path, 'r') as f:
            file_content: list = f.readlines()
        return InputHandler.get_first_input(InputHandler._parse_file(file_data=file_content))

    @staticmethod
    def _parse_file(file_data: list) -> list:
        file_data = [line.rstrip('\n').replace('[', '').replace(']', '') for line in file_data]
        file_data = [line.split(',') for line in file_data]
        return file_data

    @staticmethod
    def get_first_input(file_data: list) -> list:
        return [int(element) for element in file_data[0]]


class UserHandler:
    """UserHandler: the program will show the user an option menu.
    In it, only the relevant methods will be shown to the user:
        - Build heap or Quit
        -> After a heap is built, all of the methods will show (+quit, print), but for build_heap.
        Only after deleting the heap (heap_delete), build_heap method will show.
    """

    def __init__(self) -> None:
        self.max_min_heap = MaxMinHeap()
        self.alive = True

    def _print_heap(self):
        draw_level_order(str(self.max_min_heap.heapob))
        print(f"Heap size: {self.max_min_heap.size}")

    def get_user_input(self, prompt) -> Union[str, int]:
        user_input = input(prompt).strip()
        try:
            m = int(user_input)
            return m
        except:  # pylint: disable=E722, W0702
            return user_input

    def _build_cli_heap(self):
        stop = False
        print("To stop inserting elements, write a not integer, to print write print")
        while not stop:
            inp = self.get_user_input(prompt="Please enter an element for insertion: ")
            if self._is_str(inp):
                stop = True
            else:
                self.max_min_heap.heap_insert(key=inp)  # type: ignore
                self._print_heap()

    def operate_on_heap(self, action):
        if action > Actions.NUM_ACTIONS:
            print("Invalid action.")
            return
        if action not in [1, 2, 3] and self.max_min_heap.size == 0:
            print("Invalid action")
            return
        if action == Actions.EXIT:
            print("Bye Bye...")
            self.alive = False
        elif action == Actions.BUILD_HEAP:
            inp = self.get_user_input(prompt="1 to build with cli, 2 to heap from file: ")
            if inp == 1:
                self._build_cli_heap()
            else:
                inp = self.get_user_input(prompt="Enter full file location: ")
                if self._is_str(inp):
                    self.max_min_heap.build_heap(InputHandler.read_file_and_parse(file_path=inp))  # type: ignore
                else:
                    print("Input is not string.")
        elif action == Actions.PRINT_HEAP:
            self._print_heap()
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
            key = self.get_user_input("Enter value to insert: ")
            if self._is_str(key):
                print(f"Invalid index '{key}' - not a number.")
            elif key == sys.maxsize:
                print(f"Invalid number: The number {key} is not allowed. Enter a smaller number")
            else:
                self.max_min_heap.heap_insert(key=key)  # type: ignore
        elif action == Actions.HEAP_DEL:
            idx = self.get_user_input("Enter an index of an item to delete (1 is the root): ")
            if self._is_str(idx):
                print(f"Invalid index '{idx}' - not a number.")
            elif self.max_min_heap.size <= idx-1:  # type: ignore
                print(self.max_min_heap.size)
                print(f"Invalid index {idx} - not in range.")
            else:
                self.max_min_heap.heap_delete(i=idx)  # type: ignore
        elif action == Actions.RUN_TESTS:
            print("Running tests... it might take some time, depends on your hardware.")
            print("Tests are randomizing lists [1-512 length], with integers [-2000-2000], running 1000 times each.")
            self._run_tests()

    def _print_base_menu(self):
        print("""Options menu:
            1) Exit.
            2) Build Heap.
            3) Run Tests.""", end='')

    def _print_extended_menu(self):
        print("""\n\t4) Print Heap.
            5) Extract Max.
            6) Extract Min.
            7) Insert.
            8) Delete.""")

    @staticmethod
    def _is_str(action):
        return isinstance(action, str)

    def _run_tests(self):
        print("Testing Build Heap")
        build_test_results = TestClass.test_build_heap()
        print("Testing Heap Insert")
        insert_test_results = TestClass.test_insert_heap()
        print("Testing Extract min/max (no printing), extracting every element from heap...")
        extract_test_results = TestClass.test_remove_min_max()
        print("Testing Heap Delete, removing every element from the heap...")
        delete_test_results = TestClass.test_delete()
        print("Done!")
        print(f"Build test results: {build_test_results}")
        print(f"Insert test results: {insert_test_results}")
        print(f"Extract test results: {extract_test_results}")
        print(f"Delete test results: {delete_test_results}")

    def show_menu(self):
        if self.max_min_heap.size == 0:
            print("Heap is empty, build heap in order to see extended menu.")
            self._print_base_menu()
        else:
            self._print_base_menu()
            self._print_extended_menu()


@dataclass
class Actions:
    EXIT = 1
    BUILD_HEAP = 2
    RUN_TESTS = 3
    PRINT_HEAP = 4
    HEAPEX_MAX = 5  # EX=EXTRACT
    HEAPEX_MIN = 6
    HEAP_INS = 7
    HEAP_DEL = 8
    NUM_ACTIONS = 8
