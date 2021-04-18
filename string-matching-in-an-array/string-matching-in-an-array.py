class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for idx, wo in enumerate(words):
            if wo in "#".join(words[idx+1:]) or wo in "#".join(words[:idx]):
                res.append(wo)
        
        return res