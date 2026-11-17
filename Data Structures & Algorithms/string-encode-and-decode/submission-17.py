class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "Asad"
        return ' '.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "ASad":
            return []
        return s.split('asad')