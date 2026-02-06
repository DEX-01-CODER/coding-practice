
"""
LeetCode #1 — Two Sum

Problem:
Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.

Rules:
- You may assume that each input would have exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers we have seen so far
        # key   -> number
        # value -> index where the number appeared
        seen = {}

        for i, num in enumerate(nums):
            # Number needed to reach the target
            needed = target - num

            # Check BEFORE storing to avoid using the same element twice
            if needed in seen:
                return [seen[needed], i]

            # Store current number and its index
            seen[num] = i
        # Problem guarantees exactly one solution, so this line is never reached
        return []

























"""--------------------TIME & SPACE COMPLEXITY — QUICK NOTES------------------------"""

"""

Time Complexity:
- Measures how the runtime of an algorithm grows as input size (n) increases.
- It does NOT measure actual execution time in seconds.
- Focuses on the growth pattern as input becomes large.

Common Time Complexities:
- O(1): Constant time (e.g., accessing arr[i])
- O(n): Linear time (e.g., looping through an array once)
- O(n^2): Quadratic time (e.g., nested loops)
- O(log n): Logarithmic time (e.g., binary search)
- O(n log n): Linearithmic time (e.g., merge sort)

How to Determine Time Complexity:
- One loop over n elements → O(n)
- Nested loops → O(n^2)
- Loop + constant work → O(n)
- No loops → O(1)

Space Complexity:
- Measures the extra memory used by an algorithm as input size grows.
- Does NOT include the input array itself.
- Includes additional data structures or recursion stack.

Common Space Complexities:
- O(1): Constant extra space (only variables)
- O(n): Extra data structure grows with input size (array, list, set, dict)

Examples:
- Looping through an array without extra storage → O(1) space
- Using a set or dictionary to store n elements → O(n) space

Key Interview Notes:
- Built-in functions like max(), min(), sum() still take O(n) time.
- Optimizing often means trading space for time.
- Always be able to explain WHY your solution has a certain complexity.
"""




"""--------------------Array Basics------------------------"""

# def print_elements(arr):
#     for i in arr:
#         print(i)

# def find_max(arr):
#     if arr == []:
#         return None
#     else:
#         return max(arr)

# def count_occurrences(arr, target):
#     count = 0

#     for item in arr:
#         if item == target:
#             count += 1

#     return count

# test1 = [1, 2, 3, 4, 5]
# test2 = [5, 5, 5, 5]
# test3 = []
# test4 = [10]

# print_elements(arr=test1)
# print("Max:", find_max(test1))
# print("Count of 5:", count_occurrences(test2, 5))
# print("Max empty:", find_max(test3))
