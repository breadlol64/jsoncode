json_code = {
    "main": [
        {
            "type": "call",
            "id": "print",
            "args": {
                "text": "Hello world"
            }
        },
        {
            "type": "call",
            "id": "print",
            "args": {
                "text": "Bye world"
            }
        },
        {
            "type": "var",
            "name": "a",
            "value": "sjdhkjdhlajd"
        },
        {
            "type": "call",
            "id": "print",
            "args": {
                "text": "var_a"
            }
        },
    ]
}

_vars = []

main_fun = json_code['main']
print(main_fun)
code_stack = [statement['type'] for statement in main_fun]
print(code_stack)

# code interpreting
print("-----output-----")
current_index = 0
for stmt_type in code_stack:
    if stmt_type == "call":
        if main_fun[current_index]['id'] == "print":
            if main_fun[current_index]["args"]["text"].startswith("var_"):
                for _var in _vars:
                    if _var["name"] == main_fun[current_index]["args"]["text"].replace("var_", ""):
                        print(_var["value"])
            else:
                print(main_fun[current_index]["args"]["text"])
    if stmt_type == "var":
        _vars.append(main_fun[current_index])
    current_index += 1
print("----------------")

print(_vars)
