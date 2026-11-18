class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1hash = {} # letter: frequency

        for x in s: 
            if x in string1hash:
                string1hash[x] += 1
            else: 
                string1hash[x] = 1
        
        for y in t:
            if y not in string1hash:
                return False
            else:
                if string1hash[y]-1 == 0:
                    string1hash.pop(y)
                else: 
                    string1hash[y] -= 1
        
        if not string1hash:
            return True
        else:
            return False