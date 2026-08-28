class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have:
        # even n  -> 0 odd frequencies
        # odd n   -> 1 odd frequency
        odd = sum(c % 2 for c in cnt)

        if odd != n % 2:
            return ""

        # Middle character
        middle = ""
        if n % 2:
            for i in range(26):
                if cnt[i] % 2:
                    middle = chr(ord('a') + i)
                    break

        # Characters available for the left half
        half_cnt = [c // 2 for c in cnt]
        half_len = n // 2

        left = []

        # Check whether the current prefix can still
        # produce some palindrome > target.
        def can_be_greater():
            # Make the LARGEST possible remaining left half.
            candidate_left = left[:]

            for i in range(25, -1, -1):
                candidate_left.extend(
                    [chr(ord('a') + i)] * half_cnt[i]
                )

            left_part = ''.join(candidate_left)

            # Construct the largest possible palindrome
            palindrome = left_part + middle + left_part[::-1]

            return palindrome > target

        # Build the left half from left to right.
        for _ in range(half_len):

            found = False

            # Try smallest character first.
            for c in range(26):

                if half_cnt[c] == 0:
                    continue

                ch = chr(ord('a') + c)

                # Try using this character
                half_cnt[c] -= 1
                left.append(ch)

                # If some completion can beat target,
                # this is the smallest valid choice.
                if can_be_greater():
                    found = True
                    break

                # Otherwise undo the choice
                left.pop()
                half_cnt[c] += 1

            if not found:
                return ""

        # Build final palindrome
        left = ''.join(left)

        answer = left + middle + left[::-1]

        return answer if answer > target else ""