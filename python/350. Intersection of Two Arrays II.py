from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # What if the given array is already sorted?
        # # ANS: two pointer
        # nums1.sort()
        # nums2.sort()
        
        # print(nums1, nums2)
        # index1, index2 = 0, 0
        # output = []
        # freq = 0
        # cur_num = float('-inf')

        # while index1 < len(nums1) and index2 < len(nums2):
        #     if freq != 0 and cur_num != nums1[index1]:
        #         output += [cur_num] * freq
        #         freq = 0
    
        #     if nums1[index1] == nums2[index2]:
        #         cur_num = nums1[index1]
        #         index1 += 1
        #         index2 += 1
        #         freq += 1
        #     elif nums1[index1] < nums2[index2]:
        #             index1 += 1
        #     else:
        #         index2 += 1

        # if freq != 0:
        #     output += [cur_num] * freq

        # return output

        # intersect_map = defaultdict(int)
        # nums1_map = defaultdict(int)
        # nums2_map = defaultdict(int)

        # for num in nums1:
        #     nums1_map[num] += 1
        
        # for num in nums2:
        #     nums2_map[num] += 1
        
        # num_set = set(nums1) | set(nums2)
        # for num in num_set:
        #     intersect_map[num] = min(nums1_map[num], nums2_map[num])
        
        # output = []
        # for num in intersect_map:
        #     freq = intersect_map[num]
        #     if freq == 0:
        #         continue
        #     output += [num] * freq
        
        return output