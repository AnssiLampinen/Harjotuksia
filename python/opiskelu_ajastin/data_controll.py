import time
import datetime
import studyin_time_data as std

local_time = time.localtime()
date = datetime.date(local_time[0], local_time[1], local_time[2]).isocalendar()



# year = 2023
# week = 14
# weekday = 1

# print(date)
# print(year, week, weekday)

def get_study_time(year, week, weekday):
    """
    Returns the time studied during given day.
    """

    if week in std.studying_time_data[year].keys():
        if weekday in std.studying_time_data[year][week].keys():
            study_time = (std.studying_time_data[year][week][weekday])
        else:
            study_time = 0
    else:
        study_time = 0
    return study_time

def modify_study_time(year, week, weekday, added_study_time):
    """
    Adds added_study_time amount of time to the total study time of given day.
    """
    while True:
        if year in std.studying_time_data.keys():
            if week in std.studying_time_data[year].keys()
                if weekday in std.studying_time_data[year][week].keys()
                    study_time = get_study_time(year, week, weekday) + added_study_time
                    print(study_time)
                    studyin_time_data = std.studying_time_data[year][week].copy()
                    print(std.studying_time_data)
                    print(studyin_time_data)
                    studyin_time_data.update({weekday:study_time})
                    print(studyin_time_data)
                    f = open(r"C:\Users\anssi\Documents\GitHub\Harjotuksia\python\opiskelu_ajastin\studyin_time_data.py", "w")
                    f.write("studying_time_data = {" + str(year) + ":{" + str(week) + ":" + str(studyin_time_data) + "}}")
                    f.close()
                    break
                else:
                    ""
            else:
                ""
        else:
            ""


    

modify_study_time(2023, 15, 0, 2)
# print(get_study_time(2023, 14, 5))









# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# print(weekdays[date[6]], date[2], months[date[1]], date[0])