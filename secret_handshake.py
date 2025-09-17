ACTIONS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    actions = []

    for i in range(4):
        if binary_str[-(i+1)] == '1':
            actions.append(ACTIONS[i])

    if binary_str[-5] == '1':
        actions.reverse()

    return actions
