#!/usr/bin/env python3

# Read the data from each of the two datasets in separately and then reconcile.

_95 = {}  # To store the data from the 95 ants/8 loci dataset.

sample_to_site = {}  # Keep track of which ants belong to which site.

# Parse the 95/8 file, line-by-line:

with open("95_samples_8_loci.txt", "r") as f:
    lines = f.readlines()

    header = lines[0].rstrip().split("\t")
    loci = [i[-2:] for i in header[2:] if not i == '']

    for l in lines[1:]:
        l = l.rstrip().split("\t")
        sample = l[0]
        site = l[1]
        sample_to_site[sample] = site

        allele1 = [i[1:] if i != "NA" else "NA" for i in l[2::2]]
        allele2 = [i[1:] if i != "NA" else "NA" for i in l[3::2]]
        alleles = list(zip(allele1, allele2))
        
        _95[sample] = {}
        
        for i in range(len(alleles)):
            locus = loci[i]
            allele = alleles[i]
        
            # Replace the NAs with -99, as per STRUCTURE's requirements.
            if allele == ("NA", "NA"):
                allele = ("-99", "-99")
        
            _95[sample][locus] = allele

_95_loci = loci[:]  # Keep a list of the 95/8 loci.

_66 = {}  # To store the data from the 66 ants/21 loci dataset.

# Parse the 66/21 file in the same way:

with open("66_samples_21_loci.txt", "r") as f:
    lines = f.readlines()
    
    header = lines[0].rstrip().split("\t")
    loci = [i[-2:] for i in header[2:] if not i == '']
    
    for l in lines[1:]:
        l = l.rstrip().split("\t")
        sample = l[0]
        
        allele1 = [i[1:] if i != "NA" else "NA" for i in l[2::2]]
        allele2 = [i[1:] if i != "NA" else "NA" for i in l[3::2]]
        alleles = list(zip(allele1, allele2))
        
        _66[sample] = {}
        
        for i in range(len(alleles)):
            locus = loci[i]
            allele = alleles[i]
            
            # Replace NAs with -99 again.
            if allele == ("NA", "NA"):
                allele = ("-99", "-99")
            
            _66[sample][locus] = allele

_66_loci = loci[:]  # A list of the 66/21 loci.

all_loci = sorted(list(set(_95_loci + _66_loci)))  # A merged list of all loci.

merged = {}  # New dictionary to stored the merged data in.

# Go through each sample in the 95/8 dataset, which has all the ants:

for sample in _95:
    for locus in all_loci:
        if locus in _95[sample]:
            # Sample is in the 66/21 dataset also:
            if sample in _66:
                # If the loci match between the datasets then add to the merged set:
                if _95[sample][locus] == _66[sample][locus]:
                    if sample in merged:
                        merged[sample][locus] = _95[sample][locus]
                    else:
                        merged[sample] = {locus: _95[sample][locus]}
                # One or other dataset has missing values for a loci:
                elif (_95[sample][locus] == ("-99", "-99")) or (_66[sample][locus] == ("-99", "-99")):
                    # If missing in 95/8 dataset, then use value from 66/21 dataset:
                    if _95[sample][locus] == ("-99", "-99"):
                        if sample in merged:
                            merged[sample][locus] = _66[sample][locus]
                        else:
                            merged[sample] = {locus: _66[sample][locus]}
                    # Otherwise, if missing from 66/21, then use 95/8 value:
                    else:
                        if sample in merged:
                            merged[sample][locus] = _95[sample][locus]
                        else:
                            merged[sample] = {locus: _95[sample][locus]}
                # If different in both datasets, then print sample and locus:
                else:
                    print(sample, locus)
            # Add ants that are in 95/8 dataset but not 66/21:
            else:
                if sample in merged:
                    merged[sample][locus] = _95[sample][locus]
                else:
                    merged[sample] = {locus: _95[sample][locus]}
        # Add loci that are in 66/21 dataset but not 95/8 dataset:
        else:
            if sample in _66:
                if sample in merged:
                    merged[sample][locus] = _66[sample][locus]
                else:
                    merged[sample] = {locus: _66[sample][locus]}

# Make a sorted list of all of the sites, and a number/site dictionary:
all_sites = sorted(list(set(sample_to_site.values())))
site_to_num = {all_sites[i]: str(i+1) for i in range(len(all_sites))}

# Write the merged data to a file that can be used as input to STRUCTURE, with
# each allele on successive lines:
with open("merged_loci.str", "w") as out:
    out.write("\t".join(all_loci) + "\n")
    for sample in merged:
        allele1s = []
        allele2s = []
        for locus in all_loci:
            if locus in merged[sample]:
                allele1s.append(merged[sample][locus][0])
                allele2s.append(merged[sample][locus][1])
            else:
                allele1s.append("-99")
                allele2s.append("-99")
        out.write("\t".join([sample, site_to_num[sample_to_site[sample]], "1"] + allele1s) + "\n")
        out.write("\t".join([sample, site_to_num[sample_to_site[sample]], "1"] + allele2s) + "\n")