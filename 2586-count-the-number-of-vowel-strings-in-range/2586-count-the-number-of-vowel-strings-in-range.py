class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:

        tracker=0
        l1=["a","e","i","o","u","A","E","I","O","U"]
        for character in words[left:right+1]:
            if character[0] in l1:
                if character[-1] in l1:
                    tracker+=1
               

        return tracker         
        