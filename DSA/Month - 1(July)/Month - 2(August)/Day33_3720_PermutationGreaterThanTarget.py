class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Match target as much as possible
        i = 0

        while i < len(target):
            idx = ord(target[i]) - ord('a')

            if freq[idx] == 0:
                break

            freq[idx] -= 1
            i += 1

        # Try to make the current position greater
        if i < len(target):

            idx = ord(target[i]) - ord('a')

            for j in range(idx + 1, 26):

                if freq[j] > 0:

                    freq[j] -= 1

                    ans = target[:i] + chr(j + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * freq[k]

                    return ans

        # Backtrack
        i -= 1

        while i >= 0:

            # Restore target[i]
            idx = ord(target[i]) - ord('a')
            freq[idx] += 1

            # Try the smallest character greater than target[i]
            for j in range(idx + 1, 26):

                if freq[j] > 0:

                    freq[j] -= 1

                    ans = target[:i] + chr(j + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * freq[k]

                    return ans

            i -= 1

        return ""