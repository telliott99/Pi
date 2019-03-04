#### EOF

Trick used to write stuff to a file:

```
> cat << EOF > x.txt
> a
> b
> EOF
> 
> cat x.txt
a
b
>
```