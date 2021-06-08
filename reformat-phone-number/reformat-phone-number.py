class Solution:
    def reformatNumber(self, number: str) -> str:
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))