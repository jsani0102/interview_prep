# https://leetcode.com/problems/remove-duplicate-letters/

def removeDuplicateLetters(s):
    counts = [0] * 26
    
    for ch in s:
        if counts[ord(ch) - ord('a')] == 0:
            counts[ord(ch) - ord('a')] = 1
        
    s = ""
    for i in range(26):
        if counts[i] == 1:
            s += unichr(ord('a') + i)
    return s

assert(removeDuplicateLetters("bcabc") == "abc")
assert(removeDuplicateLetters("cbacdcbc") == "abcd")