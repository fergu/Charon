import ast
from functools import total_ordering
from collections import defaultdict
import random

@total_ordering
class tree_leaf:
    def __init__(self, name):
        self.name = name
        self.code = ""
        self.block_id = ""
        self.children = []
        self.parents = []
        self.has_executed = False
        self.value = None
    def __eq__(self, other):
        if (self.name == other.name):
            return True
        else:
            return False
    def __lt__(self, other):
        if (self in other.parents):
            return True
        else:
            return False
    def __repr__(self):
        return "Tree Leaf \"{0}\"".format(self.name)
    def __str__(self):
        return "Tree Leaf \"{0}\"".format(self.name)

def process_assignment(assignment):
    depends = []
    for arg in [assignment.left, assignment.right]:
        if type(arg) in [ast.BinOp]:
            sub_deps = process_assignment(arg)
            [depends.append(dep) for dep in sub_deps]
        elif type(arg) in [ast.Name]:
            if type(arg.ctx) in [ast.Load]:
                depends.append(str(arg.id))
    return depends

def process_block(group_id, block_as_string):
    parsed = ast.parse(block_as_string)
    block_leafs = {}
    for assignment in (x for x in parsed.body if type(x) in [ast.Assign]):
        this_leaf = tree_leaf(assignment.targets[0].id)
        this_leaf.code = block_as_string
        this_leaf.block_id = group_id
        if (type(assignment.value) in [ast.BinOp]):
            this_leaf.parents = process_assignment(assignment.value)
        block_leafs[this_leaf.name] = this_leaf
    return block_leafs

def determine_execute_order(blocks):
    total = 0
    success = 0
    fail = 0
    for i in range(0,1000):
        try:
            random.shuffle(blocks)
            assert sorted(blocks) == ['a', 'b', 'c', 'd', 'e', 'f', 'q']
            success += 1
        except AssertionError:
            fail += 1
        total += 1
    print("Success: {0}\nFail: {1}\nTotal: {2}({3}%)".format(success, fail, total,100.0* success/total))

def execute_tree(tree):
    pass

def execute_block(block, local_dict):
    pass

def parse_file(input_text):
    current_group = ""
    group_id = ""
    parsing_group = False
    blocks = {}
    for line in input_text:
        if line[0:3] == "###":
            if parsing_group == False:
                current_group = ""
                group_id = line[3:].strip()
                parsing_group = True
            elif parsing_group == True: # This indicates we've hit the next "block"
                blocks = [*process_block(group_id, current_group), *blocks]
                current_group = ""
                group_id = line[3:].strip()
        else:
            if parsing_group == True:
                current_group += line
    blocks = [*process_block(group_id, current_group), *blocks]
    determine_execute_order(blocks)

if __name__ == "__main__":
    with open("test.py", "r") as file:
        # Just for comparison
        file_contents = file.readlines()
        print(ast.dump(ast.parse("".join(file_contents)), indent=4))
        parse_file(file_contents)
