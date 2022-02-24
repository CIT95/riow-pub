
# Ask user for their weight, type of activity and duration
# Allow user to input as many activities as they want and once complete
# calculate estimates calories burned
# Program will be limited to 4 activites and lbs of 140
# Calories will be calculated based on this chart:
# https://www.infofit.ca/calorie-burn-chart/

# Create list of dictionary to hold data
# [
# {
#   "BasketBall": 60
# },
# {
#   "Housework": 10
# }
# ]

tracking = []

cal_activity_weight = {
    "basketball": 161,
    "housework": 126,
    "weight_training": 175,
    "backpacking": 182
}


def determine_cal_burned(mins, activity):
    time = mins / 30
    cal_burned = int(cal_activity_weight[activity] * time)
    new_entry = {
        activity: cal_burned,
    }
    tracking.append(new_entry)
    return cal_burned


def get_user_input():
    for activity in cal_activity_weight:
        print(activity)
    activity = input("Select an activity? ---> ")
    mins = int(input(f"How many minutes did you {activity}"))
    cal_burned = determine_cal_burned(mins, activity)
    print(f"Calories burned {cal_burned} entered")


enter_activites = True

while enter_activites:
    get_user_input()
    enter_more = True
    while enter_more:
        user_input = input("Do you want to enter another"
                           "excerise? y or n  --->")
        if(user_input == 'n'):
            enter_more = False
            enter_activites = False
        else:
            get_user_input()

    # https://stackoverflow.com/questions/52889202/python-sum-of-certain-values-of-a-dictionary/52889317
    total_calories = 0
    for entry in tracking:
        for k, v in entry.items():
            print(f"{k} burned {v} calories")
            total_calories += v
    print(f"Total Calories burned = {total_calories}")
