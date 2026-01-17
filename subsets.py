# Time:  O(n * 2^n)
# Space: O(1)
# Pattern: Backtracking (Iterative Cascading)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Cascading approach: for each new element, 
        # add it to all existing subsets to create new ones
        
        # 1. Start with empty subset
        nums.sort()
        result = [[]]
        
        # 2. For each number, extend all existing subsets
        for i in xrange(len(nums)):
            # 2a. Get current size (avoid infinite loop)
            size = len(result)
            
            # 2b. For each existing subset, create a new one with nums[i]
            for j in xrange(size):
                # Copy existing subset and add new element
                result.append(list(result[j]))
                result[-1].append(nums[i])
        
        # Example: nums = [1,2]
        # Start: [[]]
        # After 1: [[], [1]]
        # After 2: [[], [1], [2], [1,2]]
        return result


# Time:  O(n * 2^n)
# Space: O(1)
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            result.append(cur)
            i += 1

        return result


# Time:  O(n * 2^n)
# Space: O(1)
class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, cur, nums):
        if not nums:
            return [cur]

        return self.subsetsRecu(cur, nums[1:]) + self.subsetsRecu(cur + [nums[0]], nums[1:])


