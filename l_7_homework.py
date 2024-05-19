import time

def measure_time(func):
    def wrapper():
        start = time.time()
        result_func = func()
        end = time.time()
        total_time = start - end
        return result_func, total_time
    return wrapper


@measure_time
def time_delay():
    a = 1 + 1
    time.sleep(3)
    return a

print(time_delay())