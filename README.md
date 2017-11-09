# SynthLeth

SynthLeth is a python script that infers synthetic lethal gene pairs of Plasmodium falciparum from synthetic lethal gene pairs of Saccharomyces Cerevisiae 

## Download SynthLeth and data files 

```ruby
git clone https://github.com/suvi-subra/SynthLeth
cd SynthLeth
unzip BioSc.txt.zip
unzip groups.txt.zip
curl -O http://orthomcl.org/common/downloads/release-5/pairs/orthologs.txt.gz
unzip orthologs.txt.gz
```
## Running SynthLeth

Users can run SynthLeth using the following command:

```ruby
python ./SynthLeth.py
```

