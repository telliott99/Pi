#### grep two patterns


```
> printf "foo\nbar\nbaz\n" > x.txt
> grep 'foo\|bar' x.txt
foo
bar
> grep -E 'foo|bar' x.txt
foo
bar
> grep -e foo -e bar x.txt
foo
bar
> egrep "foo|bar" x.txt
foo
bar
> 

```

So ``-E`` or ``\|`` or egrep or two ``-e`` flags.

#### example

In this project there are more than 1000 files but most of them are git-related and many others are hidden ``.DS_Store`` files for the Finder's use:

```
> find $ghd/Pi | wc -l
    1356
> find $ghd/Pi | grep ".git" | wc -l
     864
> 
> find $ghd/Pi | head -n 3
/Users/telliott_admin/Dropbox/Github/Pi
/Users/telliott_admin/Dropbox/Github/Pi/flask
/Users/telliott_admin/Dropbox/Github/Pi/flask/.DS_Store
```

We combine ``-Ev`` to exclude both patterns:

```
> find $ghd/Pi | grep -vE ".DS|.git" | wc -l
     430
>
```

