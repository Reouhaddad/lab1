f_call = False 
def add(x, y):
    global f_call
    f_call = True
    return x + y

def subtract(x, y):
    global f_call
    f_call = True
    return x - y
