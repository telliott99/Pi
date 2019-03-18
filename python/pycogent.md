#### Pycogent

[website](http://pycogent.org)

I used to get it from github and build it myself:

```
git clone git://github.com/pycogent/pycogent.git
...
cd pycogent
python setup.py build
python setup.py install
```

But now I just do

    pip install cogent

``` python
>>> import cogent.maths.stats.distribution as distr
>>> distr.binomial_low(successes=5, trials=10, prob=0.5)
0.6230468749999999
>>> distr.binomial_low(successes=5, trials=10, prob=0.5)
0.6230468749999999
>>>
```

#### Grabbing sequences

In Python:

```
import cogent
from cogent.db.ncbi import EFetch
seqL = ['AF411020','EU373389','AJ278451',
'AF411019','DQ450530','AJ002809']
FH = open('/Users/telliott_admin/Desktop/seqs.txt','w')
for seq in seqL:
    ef = EFetch(id=seq)
    FH.write(ef.read() + '\n')
    
FH.close()
```

[seqs.txt](data/seqs.txt)

```
>AF411020.1 Achromobacter xylosoxidans strain AU1011 16S ribosomal RNA gene, partial sequence
AGTTTGATCCTGGCTCAGATTGAACGCTAGCGGGATGCCTTACACATGCAAGTCGAACGGCAGCACGGAC
...
```


```
> muscle -in seqs.txt -out seqs.aln
...
> FastTree -nt seqs.aln > seqs.tr
...
```

Quick look:

```
> python
Python 2.7.13 (default, Jul  9 2017, 16:40:37) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from cogent import LoadTree
>>> tr = LoadTree('/Users/telliott/Desktop/seqs.tr')
>>> print tr.asciiArt()
          /-AF411020.1
         |
         |--AF411019.1
-root----|
         |                    /-AJ002809.1
         |          /0.931---|
         |         |          \-EU373389.1
          \0.799---|
                   |          /-AJ278451.1
                    \0.949---|
                              \-DQ450530.1
>>> 
```
