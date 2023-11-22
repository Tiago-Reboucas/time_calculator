# Time Calculator

Full code run with examples test can be found in: https://replit.com/@tiagoreboucas90/boilerplate-time-calculator#time_calculator.py

There is a function named `add_time()` that takes in two required parameters and one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM);
- a duration time that indicates the number of hours and minutes;
- (optional) a starting day of the week, case insensitive.

The function add the duration time to the start time and return the result.

If the result will be the next day, it shows `(next day)` after the time. If the result will be more than one day later, it shows `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. The day of the week in the output appear after the time and before the number of days later.


Below are some examples of different cases the function handles.
```text
add_time("3:00 PM", "3:10")
    Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
    Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
    Returns: 12:03 PM

add_time("10:10 PM", "3:30")
    Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
    Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
    Returns: 7:42 AM (9 days later)
```

It is assumed that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

## Testing
- If you chose to open in [replit](https://replit.com/@tiagoreboucas90/boilerplate-time-calculator#time_calculator.py), the code is writen in `time_calculator.py`. For development, you can use `main.py` to test the `add_time()` function. Click the "run" button and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
