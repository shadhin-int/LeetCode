class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        max_from_right = arr[-1]
    
        for i in range(len(arr) - 1)[::-1]:
            ans.append(max_from_right)
            max_from_right = max(max_from_right, arr[i])
        
        return ans[::-1]