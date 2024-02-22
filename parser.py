parsing_table = {
    'S': {
        '(': 'S->(S)S',
        ')': 'S->ε',
        '$': 'S->ε'
    }
}

input_string = input("Input string: ")
input_string = input_string + '$'
input_string = [*input_string]

parsing_stack = '$' + list(parsing_table.keys())[0]
parsing_stack = [*parsing_stack]

top = len(parsing_stack) - 1
x = parsing_stack[top]
a = input_string[0]

print('Parsing Stack\tInput\tActions')

while x != '$':
    action = ""
    d = ''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t"
    if x == a:
        action = "match"
        print(d + "match")
        parsing_stack.pop(top)
        input_string.pop(0)
    elif x not in list(parsing_table.keys()):
        print("--Error--")
        break
    elif parsing_table[x][a] is not None:
        action = parsing_table[x][a]
        print(d + parsing_table[x][a])
        p = parsing_table[x][a].split('->')[1]
        p = [*p]
        p.reverse()
        parsing_stack.pop(top)
        parsing_stack += p
        action = parsing_table[x][a]
        if 'ε' in parsing_stack:
            parsing_stack.remove('ε')
    else:
        print("--Error--")
        break

    top = len(parsing_stack) - 1
    x = parsing_stack[top]
    a = input_string[0]

if x == '$' and a == '$': print(''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t" + "accept")
else: print(''.join(parsing_stack) + "\t\t" + ''.join(input_string) + "\t" + "reject")
