# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import defaultdict

def is_ransomeware(r,m) :
    if len(r) > len(m) :
        return  False

    rh = defaultdict(int)
    for c in r :
       rh[c]+=1

    mh = defaultdict(int)
    for c in m :
       mh[c]+=1

    for c in r:
        if rh[c] > mh[c] :
            return False

    return True

r = "aa"
m = "aab"
print(is_ransomeware(r,m))


r = "aa"
m = "ab"
print(is_ransomeware(r,m))


r = "a"
m = "b"
print(is_ransomeware(r,m))


# another solution
from collections import Counter

def canConstruct( ransomNote, magazine):
    # Count characters in both
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    # Check if ransomNote's counts are all satisfied by magazine
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True

# another solution
from collections import Counter
def canConstruct(ransomNote, magazine):
    return not (Counter(ransomNote) - Counter(magazine))


print(canConstruct("qww","qqww"))