class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checking length
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        # Building freq map for s
        for i in s:
            if i in freq_s:
                freq_s[i] += 1
            else:
                freq_s[i] = 1
        # Building freq map for t
        for i in t:
            freq_t[i] = freq_t.get(i, 0)+1
        # Compare both
        return freq_s == freq_t

        # return (sorted(s)==sorted(t))
    
s = input()
t = input()
sol = Solution()
print(sol.isAnagram(s,t))    
