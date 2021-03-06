class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pat_word_hash = {}
        words = str.split()
        pat_len = len(pattern)
        str_len = len(words)
        
        if pat_len != str_len:
            return False
        else:
            i = 0
            j = 0
            while i < pat_len and j < str_len:
                if pat_word_hash.has_key(pattern[i]) == False:
                    if words[j] in pat_word_hash.values():
                        return False
                    pat_word_hash[pattern[i]] = words[j]
                    i = i + 1
                    j = j + 1
                else:
                    if pat_word_hash.get(pattern[i]) != words[j]:
                        return False
                    else:
                        i = i + 1
                        j = j + 1
            return True
