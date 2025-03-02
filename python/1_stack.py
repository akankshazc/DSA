# Stack implementation in python

# create a stack
def create_stack():
    stack = []
    return stack

# check if the stack is empty


def is_empty(stack):
    return len(stack) == 0

# push an element into the stack


def push(stack, item):
    stack.append(item)
    print("pushed to stack " + item)

# pop an element from the stack


def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    return stack.pop()


# test the stack
if __name__ == "__main__":
    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    print(stack)
    print("popped from stack " + pop(stack))
    print("stack after popping an element " + str(stack))
