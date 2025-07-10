A = [1, 2, 3]

subset = [[]]

for num in A:
    new_subsets = []
    for sub in subset:
        new_subsets.append(sub + [num])  
    subset.extend(new_subsets)  

print(subset)
