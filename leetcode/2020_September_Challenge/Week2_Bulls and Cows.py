class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0; B = 0
        for ch in set(guess):
            B += min(secret.count(ch), guess.count(ch))
            
        for i, ch in enumerate(guess):
            if ch == secret[i]:
                A += 1

        return str(A) + 'A' + str(B - A) + 'B'