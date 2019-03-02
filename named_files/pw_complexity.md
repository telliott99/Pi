Suppose we choose our shiny new password from an alphabet of size `n`, say, the lowercase letters `a-z`.  We use a password of length `p = 4`.

The number of possible passwords is:

```
SZ = n^p = 26^4 = 456976
```    

For this alphabet and a length of 4, that's almost half a million.
    
Suppose the alphabet is expanded to include twice the number of characters, say `a-z` + `A-Z`,

    SZ = (2n)^p = 2^p n^p

the complexity increases by a factor of `2^p`.

Here, that is a factor of `2^4` or 16, giving a `SZ` of a bit more than 7.3 million.

Now, here's the point:

Complexity goes *exponentially* with the length of the password. Doubling the length gives

    SZ = n^(2p) = (n^2)^p

The ratio to the original value is `n^p`.  In this example the new complexity is 26**8, which is larger than the old one by a factor of 456976.

```
>>> 26**8/26**4
456976
```

The disparity gets bigger as the length increases.  Doubling the length from 5 to 10 increases complexity by a factor of 11 million.

This is why it makes no sense to insist on particular characters in the alphabet used (say 1 number and 1 character chosen from `$%*` (but not some others!), if the length is maxed out at 8 or 16.

There may have been a time when password crackers didn't check the punctuation characters, but that time has passed.
