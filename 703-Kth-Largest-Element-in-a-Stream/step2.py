from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest_elements = self.heapify(nums)

    def add(self, val: int) -> int:
        self.push(self.k_largest_elements, val)
        return self.k_largest_elements[0]

    def _parent(self, child: int) -> int:
        return (child - 1) // 2

    def _left_child(self, parent: int) -> int:
        return parent * 2 + 1

    def _right_child(self, parent: int) -> int:
        return (parent + 1) * 2

    def _shift_up(self, heap: List[int], index: int):
        while index > 0 and heap[index] < heap[self._parent(index)]:
            heap[index], heap[self._parent(index)] = (
                heap[self._parent(index)],
                heap[index],
            )
            index = self._parent(index)

    def _shift_down(self, heap: List[int], index: int):
        heap_size = len(heap)
        while True:
            smallest = index
            if (
                self._left_child(index) < heap_size
                and heap[self._left_child(index)] < heap[smallest]
            ):
                smallest = self._left_child(index)
            if (
                self._right_child(index) < heap_size
                and heap[self._right_child(index)] < heap[smallest]
            ):
                smallest = self._right_child(index)

            if smallest == index:
                break
            heap[index], heap[smallest] = (
                heap[smallest],
                heap[index],
            )
            index = smallest

    def push(self, heap: List[int], num: int):
        heap_size = len(heap)
        if heap_size < self.k:
            heap.append(num)
            self._shift_up(heap, len(heap) - 1)
        elif num > heap[0]:
            heap[0] = num
            self._shift_down(heap, 0)

    def pop(self, heap: List[int]) -> int:
        head = heap[0]
        tail = heap.pop()
        if heap:
            heap[0] = tail
            self._shift_down(heap, 0)
        return head

    def heapify(self, nums: List[int]) -> List[int]:
        heap: List[int] = []
        for index in range(len(nums)):
            self.push(heap, nums[index])
        return heap
