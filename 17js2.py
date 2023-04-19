import js2py   #JavaScript functions and methods from your Python code

js_code = '''
function add(x, y) {
    return x + y;
}
'''
result = js2py.eval_js(js_code + 'add(2, 3);')

print(result)
# ======================================================

add = js2py.eval_js('function add(a, b) {return a + b}')
print(add(1,2))
print(add(1, 2)+3)
print(add('5', 2),'3')
print(add('5', 2,3))



