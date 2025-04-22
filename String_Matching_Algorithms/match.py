def naive_string_matching(text, pattern):
    """Performs naive string matching."""
    n = len(text)
    m = len(pattern)
    occurrences = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            occurrences.append(i)
    return occurrences

def rabin_karp_matching(text, pattern):
    """Performs Rabin-Karp string matching with a simple rolling hash."""
    n = len(text)
    m = len(pattern)
    occurrences = []
    if m > n:
        return occurrences

    d = 256  # Number of characters in the alphabet (assuming ASCII)
    q = 101  # A prime number for modulo operation

    pattern_hash = 0
    text_hash = 0
    h = pow(d, m - 1, q)  # d^(m-1) mod q

    # Calculate hash of pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values
        if pattern_hash == text_hash:
            # Verify character by character in case of collision
            if text[i:i + m] == pattern:
                occurrences.append(i)

        # Calculate hash for the next window of text
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            # Ensure hash is non-negative
            if text_hash < 0:
                text_hash = (text_hash + q) % q

    return occurrences

def kmp_matching(text, pattern):
    """Performs Knuth-Morris-Pratt (KMP) string matching."""
    n = len(text)
    m = len(pattern)
    occurrences = []
    if m > n:
        return occurrences

    # Compute the prefix function (longest proper prefix which is also suffix)
    pi = [0] * m
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    # Search for the pattern in the text
    j = 0  # index for pattern
    for i in range(n):  # index for text
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = pi[j - 1]

    return occurrences

# Example Usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    naive_occurrences = naive_string_matching(text, pattern)
    print(f"Naive Matching occurrences of '{pattern}' in '{text}': {naive_occurrences}")

    rabin_karp_occurrences = rabin_karp_matching(text, pattern)
    print(f"Rabin-Karp Matching occurrences of '{pattern}' in '{text}': {rabin_karp_occurrences}")

    kmp_occurrences = kmp_matching(text, pattern)
    print(f"KMP Matching occurrences of '{pattern}' in '{text}': {kmp_occurrences}")

    text2 = "AAAAABAAABA"
    pattern2 = "AAAA"

    naive_occurrences2 = naive_string_matching(text2, pattern2)
    print(f"Naive Matching occurrences of '{pattern2}' in '{text2}': {naive_occurrences2}")

    rabin_karp_occurrences2 = rabin_karp_matching(text2, pattern2)
    print(f"Rabin-Karp Matching occurrences of '{pattern2}' in '{text2}': {rabin_karp_occurrences2}")

    kmp_occurrences2 = kmp_matching(text2, pattern2)
    print(f"KMP Matching occurrences of '{pattern2}' in '{text2}': {kmp_occurrences2}")