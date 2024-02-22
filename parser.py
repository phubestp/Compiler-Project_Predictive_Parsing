# parsing table 
# { 'non-terminal': {'terminal' : production... } ,... }
parsing_table = {
    'S': {
        '(': 'S->(S)S',
        ')': 'S->ε',
        '$': 'S->ε'
    }
}

input_string = input("Input string: ")
input_string = input_string + '$'
input_string = [*input_string] # convert string to list

parsing_stack = '$' + list(parsing_table.keys())[0] # put initial grammar
parsing_stack = [*parsing_stack] # convert string to list

top = len(parsing_stack) - 1
# following algorithm, x is top of parsing_stack and a is the first input symbol
x = parsing_stack[top]
a = input_string[0]

# header
print('Parsing Stack\tInput\tActions')

while x != '$':

    # row formatting
    d = ''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t"

    # if top of parsing_stack and input is match, pop both from stacks
    if x == a:
        print(d + "match")
        parsing_stack.pop(top)
        input_string.pop(0)

    # if x is terminal, it's error
    elif x not in list(parsing_table.keys()):
        print("--Error--")
        break

    # if it has production M[x,a], put reverse production to the parsing stack
    elif parsing_table[x][a] is not None:
        print(d + parsing_table[x][a])
        p = parsing_table[x][a].split('->')[1] # split -> from production
        p = [*p] # convert string to list
        p.reverse()
        parsing_stack.pop(top)
        parsing_stack += p # put reverse produciton
        if 'ε' in parsing_stack:
            parsing_stack.remove('ε')

    # if it not have production M[x,a], it's error too
    else:
        print("--Error--")
        break

    # update top, x and a
    top = len(parsing_stack) - 1
    x = parsing_stack[top]
    a = input_string[0]

# if x and a is $ => accept 
if x == '$' and a == '$': 
    print(''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t" + "accept")
else: 
    print(''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t" + "reject")
