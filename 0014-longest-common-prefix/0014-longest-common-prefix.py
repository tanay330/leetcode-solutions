class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        track=strs[0]

        for i in range(1,len(strs)):
            while not strs[i].startswith(track):
                track=track[:-1]

            if track=="":
                return ""
        return track            
        