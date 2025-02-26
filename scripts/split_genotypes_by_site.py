#!/usr/bin/env python3
"""
Process nest IDs and generate site-specific structure and nest numbering files.
"""

# Map IDs to nests from file.
id_to_nest = {}
with open("id_to_nest.txt", "r") as f:
    for line in f:
        parts = line.rstrip().split()
        id_to_nest[parts[0]] = parts[1]

# Get unique sites (first two characters of nest) and nests.
sites = list({v[:2] for v in id_to_nest.values()})
nests = list(set(id_to_nest.values()))

# Assign sequential numbers to nests per site.
nest_nums = {}
for site in sites:
    nest_nums[site] = {}
    nest_num = 1
    for nest in sorted(nests, key=lambda x: int(x[2:])):
        if nest.startswith(site):
            nest_nums[site][nest] = str(nest_num)
            nest_num += 1

# Process the main structure file and output site-specific files.
nests_done = []
for i in range(1, 8):
    with open("merged_loci_r_haploid_only.str", "r") as f:
        lines = f.readlines()
        with open(f"site_{i}_hap.str", "w") as site_out, \
             open(f"nest_nums_{i}.txt", "w") as nest_out:
            site_out.write(lines[0])
            for line in lines[1:]:
                if line.split()[1] == str(i):
                    parts = line.rstrip().split()
                    nest = id_to_nest[parts[0]]
                    site = nest[:2]
                    nest_num = nest_nums[site][nest]
                    if nest not in nests_done:
                        nest_out.write("\t".join([nest_num, nest]) + "\n")
                    nests_done.append(nest)
                    site_out.write("\t".join([parts[0], nest_num] + parts[2:]) + "\n")