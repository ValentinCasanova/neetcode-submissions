class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create a string from list of string
        # With a delimiter (int)($) where int is
        # the lenght of the following word
        res = ""
        for word in strs:
            res += f'{len(word)}${word}'
        return res

    def decode(self, s: str) -> List[str]:
        # Iterate over string, using predefined delimiter
        # To create list
        res = []
        print(s)
        word_count, word_ptr = 0, 0
        while word_ptr < len(s):
            curr_word = ''
            length = ''
            while s[word_count] != "$":
                length += s[word_count]
                word_count += 1
            length = int(length)
            word_ptr = word_count + 1
            word_end = word_ptr + length
            while word_ptr < word_end:
                curr_word += s[word_ptr]
                word_ptr += 1
            print(word_end)
            word_count = word_end
            res.append(curr_word)
        return res

