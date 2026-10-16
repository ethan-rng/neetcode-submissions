class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            seen[''.join(sorted(s))].append(s)

        
        res = []
        for v in seen.values():
            res.append(v)

        return res