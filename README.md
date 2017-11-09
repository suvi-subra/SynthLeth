# SynthLeth

SynthLeth is a python script that infers synthetic lethal gene pairs of Plasmodium falciparum from synthetic lethal gene pairs of Saccharomyces Cerevisiae 

## Download SynthLeth and data files 

```ruby
mkdir Run_SynthLeth
cd Run_SynthLeth
git clone https://github.com/suvi-subra/SynthLeth
cd SynthLeth
unzip BioSc.txt.zip
unzip groups.txt.zip
curl -O http://www.orthomcl.org/common/downloads/release-5/pairs/orthologs.txt.gz
gunzip orthologs.txt.gz
```  			
## Running SynthLeth

Users can run SynthLeth using the following command:

```ruby
python ./SynthLeth.py
```

### Output 1: 3 intermediate files (needed for script to run)

a) "scer_pfal.txt" - List of orthologs between Saccharomyces Cerevisiae & Plasmodium falciparum

b) "scer_pfal_only.txt" - List of orthologs between Saccharomyces Cerevisiae & Plasmodium falciparum excluding those with orthologs in Homo sapiens

c) "sph.txt" - Clusters containing orthologs of Saccharomyces Cerevisiae, Plasmodium falciparum & Homo sapiens

### Output 2: 1 file 

"final_sl_pfal.txt"- List of inferred synthetic lethal gene pairs in target organism, Plasmodium falciparum
