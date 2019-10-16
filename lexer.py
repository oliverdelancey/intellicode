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
    if cline[:1] == "#":
        continue
    elif cline == "":
        continue
    # i/o
    elif cline[:5] == "hello":
        print("Hello World!")
    elif cline[:3] == "get":
        exec("{0} = input()".format(cline[4:]))
    elif cline[:3] == "out":
        exec("print({0})".format(cline[4:]))
    elif cline[:5] == "modme":
        # add/insert/remove line of code
        ops = cline[6:].split(",")
        for i in range(2):
            ops[i] = int(ops[i])
        if len(ops) == 3:
            ops[2] = ops[2][1:]
        with open(sys.argv[1], "r") as f:
            selfcode = f.read()
        selfcode = selfcode.split("\n")
        if ops[1] == 0:
            del selfcode[ops[0]]
        elif ops[1] == 1:
            selfcode[ops[0]] = ops[2]
        elif ops[1] == 2:
            selfcode.insert(ops[0], ops[2])
        with open(sys.argv[1], "w") as f:
            f.write(lts(selfcode))
    elif cline[:6] == "modyou":
        # add/insert/remove line of code in another file
        ops = cline[7:].split(",")
        for i in range(2):
            ops[i] = int(ops[i])
        if len(ops) == 3:
            ops[2] = ops[2][1:]
        if len(ops) == 4:
            ops[2] = ops[2][1:]
            ops[3] = ops[3][1:]
        with open(ops[2], "r") as f:
            selfcode = f.read()
        selfcode = selfcode.split("\n")
        if ops[1] == 0:
            del selfcode[ops[0]]
        elif ops[1] == 1:
            selfcode[ops[0]] = ops[3]
        elif ops[1] == 2:
            selfcode.insert(ops[0], ops[3])
        with open(ops[2], "w") as f:
            f.write(lts(selfcode))
    elif cline[:2] == "py":
        # python code
        exec(str(cline[3:]))
    else:
        print("Error in line {0}: '{1}' | Command not recognized.".format(i + 1, cline))
