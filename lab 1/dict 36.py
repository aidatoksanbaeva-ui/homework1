from itertools import combinations
def all_subsets_of_size_k(s, k):
    return [set(c) for c in combinations(s, k)]
s = {1, 2, 3}
k = 2
print(all_subsets_of_size_k(s, k))