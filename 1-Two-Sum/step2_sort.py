class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = sorted([(num, index) for index, num in enumerate(nums)])
        front = 0
        rear = len(nums) - 1
        while front < rear:
            sum_ = num_and_index[front][0] + num_and_index[rear][0]
            if sum_ < target:
                front += 1
                continue
            if target < sum_:
                rear -= 1
                continue
            return [num_and_index[front][1], num_and_index[rear][1]]
