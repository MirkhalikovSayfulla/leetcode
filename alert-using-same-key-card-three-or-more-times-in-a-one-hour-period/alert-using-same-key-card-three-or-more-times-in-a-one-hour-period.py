class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict
        ans = []
        d = defaultdict(list)
        for i in range(len(keyName)):
            d[keyName[i]].append(keyTime[i])
        for i in d:
            d[i].sort()
            for j in range(len(d[i])-2):
                if abs(int(d[i][j][0:2]) - int(d[i][j+2][0:2]))==0:
                    if i not in ans:
                        ans.append(i)
                        break
                elif (abs(int(d[i][j][0:2]) - int(d[i][j+2][0:2]))==1 and int(d[i][j][3:5]) >= int(d[i][j+2][3:5])):
                    if i not in ans:
                        ans.append(i)
                        break
        return sorted(ans) 