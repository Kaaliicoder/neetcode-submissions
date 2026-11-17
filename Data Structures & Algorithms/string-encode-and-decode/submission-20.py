class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "Asad"
        return 'ganok'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "Asad":
            return []
        return s.split('ganok')