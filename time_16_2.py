# Phyllis Torres
# 16.2 Time Assignment
# Due 11/10/2016

print('16.2 Time Assignment\n')
print('Phyllis Torres\n\n')

# create a time class
# noinspection PyClassHasNoInit
class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

# create function to convert time to an integer
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

# create function to determine if time1 follows time1 chronologically
def is_after(t1, t2):
    seconds1 = time_to_int(t1)
    seconds2 = time_to_int(t2)
    difference = seconds2 - seconds1
    return [" follows ", " does not follow "][difference >= 0]

# create time1 object and populate the hour, minute, and second fields
# this object will be evaluated to determine if it follows time2
time1 = Time()
time1.hour = 9
time1.minute = 01
time1.second = 10

# create time2 object and populate the hour, minute, and second fields
# this object will be evaluated to determine if it comes before time1
time2 = Time()
time2.hour = 10
time2.minute = 01
time2.second = 20

# convert time1 to seconds
time1.seconds = time_to_int(time1)

time2.seconds = time_to_int(time2)

result = is_after(time1, time2)

print ('Time 1 = ' + '%.2d:%.2d:%2d' % (time1.hour, time1.minute, time1.second))
print ('\nTime 2 = ' + '%.2d:%.2d:%2d' % (time2.hour, time2.minute, time2.second))
print ('\n%.2d:%.2d:%.2d' % (time1.hour, time1.minute, time1.second) + result + '%.2d:%.2d:%.2d' % (time2.hour, time2.minute, time2.second) + ' chronologically.')




