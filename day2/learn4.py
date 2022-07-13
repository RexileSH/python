from math import remainder


age= input("what is your current age? ")
remaind= 90 -int(age)
remaind_in_day=remaind*360
remaind_in_month=remaind*12
remaind_in_week=remaind*52

print(f"reminder in day is {remaind_in_day}, reminder in month is {remaind_in_month}, reminder in year {remaind}, reminder in week {remaind_in_week}")
