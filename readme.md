This is a project of gene sequence extractor of hg 19 and hg38 by python.

# Data download and unzip

The complete dataset was obtained from the [UCSC Genome Browser](https://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/). As specified on the UCSC website, the download code is:

hg38:

```
mkdir hg38
wget --timestamping ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/*'
gunzip *.fa.gz
```

hg19:

```
mkdir hg19
`wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/*'
gunzip *.fa.gz
```

# Data pretreat

Run `gene_sequence_extractor.py`, then you will get 2 dictionary files: `hg19` and `hg38`. 

```python
python gene_sequence_extractor.py
```

# Gene sequence extractor

You could use shell to get your target sequence by `get_gene_sequence.py` or extracting information in bulk by tweaking the Python script:

```python
python get_gene_sequence.py "hg38" "chr3" 1000000 1000100

agtcctatccccagtacctgtgaatgtgacattatttggaatagggtctttgtagatataattaaggatcctgtgattagatgatcttagatttagggtg
```

