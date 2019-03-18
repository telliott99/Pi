#### bytes

One difference between Python 2 and 3 is that many objects that look like strings (that *were* strings in Python 2) are bytes in Python 3.  


```
> python3
..
>>> import subprocess
>>> result = subprocess.run(['ls','-al','.'],
...     stdout=subprocess.PIPE,
...     stderr=subprocess.PIPE)
>>> o = result.stdout
>>> type(o)
<class 'bytes'>
>>> o[:12]
b'total 642760'
>>>
>>> s = o.decode('utf-8')
>>> s[:10]
'total 642760'
```

A bytes object is an immutable byte array, i.e. an array of ints in the range 0..255.

```
>>> x = b'abc'
>>> x
b'abc'
>>> type(x)
<class 'bytes'>
>>> list(x)
[97, 98, 99]
>>> x.decode('utf-8')
'abc'
>>> s = x.decode('utf-8')
>>> list(s)
['a', 'b', 'c']
>>>
```