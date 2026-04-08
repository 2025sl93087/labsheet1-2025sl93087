def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def sub(a,b):
    return a-b

def div(a,b):
    if b==0:
	return None
    return a/b

if __name__ == "__main__":
    assert  add(2,3) == 5
    print("All tests passed")
