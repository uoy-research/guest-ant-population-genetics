# Guest ant population genetics analysis

Code, data, and figures from a study of guest ant (_Formicoxenus nitidulus_) population genetics across a range of sites in Northern England and Northern Scotland, from Robinson _et al_ 2025.

The full code for analysing the data, and generating all of the figures and tables, can be found in the R Markdown document [guest_ant_population_genetics.Rmd](guest_ant_population_genetics.Rmd) and an HTML-rendered version of the code, figures, and tables can be found in [guest_ant_population_genetics.html](guest_ant_population_genetics.html)

## List of figures

### Main figures

* [Figure 1: allelic richness and private alleles](figures/figure_1_allelic_richness_private_alleles.png)
* [Figure 2: allele frequencies](figures/figure_2_allele_frequencies.png)
* [Figure 3: PCA and DAPC of genotypes by site](figures/figure_3_PCA_DAPC.png)
* [Figure 4: pairwise linearised Fst vs. distance scatter plots](figures/figure_4_distance_Fst_scatter_plots.png)
* [Figure 5: haplotype map and network](figures/figure_5_haplotype_map_network.png)

### Supplementary figures

* [Figure S1: site-level pairwise Fst and distance matrices](figures/figure_S1_sites_Fst_distance_matrix.png)
* [Figure S2: nest-level pairwise Fst and distance matrices](figures/figure_S2_nests_Fst_distance_matrix.png)
* [Figure S3: nest location maps by site](figures/figure_S3_nest_location_maps.png)
* [Figure S4: STRUCTURE ancestry plots](figures/figure_S4_STRUCTURE_plots.png)

## List of tables

### Main tables

* [Table 3: AMOVA results](tables/table_3_amova_results.csv)
* [Table 4: mitochondrial haplotypes](tables/table_4_mitochondrial_haplotypes.csv)

### Supplementary tables

* [Table S1: SPAGeDi gene diversity values](tables/table_S1_spagedi_gene_diversity.csv)
* [Table S2: SPAGeDi kinship values](tables/table_S2_spagedi_kinship.csv)

### Other tables

* [Mantel test results for Fst vs. distance association](tables/mantel_test_results.csv)
* [Site-level M-ratio test results](tables/m_ratio_test_results.csv)
* [Ant metadata (IDs, sites, nests, coordinates)](tables/ant_ids_and_locs.csv)

## Scripts

[merge_genotype_data.py](scripts/merge_genotype_data.py)

Python script that merges and sanitises the two separate sets of microsatellite genotype data into a single set.

[split_genotypes_by_site.py](scripts/split_genotypes_by_site.py)

Python script splits the complete genotype data into the seven separate sites, with separate `.str` genotype files and metadata files with nest numbers.

[structure_test_k.sh](scripts/structure_test_k.sh)

Bash script that runs STRUCTURE with a range of values of K and a number of replicate runs for each K value.