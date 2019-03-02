#### Python examples

- a fun [Python version](../files/20.md) of the [password generator](pw_util.md)
- [Caesar cipher](caesar.md)
- [Beale cipher](Beale-cipher.md)
- Sieve of Eratosthenes in [Python](../scripts/eratosthenes.py)
- simple [integration script](../scripts/integrate.py) 
- automating check of git status:  [gitcheck](gitcheck.md)
- [Pycogent](pycogent.md) bioinformatics [in progress]

#### Sieve of Eratosthenes

As an example:

```
> scp ~/Desktop/eratosthenes.py pi@10.0.1.7:~
eratosthenes.py       100% 1218   334.1KB/s   00:00    
```

and then

```
$ python eratosthenes.py 
   2    3    5    7   11   13   17   19   23   29
  31   37   41   43   47   53   59   61   67   71
  73   79   83   89   97  101  103  107  109  113
 127  131  137  139  149  151  157  163  167  173
 179  181  191  193  197  199  211  223  227  229
 233  239  241  251  257  263  269  271  277  281
 283  293  307  311  313  317  331  337  347  349
 353  359  367  373  379  383  389  397  401  409
 419  421  431  433  439  443  449  457  461  463
 467  479  487  491  499  503  509  521  523  541
 547  557  563  569  571  577  587  593  599  601
 607  613  617  619  631  641  643  647  653  659
 661  673  677  683  691  701  709  719  727  733
 739  743  751  757  761  769  773  787  797  809
 811  821  823  827  829  839  853  857  859  863
 877  881  883  887  907  911  919  929  937  941
 947  953  967  971  977  983  991  997
$
```

#### Refs

[Pycogent website](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjgv8T-rtTgAhXxV98KHVK8Ds0QFjAAegQIAhAB&url=http%3A%2F%2Fpycogent.org%2Findex.html&usg=AOvVaw1lvjTFQxu0Gh9h_AU3lnKV) is broken, unfortunately

I've written quite a lot about Python with projects on github (examples in [1](https://github.com/telliott99/PythonQuickies), [2](https://github.com/telliott99/Python2-Data), [3](https://github.com/telliott99/PyBioinformatics)).
