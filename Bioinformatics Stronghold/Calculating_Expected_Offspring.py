pair_AA_AA = 16646
pair_AA_Aa = 18405
pair_AA_aa = 18798
pair_Aa_Aa = 19844
pair_Aa_aa = 18669
pair_aa_aa = 19702

offspring_A = pair_AA_AA + pair_AA_Aa + pair_AA_aa + 0.75*pair_Aa_Aa + 0.5*pair_Aa_aa
offspring_A *= 2

print(offspring_A)