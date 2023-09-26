#!/usr/bin/python3
"""
way to calculate the minimal no of operations
"""


def minOperations(n):
    """
    minimal operations method
    """
    if n <= 1:
       return 0
    operations = 0
    A = 1
    copyall = 0
    paste = 0
    A_copied = 0
    while A < n:
          if n % A == 0:
               copyall += 1
               A_copied = A
          paste += 1
          operations = copyall + paste
          A += 1
     return operations
