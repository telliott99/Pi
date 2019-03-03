#### if-then-else

```
word='erase'
msg="You appear to have typed $word in the past"

if grep -q $word ~/.bash_history; then
  echo $msg
fi
```

output:

```
> ./script.sh 
You appear to have typed erase in the past
```

- terminate with **fi**
- ``then`` or ``else`` without an expression is a syntax error
- grep ``-q`` (quiet) --- suppress normal output
- parentheses on condition are fine but not necessary


Alternate form:
  
```
word='erase'
msg="You appear to have typed $word in the past"

grep -q word ~/.bash_history
retval=$?

if [[ $retval -ne 0 ]]; then
  echo $msg
fi
```

- note the ``;`` after the condition
- and the ``[[ .. ]]``
- ``$?`` holds the return value of the last expression

#### exists

```
if [[ -e "/Users/telliott_admin/.ssh/id_rsa.pub" ]]; then
  echo "you got a key"
fi
```

Note "~" doesn't work here/