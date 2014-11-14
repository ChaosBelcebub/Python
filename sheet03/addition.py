def read(term):
    output = [None, None, None]
    readterm(term, output)
    return output

def readterm(term, destination):
    count = 0
    left = []
    right = []
    for c in term:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if c == '+' and count == 0:
            destination[0] = c
        elif destination[0] != '+':
            left.append(c)
        else:
            right.append(c)
    if destination[0] != '+':
        if len(left) != 1:
            left.pop()
            left.pop(0)
        else:
            destination[0] = left[0]
            return
    if len(left) == 1:
        destination[1] = [str(left[0]), None, None]
    elif len(left) > 1:
        if destination[0] == None:
            readterm(''.join(left), destination)
        else:
            destination[1] = [None, None, None]
            readterm(''.join(left), destination[1])
    if len(right) == 1:
        destination[2] = [str(right[0]), None, None]
    elif len(right) > 1:
        destination[2] = [None, None, None]
        readterm(''.join(right), destination[2])

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
