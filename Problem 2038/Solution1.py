class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return sum(1 if colors[i] == 'A' else -1 for i in range(1, len(colors) - 1) if colors[i] == colors[i-1] == colors[i+1]) > 0
