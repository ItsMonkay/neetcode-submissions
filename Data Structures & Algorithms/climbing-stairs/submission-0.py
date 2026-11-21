class Solution:
    def climbStairs(self, n: int) -> int:
        db = {}
        db [0] = 1
        db [1] = 2
        if n == 1: 
            return 1
        elif n == 2:
            return 2
        for x in range(2, n): 
            db[x] = db[x-1] + db[x-2]

        return db[n-1]
