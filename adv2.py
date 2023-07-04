def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function
def demo():
    print("am an answer")

div = decorator_function(demo)

div()












