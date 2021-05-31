class Solution:
    def reformatDate(self, date: str) -> str:
        month = {m: i+1 for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
        d, m, y = date.split()
        return "{}-{:02d}-{:02d}".format(y, month[m], int(d[:-2]))