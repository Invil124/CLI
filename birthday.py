import calendar
import datetime

test_list_users = [
    {"Adrey":datetime.date(1979,9,24)},
    {"Prikolist":datetime.date(1999,9,25)},
    {"Dryg_prekolist":datetime.date(985,9,28)},
    {"Adren23":datetime.date(2000,9,27)}]


def get_birthday_per_week(users):
    obj = calendar.Calendar()

    current_datetime = datetime.datetime.now()

    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day
    
    birthday_dict = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}
    callendar_of_month = obj.monthdayscalendar(year = current_year, month = current_month)

    for weeks in callendar_of_month:
        if current_day in weeks:
            index_of_curent_week = callendar_of_month.index(weeks)
            break
    
     
    current_week = callendar_of_month[index_of_curent_week]

    next_week = callendar_of_month[index_of_curent_week+1]


    for user in users:
        for name, date in user.items():
            if date.month == current_month:
                if date.day in current_week[5:]:
                    birthday_dict["Monday"].append(name)
                    
                elif date.day in next_week[0:5]:
                    if date.day == next_week[0]:
                        birthday_dict["Monday"].append(name)

                    elif date.day == next_week[1]:
                        birthday_dict["Tuesday"].append(name)

                    elif date.day == next_week[2]:
                        birthday_dict["Wednesday"].append(name)

                    elif date.day == next_week[3]:
                        birthday_dict["Thursday"].append(name)

                    elif date.day == next_week[4]:
                        birthday_dict["Friday"].append(name)
    
    for key,velue in birthday_dict.items():
        if len(velue) != 0:
            names= ", ".join(velue)
            print(f"{key}: {names}")

                

get_birthday_per_week(test_list_users)