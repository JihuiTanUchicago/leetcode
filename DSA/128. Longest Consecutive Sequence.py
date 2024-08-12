from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        table = defaultdict(int)
        for num in nums:
            lower = table[num-1]
            upper = table[num+1]
            value = lower + upper + 1
            table[num-lower] = value
            table[num+upper] = value
        return max(list(table.values()))

"""
Intuition: we want a O(n) time solution
The question asks us to output an integer, not the actual consecutive elements sequence
Normally, we would want to sort the array, and the algorithm would keep track of a `max_num` variable regarding the length of the longest consecutive elements sequence. The actual algorithm would be something like:
```python
nums = sorted(nums)
max_length = 1
length = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
```
Observe that we are basically comparing all the locally maximal `length` values. If we could compute an array of these `length` values in O(n) time, then we could just use `max(length_arr)` to find the longest consecutive sequence.

Obviously, we cannot use `sort()` since that is O(nlogn). If given an unsorted array, we could instead keep track of a maximal `length` value's associated lower bound and upper bound. In another word, whenever we encounter a number in the array, we could see whether it could serve as a lower bound or upper bound of an associated maximal `lenght`. If we turn nums into `set(nums)`, we could actually guarantee that each number is unique, and it would actually be the case that each num we encounter has to be an upper bound or lower bound. And it could potentially connect two ranges into one by serving as the intermediary(think [2-4], 5, and [6-9]).

So, the solution would be having an dictionary that has numbers as the keys and the associated lengths as values. dict[num] = length means that num is either an upper bound or lower bound of a range with length of `length`.
"""