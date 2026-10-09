class Solution:
    def firstUniqChar(self, s: str) -> int:
        store={}
        for char in s:
            store[char]=store.get(char,0)+1

        for i, char in enumerate(s):
            if store[char]==1:
                return i
        return -1         
        