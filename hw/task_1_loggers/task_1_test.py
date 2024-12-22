import numbers

import task_1_logs as logs

def test_method(a, b):
    if b == 0.0:
        logs.log_warns.warning("Can't divide by zero")
        # raise RuntimeError("Can't divide by 0")
    elif not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        logs.log_warns.error("Type error")
    else:
        message = f'returned {a / b}'
        logs.log_info.debug(message)
        print(message)
        # return a / b

test_method(2, 4)
test_method("A", 4.0)
test_method(1.0, 0.0)

