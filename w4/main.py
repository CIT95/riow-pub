import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in days:
    morning_list = 'Make and Drink Coffee,'
    morning_message = ''
    available_time = 0
    time_before_gym = 0
    current_time = random.choice(['6', '7', '8'])
    my_turn_to_drive = random.randint(0, 1)
    print(f'Today is {day}')
    print('Current Time is ' + current_time)
    gym_class_time = int(input('Which Gym class are going to today? -->'))
    unplanned_event = False
    time_before_gym = gym_class_time - int(current_time)
    if my_turn_to_drive == 0:
        available_time = time_before_gym - 0.25
        print(f'You are driving')
    else:
        available_time = time_before_gym - 0.15
        print(f'You are getting a drive')
    print('available time is ' + str(available_time))

    if(unplanned_event):
        morning_list += 'Check Time'
        morning_message = 'Unplanned event happen, just get back on \
                           track tomorrow'
    elif available_time >= 1.5:
        morning_list += 'Mediate, Get Morning Sun, Make Green Drink'
        morning_message = 'Love getting up early!'
    elif available_time >= 0.8 and available_time < 1.4:
        morning_list += 'Mediate, Get Morning Sun, Make Green Drink'
        morning_message = 'Love getting up early!'
    elif available_time >= 0.7 and available_time <= 1.4:
        morning_list += 'Mediate, Get Morning Sun'
        morning_message = 'That green drink will taste so good after \
                           the workout!'
    elif available_time < 0:
        morning_message = 'Stuff happens!'
    else:
        morning_message = 'Not sure you are going to gym today'

    print(morning_list)
    print(morning_message)
