class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        dist = [1 for i in range(len(ratings))]
        ratings_with_index = [(ratings[i], i) for i in range(len(ratings))]
        ratings_with_index.sort(key=lambda x:x[0])
        min_rating, _ = ratings_with_index[0]
        for i in range(1, len(ratings_with_index)):
            rating, index = ratings_with_index[i]
            if rating == min_rating:
                continue
            if index == 0:
                if ratings[index+1] < rating:
                    dist[index] = dist[index+1] + 1
            elif index == len(ratings) - 1:
                if ratings[index-1] < rating:
                    dist[index] = dist[index-1] + 1
            elif ratings[index-1] < rating and ratings[index+1] < rating:
                dist[index] = max(dist[index-1], dist[index+1]) + 1
            elif ratings[index-1] < rating:
                dist[index] = dist[index-1] + 1
            elif ratings[index+1] < rating:
                dist[index] = dist[index+1] + 1
        return sum(dist)
                