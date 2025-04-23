from collections import defaultdict

class Apriori:
    def __init__(self, min_support=0.5, min_confidence=0.7):
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.frequent_itemsets = None
        self.association_rules = None

    def _calculate_support(self, itemset, transactions):
        """Calculates the support of an itemset."""
        count = 0
        for transaction in transactions:
            if itemset.issubset(transaction):
                count += 1
        return count / len(transactions)

    def _generate_candidates(self, frequent_k_itemsets):
        """Generates candidate (k+1)-itemsets from frequent k-itemsets."""
        candidates = set()
        frequent_list = list(frequent_k_itemsets)
        for i in range(len(frequent_list)):
            for j in range(i + 1, len(frequent_list)):
                l1 = list(frequent_list[i])
                l2 = list(frequent_list[j])
                l1.sort()
                l2.sort()
                if l1[:-1] == l2[:-1]:  # Merge if the first k-1 items are the same
                    candidate = frozenset(l1 + [l2[-1]])
                    candidates.add(candidate)
        return candidates

    def fit(self, transactions):
        """Finds frequent itemsets and association rules."""
        n_transactions = len(transactions)
        support_counts = defaultdict(int)
        frequent_itemsets_by_length = []

        # Find frequent 1-itemsets
        for transaction in transactions:
            for item in transaction:
                support_counts[frozenset([item])] += 1

        frequent_1_itemsets = {itemset for itemset, count in support_counts.items() if count / n_transactions >= self.min_support}
        frequent_itemsets_by_length.append(frequent_1_itemsets)
        k = 1
        current_frequent_itemsets = frequent_1_itemsets

        # Generate frequent k-itemsets
        while current_frequent_itemsets:
            k += 1
            candidates = self._generate_candidates(current_frequent_itemsets)
            support_counts = defaultdict(int)
            for transaction in transactions:
                for candidate in candidates:
                    if candidate.issubset(transaction):
                        support_counts[candidate] += 1

            current_frequent_itemsets = {candidate for candidate, count in support_counts.items() if count / n_transactions >= self.min_support}
            frequent_itemsets_by_length.append(current_frequent_itemsets)

        self.frequent_itemsets = [item for level in frequent_itemsets_by_length for item in level]
        self.association_rules = self._generate_rules(transactions)
        return self

    def _generate_rules(self, transactions):
        """Generates association rules from frequent itemsets."""
        rules = []
        for itemset in self.frequent_itemsets:
            if len(itemset) > 1:
                for i in range(1, len(itemset)):
                    for antecedent in self._combinations(list(itemset), i):
                        antecedent = frozenset(antecedent)
                        consequent = itemset - antecedent
                        if consequent:
                            support_antecedent = self._calculate_support(antecedent, transactions)
                            support_itemset = self._calculate_support(itemset, transactions)
                            confidence = support_itemset / support_antecedent
                            if confidence >= self.min_confidence:
                                rules.append((antecedent, consequent, support_itemset, confidence))
        return rules

    def _combinations(self, iterable, r):
        """Helper function to generate combinations."""
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)

# Example Usage:
if __name__ == '__main__':
    transactions = [
        {'bread', 'milk'},
        {'bread', 'diaper', 'beer', 'eggs'},
        {'milk', 'diaper', 'beer', 'coke'},
        {'bread', 'milk', 'diaper', 'beer'},
        {'bread', 'milk', 'diaper', 'coke'}
    ]

    apriori = Apriori(min_support=0.4, min_confidence=0.6)
    apriori.fit(transactions)

    print("Frequent Itemsets:")
    for itemset in apriori.frequent_itemsets:
        print(itemset)

    print("\nAssociation Rules (Antecedent => Consequent, Support, Confidence):")
    for antecedent, consequent, support, confidence in apriori.association_rules:
        print(f"{antecedent} => {consequent}, Support: {support:.2f}, Confidence: {confidence:.2f}")