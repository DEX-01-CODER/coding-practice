"""
LeetCode #217 — Contains Duplicate
Topic: Arrays + Hash Set
Pattern: "Have I seen this before?"

PROBLEM:
Given an integer array nums,
return True if any value appears at least twice in the array,
and return False if every element is distinct.

KEY OBSERVATIONS:
- We only care about WHETHER a duplicate exists.
- We do NOT care about:
  - the index
  - how many times it appears
  - which number is duplicated
- The moment we detect a duplicate, we can stop early.

BRUTE FORCE IDEA:
- Compare every element with every other element.
- Time: O(n^2)
- Space: O(1)
→ Too slow for large inputs.

OPTIMIZED IDEA:
- As we iterate, keep track of numbers we have already seen.
- If we see the same number again → duplicate found.

DATA STRUCTURE CHOICE:
- HashSet (or Dictionary used like a set)

WHY HASHSET?
- Stores only UNIQUE values
- Fast O(1) average lookup
- Perfect for "existence" checks

CORE QUESTION DURING ITERATION:
    "Have I already seen this number?"

TIME COMPLEXITY:
- O(n) — single pass through the array

SPACE COMPLEXITY:
- O(n) — storing seen numbers
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # HashSet to store numbers we have seen so far
        seen = set()

        for num in nums:
            # If the number is already in the set,
            # a duplicate exists
            if num in seen:
                return True

            # Otherwise, record that we have seen this number
            seen.add(num)

        # If we finish the loop with no duplicates found
        return False
