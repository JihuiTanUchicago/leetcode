class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        head_prefix_sum = [0]
        tail_prefix_sum = [0]
        for i in range(k):
            head_prefix_sum.append(head_prefix_sum[-1] + cardPoints[i])
            tail_prefix_sum.append(tail_prefix_sum[-1] + cardPoints[-(i+1)])
        tail_prefix_sum = tail_prefix_sum[::-1]
        max_score = 0
        for i in range(k+1):
            max_score = max(head_prefix_sum[i] + tail_prefix_sum[i], max_score)
        return max_score