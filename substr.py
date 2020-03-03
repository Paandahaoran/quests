def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        max_length = 0
        i = 0
        j = 0
        substr = ""
        existed_char = set()
        while i<len(s) and j<len(s):
            if s[j] not in existed_char:
                existed_char.add(s[j])
                length = j-i+1
                print(length)
                j += 1
            else:
                existed_char = set()
                max_length = max(length,max_length)
                length = 0
                i += 1
                j = i
        if s[-1] not in existed_char:
            length += 1
        max_length = max(max_length,length)
        return max_length


print(lengthOfLongestSubstring("pwwkew"))
