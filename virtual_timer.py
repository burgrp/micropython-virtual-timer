from machine import Timer

next_id = -1

def new():
    global next_id
    id = next_id
    next_id = next_id - 1
    return Timer(id)
