import sys


def expand_field(field, min_val, max_val):
    if field == '*':
        return list(range(min_val, max_val + 1))
    elif ',' in field:
        return [int(val) for val in field.split(',') if min_val <= int(val) <= max_val]
    elif '-' in field:
        start, end = map(int, field.split('-'))
        return list(range(start, end + 1))
    elif '/' in field:
        step = int(field.split('/')[1])
        return list(range(min_val, max_val + 1, step))
    elif field in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
        # Handle days of the week
        days_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        return [days_of_week.index(field)]
    else:
        try:
            value = int(field)
            if min_val <= value <= max_val:
                return [value]
        except ValueError:
            pass
    return []

def parse_cron_string(cron_string):
    fields = cron_string.split()
    if len(fields) != 6:
        return "Invalid cron string format. Please provide a valid cron string."

    minute, hour, day_of_month, month, day_of_week, command = fields

    minute_values = expand_field(minute, 0, 59)
    hour_values = expand_field(hour, 0, 23)
    day_of_month = expand_field(day_of_month , 0,31)
    month = expand_field(month , 0 , 12)
    day_of_week_values = expand_field(day_of_week, 0, 6)  # 0-6 correspond to SUN-SAT

    return {
        "minute": minute_values,
        "hour": hour_values,
        "day of month" : day_of_month,
        "month" : month,
        "day of week": day_of_week_values,
        "command": command,
    }

# cron_string = "20 8 ? * 2L /usr/bin/find"
# #cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"
# parsed_result = parse_cron_string(cron_string)

# if isinstance(parsed_result, dict):
#     for field, values in parsed_result.items():
#         print(f"{field.ljust(14)} {' '.join(map(str, values))}")
# else:
#     print("Error:", parsed_result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_program.py 'cron_string'")
        sys.exit(1)

    cron_string = sys.argv[1]
    parsed_result = parse_cron_string(cron_string)

    if isinstance(parsed_result, dict):
        for field, values in parsed_result.items():
            print(f"{field.ljust(14)} {' '.join(map(str, values))}")
    else:
        print("Error:", parsed_result)