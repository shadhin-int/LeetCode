class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item for item, count in Counter(nums).most_common(k)]
        