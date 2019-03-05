#### ``wc`` (word count)

```
> find $ghd/Pi | wc -l
     849
> find $ghd/Pi | grep -v ".git" |  wc -l
     285
```

There are 849 lines of output (i.e. files) in my Github directory for the Pi project (``$ghd/Pi``).

Most of those are hidden ``.git`` files, which I remove with ``grep -v``.