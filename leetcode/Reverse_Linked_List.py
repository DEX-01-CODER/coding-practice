"""
LeetCode #206 — Reverse Linked List
Topic: Linked List
Pattern: Pointer Reversal (Iterative)

PROBLEM:
Given the head of a singly linked list, reverse the list and return the new head.

KEY IDEA (VERY IMPORTANT):
- A linked list is made of nodes.
- Each node has:
    1) a value
    2) a pointer (next) to the next node
- Reversing a linked list means reversing the DIRECTION of the pointers,
  NOT moving values or creating a new list.

MENTAL MODEL:
At every step, the list is split into two parts:

    (reversed part)     (unprocessed part)

We move ONE node at a time from the unprocessed part
to the front of the reversed part.

CORE STEPS (REPEATED IN LOOP):
1. Save the address of the next node (so we don't lose the list)
2. Reverse the pointer of the current node
3. Move prev and curr forward

INITIAL STATE:
- prev = None
- curr = head

TIME COMPLEXITY:
- O(n) — each node is visited once

SPACE COMPLEXITY:
- O(1) — no extra data structures used
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # Head of the reversed part
        curr = head          # Current node being processed

        while curr is not None:
            # Step 1: Save the next node's address
            next_node = curr.next

            # Step 2: Reverse the pointer of the current node
            curr.next = prev

            # Step 3: Move prev and curr forward
            prev = curr
            curr = next_node

        # At the end, prev points to the new head of the reversed list
        return prev
