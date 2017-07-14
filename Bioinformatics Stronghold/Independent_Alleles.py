genotypes = ['dd', 'dh', 'dr', 'hd', 'hh', 'hr', 'rd', 'rh', 'rr']
genes = {'d': [1, 1], 'h': [1, 0], 'r': [0, 0]}

geno_punnet = {}
for genotype in genotypes:
    g = genes[genotype[0]] + genes[genotype[1]]
    punnet = [[g[0]]+[g[2]], [g[0]]+[g[3]], [g[1]]+[g[2]], [g[1]]+[g[3]]]
    geno_punnet[genotype] = punnet

geno_prob = {}
for genotype in genotypes:

