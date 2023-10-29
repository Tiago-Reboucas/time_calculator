

def add_time(start: str, duration: str, day=""):
    #Parsing data
    s_time = start.split()[0]
    s_period = start.split()[1].upper()

    s_hour = int(s_time.split(":")[0])
    s_min = int(s_time.split(":")[1])
    s_time_float = s_hour + s_min / 60

    a_hour = int(duration.split(":")[0])
    a_min = int(duration.split(":")[1])

    # Calculations
    def add_0(time: str):
        if len(time) < 2: return "0" + time
        return time

    # Minutes
    add_hour = 0
    f_min = s_min + a_min
    if f_min >= 60:
        f_min = str(f_min - 60)
        add_hour = 1
    else:
        f_min = str(f_min)
        
    f_min = add_0(f_min)

    # Hours
    hours = s_hour + a_hour + add_hour
    rest_hour = hours % 12
    f_hour = str(rest_hour)
    f_time_float = int(f_hour) + int(f_min)/60

    f_hour = "12" if f_hour == "0" else f_hour


    mult = hours // 12
    if mult % 2 == 0: f_period = s_period
    else:
        f_period = "PM" if s_period == "AM" else "AM"

    # Days
    add_day = 0
    if s_period == "PM" and f_period == "AM": 
        add_day = 1
    elif s_period == f_period and f_time_float < s_time_float: 
        add_day = 1
    
    mult_day = a_hour // 24
    days = add_day + mult_day

    rest_days = days % 7

    new_time = f_hour + ":" + f_min + " " + f_period

    if day != "":
        week_days = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }
        s_day_int = [i for i in week_days if week_days[i] == day.capitalize()][0]

        f_day = (rest_days + s_day_int) % 7
        f_day = week_days[f_day]
        new_time += ", " + f_day
    
    if days > 0:
        if days == 1: 
            new_time += " (next day)"
        else:
            new_time += f" ({days} days later)"

    return new_time

print(add_time("3:00 PM", "3:10"))
print("Returns: 6:10 PM\n")

print(add_time("11:30 AM", "2:32", "Monday"))
print("Returns: 2:02 PM, Monday\n")

print(add_time("11:43 AM", "00:20"))
print("Returns: 12:03 PM\n")

print(add_time("10:10 PM", "3:30"))
print("Returns: 1:40 AM (next day)\n")

print(add_time("11:43 PM", "24:20", "tueSday"))
print("Returns: 12:03 AM, Thursday (2 days later)\n")

print(add_time("6:30 PM", "205:12"))
print("Returns: 7:42 AM (9 days later)\n")

print(add_time("8:16 PM", "466:02", "tuesday"))
print("Returns: 6:18 AM, Monday (20 days later)\n")

print(add_time("2:59 AM", "24:00", "saturDay"))
print("Returns: 2:59 AM, Sunday (next day)\n")