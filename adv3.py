def deco_func(origin_func):
    def wrapper_func(*args,**kwargsk):
        print('wrapper func executed b4 {}'.format(origin_func.__name__))
        print("yes")
        return origin_func(*args,**kwargsk)
    return wrapper_func
@deco_func
def display():
    print("Hello")
display()
@deco_func
def info(name,age):

    print('name of the emp is {} and his age  {}'.format(name,age))
info("bunny",22)
