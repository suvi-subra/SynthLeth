# SynthLeth

Combinatorial chemotherapy is imperative for the treatment of malaria, caused by single-celled microorganisms called Plasmodium falciparum. However, finding a suitable partner drug for a new candidate is challenging. Here we develop an algorithm that identifies all the gene pairs of Plasmodium falciparum which possess orthologues in yeast (Saccharomyces Cerevisiae) that have an established synthetic lethal interaction, but are absent in humans. This suggests new options for drug combinations.<br>
SynthLeth is implemented in a python script to infer synthetic lethal gene pairs in Plasmodium falciparum from synthetic lethal gene pairs determined by high-throughput crossing experiments in Saccharomyces Cerevisiae.<br>

Manuscript:<br>
Using yeast synthetic lethality to inform drug combination for malaria. 
Subramaniam S, Schmid CD, Guan X, and Mäser P (2017) Antimicrob Agents Chemother

## Download SynthLeth and data files 

```ruby
git clone https://github.com/suvi-subra/SynthLeth
cd SynthLeth
unzip BioSc.txt.zip
unzip groups.txt.zip
curl -O http://orthomcl.org/common/downloads/release-5/pairs/orthologs.txt.gz
gunzip orthologs.txt.gz
```

[instructions](https://www.wikihow.com/Extract-a-Gz-File) to extract tar archives for non-linux OS

optional: prospective future releases of the [orthomcl](http://orthomcl.org) database or alternative tables with ortholog genes can be downloaded using an adapted version of the command above.


## Executing SynthLeth

The SynthLeth.py python script is executed with the input tables in the same directory using the following command:

```ruby
python ./SynthLeth.py
```

The script generates a set of text files, with Final_sl_pfal.txt describing the table with the synthetic lethal gene pairs in Plasmodium falciparum.
For comparison, the tables can be found in the directory expected_output/.

SynthLeth is licensed under the GNU General Public License v3.0

