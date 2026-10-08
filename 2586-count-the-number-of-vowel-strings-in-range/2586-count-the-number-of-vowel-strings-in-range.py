class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:

        tracker=0
        s1="aeiouAEIOU"
        for character in words[left:right+1]:
            if character[0] in s1:
                if character[-1] in s1:
                    tracker+=1
               

        return tracker         
        