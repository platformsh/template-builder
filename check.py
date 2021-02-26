

def checkstring(my_string):
    if '^' not in my_string:
        return '^{}'.format(my_string)
    else:
        return my_string

examples = [
    '^5.6.2',
    '5.6.0'
]

for x in examples:
    print(checkstring(x))