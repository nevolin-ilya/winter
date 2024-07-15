def isotrop(s1, s2):
    if len(s1) != len(s2):
        return False

    map_s1_to_s2 = {}
    map_s2_to_s1 = {}

    for k_s1, k_s2 in zip(s1, s2):
        if (k_s1 in map_s1_to_s2 and map_s1_to_s2[k_s1] != k_s2) or (k_s2 in map_s2_to_s1 and map_s2_to_s1[k_s2] != k_s1):
            return False
        map_s1_to_s2[k_s1] = k_s2
        map_s2_to_s1[k_s2] = k_s1
    return True

s1 = "ABCDA"
s2 = "NFGHN"
print(isotrop(s1, s2))