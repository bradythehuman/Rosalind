pop_AA = 16
pop_Aa = 20
pop_aa = 22

results_A = 0
results_a = 0

results_A += pop_AA * ((pop_AA-1) + pop_Aa + pop_aa)
results_A += pop_Aa * (0.75*(pop_Aa-1) + pop_AA + 0.5*pop_aa)
results_A += pop_aa * (0.5*pop_Aa + pop_AA)

results_a += pop_Aa * (0.25*(pop_Aa-1) + 0.5*pop_aa)
results_a += pop_aa * ((pop_aa-1) + 0.5*pop_Aa)

prob_A = results_A / (results_A+results_a)

print(prob_A)
