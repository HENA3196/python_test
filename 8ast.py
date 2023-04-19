import ast  #In Python, the ast (Abstract Syntax Tree) module is used to parse Python code into an abstract syntax tree. The abstract syntax tree represents the code's syntactic structure in a hierarchical form that can be easily traversed and analyzed.

def my_func(x, y):
    return x + y

ast_obj = ast.parse('def my_func(x, y):\n    return x + y\n')

print(ast_obj)

print(my_func(10,23))  