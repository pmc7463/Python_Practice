import datetime

today = datetime.date.today()
target_date = datetime.date(2022, 12, 31)

d_day = target_date - today
print(f"d-day : {d_day.days}")

start_date = datetime.date(2022, 11, 6)
target_date1 = datetime.date(2022, 12, 31)

d_day1 = target_date1 - start_date
print(f"d-day : {d_day.days}")

start_date2 = datetime.datetime.today()
d_day2 = 55

target_date2 = start_date2 + datetime.timedelta(d_day2)

print(f"start date2 : {start_date2}")
print(f"d-day : {d_day2}")
print(f"target date : {target_date2}")
