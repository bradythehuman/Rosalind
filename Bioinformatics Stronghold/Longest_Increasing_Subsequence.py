import LongestIncreasingSubsequenceMod as mod

dataset = mod.dataset_reader(r'Longest_Increasing_Subsequence_-_Dataset.txt')
n = dataset[0]
p = dataset[1]

starting_nodes = mod.find_starting_points(p)

directed_edges = mod.find_adjacency_list(starting_nodes, p, n)

# for node in starting_nodes:

print(directed_edges)
