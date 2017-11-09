# SynthLeth

SynthLeth is a python script that infers synthetic lethal gene pairs of a target organism, Plasmodium falciparum ("pfal"), from synthetic lethal gene pairs of Saccharomyces Cerevisiae ("scer") taking into account the presence/absence of orthologs in Homo Sapiens

## Files needed

### Input: 3 files 	

a) "BioSC.txt" - Synthetic lethal interaction data of Saccharomyces Cerevisiae

Source: http://thebiogrid.org/downloads/archives/Latest%20Release/BIOGRID-ORGANISM-LATEST.tab2.zip

b) "orthologs.txt" - List of pairwise orthologs between organisms from OrthoMCL

Source: http://www.orthomcl.org/common/downloads/release-5/pairs/orthologs.txt.gz

c) "groups.txt" - Groups containing orthologs of Saccharomyces cerevisiae, Homo sapiens & Plasmodium falciparum

Source: http://www.orthomcl.org/common/downloads/release-5/groups_OrthoMCL-5.txt.gz

### Output 1: 3 intermediate files (needed for script to run)

a) "scer_pfal.txt" - List of orthologs between Saccharomyces Cerevisiae & Plasmodium falciparum

b) "scer_pfal_only.txt" - List of orthologs between Saccharomyces Cerevisiae & Plasmodium falciparum excluding those with orthologs in Homo sapiens

c) "sph.txt" - Clusters containing orthologs of Saccharomyces Cerevisiae, Plasmodium falciparum & Homo sapiens

### Output 2: 1 file 

"final_sl_pfal.txt"- List of inferred synthetic lethal gene pairs in target organism, Plasmodium falciparum
  			
## Running SynthLeth

Users can run SynthLeth using the following command:

```ruby
cd mkdir
```
