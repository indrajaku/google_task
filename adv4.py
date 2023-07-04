import time
def calculate_executionTM(origin_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = origin_func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"function name '{origin_func.__name__}'took {execution_time:.4f} second to execute.")
        return result
    return wrapper
@calculate_executionTM
def my_function(a,b):
    print(a/b)
    print("hi")

my_function(5,2)

