class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(S: str) -> str:
            str_s = ''
            for i in range(len(S)):
                if S[i] != '#':
                    str_s += S[i]
                else:
                    str_s = str_s[:-1]
            return str_s
        return get_str(S) == get_str(T)