class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = ""
        for s in strs:
            encoded_msg += str(len(s)) + "." + s

        return encoded_msg


    def decode(self, s: str) -> List[str]:

        decoded_msg = []
        i = 0
        while i < len(s):

            s_len = ""
            while s[i] != ".":
                s_len += s[i]
                i += 1
            s_len = int(s_len)

            decoded_msg.append(s[i + 1:i + 1 + s_len])
            i += 1 + s_len

        return decoded_msg
