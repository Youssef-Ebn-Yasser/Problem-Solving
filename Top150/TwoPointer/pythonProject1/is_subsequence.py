#  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
from operator import truediv

# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


#Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true


# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# ===============================================  sol ========================================================


# loop in first on with original_pointer [ y o u s e f ]
# and for sub with sub_pointer start from zero and not plus only if find this charachter
# then plus by one
# in one loop we can know if we find this or not
# if the lenght of pointer == lenght of sub and we start from zero then we find this sub string
# and should go out this function
# to avoid index null exception


# original_string ="ahbgdc"
# sub_string = "abc"

original_string ="abc"
sub_string = "b"


def isSubsequence(s, t):
    sub_pointer = 0

    if s == "":
        return True

    for i in range(len(t)):
        if t[i] == s[sub_pointer]:
            sub_pointer += 1

        if sub_pointer >= len(s):
            return True

    return False


# print(sub_pointer)
print(isSubsequence("ahbgdc","abc"))






