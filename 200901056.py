import re
import ast
def module_1(targetexpression):
 token_regex=r"\d+|[a-zA-Z]+|."
 answer= re.findall(token_regex,targetexpression)
 print(answer)
def create_tree(expression):
    tree = ast.parse(expression)
    print(tree)
    print(ast.dump(tree, indent=4))

exp=("a + (b * c)")
module_1(exp)
create_tree(exp)