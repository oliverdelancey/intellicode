# this will:
#   1 execute the commands of the input file one by one --current
#  or
#   2 compile a python script to run from the input file

import sys

# definitions
def lts(s):
    st = ""
    for i in s:
        st += i + "\n"
    return st


# load file
with open(sys.argv[1], "r") as f:
    code = f.read()
code = code.split("\n")

# lexer
for i in range(len(code)):
    cline = code[i]
    if "#" in cline:
        continue
    elif cline == "":
        continue
    elif "hello" in cline:
        print("Hello World!")
    elif "get" in cline:
        exec("{0} = input()".format(cline[4:]))
    elif "out" in cline:
        exec("print({0})".format(cline[4:]))
    elif "modme" in cline:
        # add/remove line of code
        ops = cline[6:].split(",")
        for i in range(len(ops)):
            ops[i] = int(ops[i])
        with open(sys.argv[1], "r") as f:
            selfcode = f.read()
        selfcode = selfcode.split("\n")
        if ops[1] == 0:
            del selfcode[ops[0]]
        elif ops[1] == 1:
            selfcode[ops[0]] == ops[2]
        elif ops[1] == 2:
            selfcode.insert(ops[0], ops[2])
        with open(sys.argv[1], "w") as f:
            f.write(lts(selfcode))
    else:
        print("Error in line {0}: '{1}' | Command not recognized.".format(i + 1, cline))
