def dataset_reader(path):

    with open(path, 'r') as f_obj:
        reader = f_obj.readlines()
        n = int(reader[0])
        p = []
        for line in reader[1:]:
            p += line.split()
        temp_p = []
        for string in p:
            temp_p.append(int(string))
        p = temp_p
    return [n, p]


def find_starting_points(permutation, increasing=True):
    result = []
    current = permutation[0]
    for num in permutation:
        if num <= current:
            current = num
            result.append(num)
    return result


def find_adjacency_list(starting_nodes, p, n):
    to_edge = starting_nodes[:]
    directed_edges = {}

    while to_edge:
        cur_node = to_edge.pop(0)
        next_i = p.index(cur_node) + 1

        cur_low = n + 1
        for node in p[next_i:]:
            if cur_low > node > cur_node:
                cur_low = node
        try:
            next_low_i = p.index(cur_low)
        except ValueError:
            continue

        cur_edges = []
        for node in p[next_i:next_low_i + 1]:
            if p[next_i] > node > cur_node:
                cur_edges.append(node)
                to_edge.append(node)
        directed_edges[cur_node] = cur_edges[:]

    return directed_edges


def find_longest_from(node):
    pass


# def subset_in_permutation(permutation, subset):
#     slen = len(subset)
#     i = 0
#     for number in permutation:
#         if subset[i] == number:
#             i += 1
#         if i == slen:
#             return True
#     return False
#
#
# def is_non_repeating(t_list):
#     return len(t_list) == len(set(t_list))
#
#
# def cut_from_full(full, cuts):
#     replaced_full = full[:]
#     for i in cuts:
#         replaced_full[i] = 0
#     cut_full = []
#     for num in replaced_full:
#         if num:
#             cut_full.append(num)
#     return cut_full
#
#
# def increase_cuts(cuts, plen):
#     lcuts = len(cuts)
#     from_right = 1
#     while True:
#         if cuts[-from_right] != plen-1 or from_right == lcuts:
#             cuts[-from_right] += 1
#             return cuts
#         else:
#             from_right


def format_print(permutation):
    for number in permutation:
        print(number, end=' ')
    print()
