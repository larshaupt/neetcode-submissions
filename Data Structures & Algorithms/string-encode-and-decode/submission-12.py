class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        index = 0
        output_string = []
        while index < len(s):
            j = s.index("#", index)
            leng_substring = int(s[index:j])
            output_string.append(s[j+1:j+1+leng_substring])
            index = j+1+leng_substring
        return output_string