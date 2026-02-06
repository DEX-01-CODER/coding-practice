"""
LeetCode #242 — Valid Anagram
Topic: Strings + Hash Map (Frequency Counting)

PROBLEM:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

DEFINITION:
Two strings are anagrams if:
- They have the same length
- They contain the same characters with the same frequencies
- Order does NOT matter

APPROACHES DISCUSSED (3):
1) Sort both strings and compare (easy, but O(n log n))
2) Build two frequency dictionaries and compare (O(n))
3) One dictionary: count s, subtract using t (O(n), clean)

TIME/SPACE NOTES:
- Sorting: Time O(n log n), Space O(n)
- Hash counting: Time O(n)
  Space is O(1) if alphabet size is fixed (e.g., lowercase letters), otherwise O(k) unique chars.
"""

from typing import Dict


# -----------------------------
# Solution 1: Sorting
# -----------------------------
class SolutionSorting:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# -----------------------------
# Solution 2: Two Dictionaries (your structure)
# -----------------------------
class SolutionTwoDicts:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count: Dict[str, int] = {}
        t_count: Dict[str, int] = {}

        for ch in s:
            if ch in s_count:
                s_count[ch] += 1
            else:
                s_count[ch] = 1

        for ch in t:
            if ch in t_count:
                t_count[ch] += 1
            else:
                t_count[ch] = 1

        return s_count == t_count


# -----------------------------
# Solution 3: One Dictionary (count + subtract)
# -----------------------------
class SolutionOneDict:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count: Dict[str, int] = {}

        # Count characters in s
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Subtract characters in t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
