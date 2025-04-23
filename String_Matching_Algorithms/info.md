# String Matching Algorithms

These algorithms are designed to find occurrences of a specific pattern (a short string) within a larger text (a longer string). This is a fundamental problem in computer science with applications in text editors, search engines, bioinformatics (finding DNA sequences), network security (intrusion detection), and many other areas.

Here's a breakdown of some common and important string matching algorithms:

**1. Naive String Matching Algorithm (Brute Force):**

* **How it works:** This is the simplest approach. It slides the pattern across the text, one character at a time, and at each position, it checks if the pattern matches the current substring of the text.
* **Analogy:** Imagine manually comparing a short word with every possible sequence of letters of the same length in a long sentence.
* **Example:**
    * Text: `ABCABDABC`
    * Pattern: `ABC`
    * Compare `ABC` with `ABC` (match at index 0).
    * Compare `ABC` with `BCA` (no match).
    * Compare `ABC` with `CAB` (no match).
    * Compare `ABC` with `ABA` (no match).
    * Compare `ABC` with `ABD` (no match).
    * Compare `ABC` with `BDA` (no match).
    * Compare `ABC` with `DAB` (no match).
    * Compare `ABC` with `ABC` (match at index 6).
* **Time Complexity:**
    * Worst Case: $\mathcal{O}(m \cdot n)$, where $n$ is the length of the text and $m$ is the length of the pattern. This occurs when the pattern almost matches at every position and we have to compare all $m$ characters.
    * Best Case: $\mathcal{O}(n)$ (if the pattern is not found or if the first character of the pattern rarely matches the text).
* **Space Complexity:** $\mathcal{O}(1)$ (constant extra space).
* **Advantages:** Simple to understand and implement.
* **Disadvantages:** Inefficient for large texts and patterns, especially when there are many near misses.

**2. Rabin-Karp Algorithm:**

* **How it works:** This algorithm uses hashing to find potential matches. It calculates a hash value for the pattern and then calculates the hash value for each substring of the text of the same length as the pattern. If the hash values match, it performs a character-by-character verification to confirm the actual match (to handle hash collisions). Rolling hash functions are often used to efficiently calculate the hash of the next substring based on the current hash.
* **Analogy:** Think of creating a unique fingerprint for your search word and then quickly checking the fingerprints of all similarly sized segments in the document. Only when the fingerprints match do you do a detailed comparison.
* **Time Complexity:**
    * Average Case: $\mathcal{O}(n + m)$ (with a good rolling hash function and assuming few hash collisions).
    * Worst Case: $\mathcal{O}(m \cdot n)$ (if there are many hash collisions).
* **Space Complexity:** $\mathcal{O}(1)$ (constant extra space, excluding the space for the pattern and text).
* **Advantages:** Can be faster than naive string matching in practice, especially for longer patterns. Can be extended to handle multiple pattern matching.
* **Disadvantages:** Worst-case performance can be as bad as the naive algorithm due to hash collisions. Requires careful selection of the hash function and modulus.

**3. Knuth-Morris-Pratt (KMP) Algorithm:**

* **How it works:** This algorithm avoids redundant comparisons by using information about the pattern itself. It pre-processes the pattern to build a "prefix function" (also known as a "failure function" or "border array"). This function tells us, for each position in the pattern, the length of the longest proper prefix of the pattern that is also a suffix of the pattern up to that position. When a mismatch occurs during the matching process, the prefix function is used to determine how much to shift the pattern to the right without re-comparing characters that are already known to match.
* **Analogy:** Imagine your search word has a repeating prefix. If you find a partial match and then a mismatch, the KMP algorithm helps you realize how much you can slide your search word forward based on these repetitions, without having to start all over from the beginning of your search word.
* **Time Complexity:**
    * Pattern Pre-processing: $\mathcal{O}(m)$.
    * Text Searching: $\mathcal{O}(n)$.
    * Total: $\mathcal{O}(n + m)$.
* **Space Complexity:** $\mathcal{O}(m)$ (for storing the prefix function).
* **Advantages:** Guaranteed linear time complexity, which is a significant improvement over the naive algorithm in the worst case.
* **Disadvantages:** The pre-processing step can be a bit complex to understand and implement.

**4. Boyer-Moore Algorithm:**

* **How it works:** This is often considered one of the most efficient string matching algorithms in practice. It also pre-processes the pattern but uses two different heuristics to determine the shift amount when a mismatch occurs:
    * **Bad Character Heuristic:** If a mismatch occurs at text character `T[i]` with pattern character `P[j]`, this heuristic looks at `T[i]` in the pattern `P`. If `T[i]` appears in `P` before position `j`, the pattern is shifted to align that occurrence with `T[i]`. If `T[i]` does not appear in `P`, the pattern is shifted past `T[i]`.
    * **Good Suffix Heuristic:** If a mismatch occurs after a suffix of the pattern has been matched, this heuristic uses information about the matched suffix to determine how far to shift the pattern. It looks for another occurrence of that suffix (or a prefix of the pattern that is also a suffix of the matched part) and shifts accordingly.
    The algorithm takes the maximum of the shifts suggested by these two heuristics. It also typically scans the pattern from right to left.
* **Analogy:** Imagine you're searching for a word and you encounter a letter in the text that's not in your word at the current position. The Boyer-Moore algorithm smartly decides how far to jump ahead based on whether that mismatched letter even exists in your word and based on any matching parts you've already found at the end of your word.
* **Time Complexity:**
    * Pattern Pre-processing: $\mathcal{O}(m)$.
    * Text Searching:
        * Worst Case: $\mathcal{O}(m \cdot n)$ (though this is rare and doesn't occur in typical practical cases).
        * Average Case: Sublinear, often significantly faster than $\mathcal{O}(n)$. In many practical scenarios, it can be around $\mathcal{O}(n/m)$.
    * Best Case: Can be as good as $\mathcal{O}(n/m)$ in some cases (e.g., when the pattern and text have very different alphabets).
* **Space Complexity:** $\mathcal{O}(\sigma + m)$, where $\sigma$ is the size of the alphabet (for storing the bad character table) and $m$ is the length of the pattern (for the good suffix table).
* **Advantages:** Very efficient in practice, often outperforming other algorithms.
* **Disadvantages:** The pre-processing and the logic behind the heuristics can be more complex to implement.

**5. Other Algorithms (Brief Mention):**

* **Aho-Corasick Algorithm:** Efficient for finding occurrences of multiple patterns in a text. It builds a finite automaton (a trie with failure links).
* **Sunday Algorithm:** A relatively simple and often efficient algorithm that is similar to Boyer-Moore but shifts based on the character in the text *after* the current window.

The choice of which string matching algorithm to use depends on factors like the size of the text and pattern, the frequency of searches, the size of the alphabet, and the need for guaranteed worst-case performance versus typical average-case performance. For many general-purpose applications, Boyer-Moore or its variants are often preferred for their practical efficiency. For applications requiring guaranteed linear time, KMP is a good choice. Rabin-Karp can be useful for multiple pattern searching with extensions.