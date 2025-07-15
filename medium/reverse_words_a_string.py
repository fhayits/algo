class Solution:
    def join(self, words, sep=" "):
        if not words:
            return ""
        result = words[0]
        for word in words[1:]:
            result += sep + word
        
        return result

    def split(self, word):
        result = []
        pos = 0
        start_pos = 0
        n = len(word)

        while pos < n:
            while pos < n and word[pos] == " ":
                pos += 1
            if pos >= n:
                break

            start_pos = pos    
            while pos < n and word[pos] != " ":
                pos += 1

            result.append(word[start_pos:pos])
        return result

    def reverseWords(self, s: str) -> str:
        words = self.split(s)
        i, j = 0, len(words)-1
        
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        return self.join(words)
