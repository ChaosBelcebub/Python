def read(term):
    output = [None, None, None]
    readterm(term, output)
    return output
    
def readterm(term, dest):
    destination = dest
    count = 0
    toggle = False
    ignore = False
    leftstack = []
    rightstack = []
    for c in term:
        if c == '(' and count == 0:
            ignore = True
            count += 1
        elif c == ')' and count != 0 and toggle == False:
            count -= 1
            leftstack.append(c)
        elif c == ')' and count != 0 and toggle == True:
            count -= 1
            rightstack.append(c)
        elif c == ')' and count == 0:
            ignore = False
        elif ignore == True and toggle == False:
            leftstack.append(c)
        elif ignore == True and toggle == True:
            rightstack.append(c)
        elif c != '+' and toggle == False:
            leftstack.append(c)
        elif c != '+' and toggle == True:
            rightstack.append(c)
        elif c == '+' and ignore == False:
            toggle = True
            destination[0] = c

    if len(leftstack) == 1:
        destination[1] = [str(leftstack[0]), None, None]
        leftstack = []
    elif len(leftstack) > 1:
        if destination[0] != None:
            destination[1] = [None, None, None]
            readterm(''.join(leftstack), destination[1])
        else:
            readterm(''.join(leftstack), destination)
        leftstack = []
    if len(rightstack) == 1:
        destination[2] = [str(rightstack[0]), None, None]
        rightstack = []
    elif len(rightstack) > 1:
        destination[2] = [None, None, None]
        readterm(''.join(rightstack), destination[2])
        rightstack = []

def print_tree(tree):
    print_tre(tree)
    print("")

def print_tre(tree):
    if tree[0] != None:
        print(tree[0], end="")
    if tree[1] != None:
        print_tre(tree[1])
    if tree[2] != None:
        print_tre(tree[2])
    
