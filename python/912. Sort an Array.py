class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, mid, right):
            left_start = left
            right_start = mid + 1
            left_end = mid
            right_end = right

            sorted_arr = []
            while left_start <= left_end and right_start <= right_end:
                if nums[left_start] > nums[right_start]:
                    sorted_arr.append(nums[right_start])
                    right_start += 1
                else:
                    sorted_arr.append(nums[left_start])
                    left_start += 1
                
            if left_start <= left_end:
                sorted_arr += [nums[i] for i in range(left_start, left_end+1)]
            if right_start <= right_end:
                sorted_arr += [nums[i] for i in range(right_start, right_end+1)]
            
            return sorted_arr
        
        def merge_split(left, right):
            if left >= right:
                return [nums[left]]
            left_arr = merge_split(left, (right+left)//2)
            right_arr = merge_split((right+left)//2+1, right)
            arr = merge(left, (right+left)//2, right)
            nums[left:right + 1] = arr
            return arr
        
        return merge_split(0, len(nums)-1)


            
                
