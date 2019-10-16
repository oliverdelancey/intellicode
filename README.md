# intellicode v1.00

intellicode is an experimental programming language which focuses on:
* Ease and speed of composition, i.e. it is fast and simple to convert ideas to code.
* Implementing unusual, nonstandard features, i.e. self- or interfile-modification.

Files that end in *.itc* are intellicode files. However, for the time being, this is merely an arbitrary rule. In theory, the file extension does not matter, as long as the file itself is plaintext.

Manual/reference in progress.

## Installation

Download *lexer.py* and place it wherever you wish to run it.
Note: python 3 must be installed for *lexer.py* to work.

## Usage

1. Create an intellicode file with any text editor. (See *example.itc* for a sample program.)
2. Run in terminal/cmd:
```
python /path/to/lexer.py /path/to/intellicode_file.itc
```

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

## py
```
py line_of_python_code
```

Execute any python code on the line, after *py*.

### modme
```
modme x, y, z
```

Change a specific line(s) of code *x*-1. If *y* == 0, remove. If *y* == 1, replace. If *y* == 2, insert before line *x*. *z* is the line of code if replacing or inserting, and is **not** in quotes, `""`. WARNING: If *modme* errors out, the entire file may be wiped. Use this command with extreme caution.

### modyou
```
modyou x, y, z, w
```

Change a specific line(s) of code *x*-1 . If *y* == 0, remove. If *y* == 1, replace. If *y* == 2, insert before line *x*. *z* is the name of the file being edited, and is **not** in quotes, `""`. *w* is the line of code if replacing or inserting, and is **not** in quotes, `""`. *modyou* may be used to create a new file if the given filename does not exist. WARNING: If *modyou* errors out, the entire file being edited may be wiped. Use this command with extreme caution.
