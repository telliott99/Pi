#### awk

``awk`` is a powerful, complex and mysterious scripting language.

From my perspective it's main use is pick out particular column(s) in lines of data for further processing:

```
> echo "a b c" | awk ' { print $2 }'
b
```

```
> printf "a b c\nd e f" > x.txt
> awk ' { print $2 }' < x.txt
b
e
>
```

#### Other separators

Suppose we do some fance ``sed`` stuff:  global substitution for spaces.

```
> sed -E "s/[[:space:]]/*/g" < x.txt
a*b*c
d*e*f
> sed -E "s/[[:space:]]/*/g" < x.txt > y.txt
> cat y.txt
a*b*c
d*e*f
```

Now to split on that ``*``, we need ``FS`` (for separator):

```
> awk ' BEGIN { FS="*" } { print $1 }' < y.txt
a
d
```