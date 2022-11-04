def seconds_since_midnight():
    hour_in_seconds = hours * 3600
    minute_in_seconds = minutes * 60
    return f'Your time {hours}hours: {minutes}minutes: {seconds}seconds converted to seconds is' \
           f' equal to {hour_in_seconds + minute_in_seconds + seconds} seconds'


hours = int(input("Enter the hours you want to convert: "))
minutes = int(input("Enter the minutes you want to convert: "))
seconds = int(input("Enter the seconds you want to convert: "))

print(seconds_since_midnight())


# def seconds_since_midnight(hour, minute, second):
#     hour_in_seconds = hour * 3600
#     minute_in_seconds = minute * 60
#     return f'Your time {hour}hours: {minute}minutes: {second}seconds converted to seconds is' \
#            f' equal to {hour_in_seconds + minute_in_seconds + second} seconds'
#
#
# print(seconds_since_midnight(8, 38, 00))
