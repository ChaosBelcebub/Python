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