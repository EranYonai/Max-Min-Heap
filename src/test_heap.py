import random

from max_min_heap import MaxMinHeap


class TestClass:
    @staticmethod
    def test_build_heap():
        fail_count = 0
        total_runs = 500
        for i in range(total_runs):
            random_list = []
            for i in range(random.randint(1, 15)):
                random_list.append(random.randint(-2000, 2000))
            test_heap = MaxMinHeap()
            test_heap.build_heap(unsorted_heap=random_list)
            if not (TestClass._is_max_min_heap(test_heap)):
                print(f"Failed to build heap with array: {random_list}, heap: {test_heap.heapob}")
                fail_count += 1
                if len(test_heap.heapob) != test_heap.size:
                    print(f"Wrong size!, heapleb: {len(test_heap.heapob)}, size: {test_heap.size}")
        if fail_count > 0:
            return (f"Fail/Total: {fail_count}/{total_runs}")
        else:
            return (f"All {total_runs} attempts PASSED.")

    @staticmethod
    def test_insert_heap():
        fail_count = 0
        total_runs = 500
        for i in range(total_runs):
            random_list = []
            for i in range(random.randint(1, 512)):
                random_list.append(random.randint(-2000, 2000))
            test_heap = MaxMinHeap()
            for element in random_list:
                test_heap.heap_insert(key=element)
            if not (TestClass._is_max_min_heap(test_heap)):
                print(f"Failed to build heap with array: {random_list}, heap: {test_heap.heapob}")
                fail_count += 1
                if len(test_heap.heapob) != test_heap.size:
                    print(f"Wrong size!, heapleb: {len(test_heap.heapob)}, size: {test_heap.size}")
        if fail_count > 0:
            return (f"Fail/Total: {fail_count}/{total_runs}")
        else:
            return (f"All {total_runs} attempts PASSED.")

    @staticmethod
    def _is_max_min_heap(heap: MaxMinHeap):
        if heap.size == 0:
            return False
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


if __name__ == "__main__":
    build_test_results = TestClass.test_build_heap()
    insert_test_results = TestClass.test_insert_heap()
    print(f"Build test results: {build_test_results}")
    print(f"Insert test results: {insert_test_results}")