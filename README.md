# intellicode v0.01

intellicode is an experimental programming language which focuses on:
* Ease and speed of composition, i.e. it is fast and simple to convert ideas to code.
* Implementing unusual, nonstandard features, i.e. self- or interfile-modification.

Files that end in *.itc* are intellicode files.

Manual/reference in progress.

## Reference

### Comments
```
# this is a comment
```

Comments work just like in python, starting with a *#*.

### hello
```
hello
```

A simple command that prints *Hello World!* to the terminal.

### get
```
get x
```

Ask user for an input value with variable name *x*. *x* may be any vaild python variable name.

### out
```
out x
```

Print *x* to the terminal. *x* may be a variable, integer/float, string, list, etc.

### modme
```
modme x, y, z
```

Change a specific line(s) of code *x*-1. If *y* == 0, remove. If *y* == 1, replace. If *y* == 2, insert before line *x*. *z* is the line of code if replacing or inserting, and must be a string. WARNING: If *modme* errors out, the entire file may be wiped. Use this command with extreme caution.
## © 2019 Oliver Sandli
