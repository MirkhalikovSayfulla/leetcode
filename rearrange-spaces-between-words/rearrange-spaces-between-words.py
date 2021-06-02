class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        len_words = len(words)
        spaces = text.count(' ')

        if len_words == 1:
            return ''.join([words[0],  ' ' * spaces])

        separator = ' ' * (spaces // (len_words - 1))
        trailing = ' ' * (spaces % (len_words - 1))
        sentence = separator.join(words)
        return ''.join([sentence, trailing])