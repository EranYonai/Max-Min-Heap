from max_min_heap import MaxMinHeap
from test_heap import TestClass


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

def main():
    pass

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