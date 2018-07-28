#coding:utf-8

months = [
    'Januray',
    'February',
    'March',
    'April',
    'May',
    'june',
    'july',
    'August',
    'September',
    'Otcober',
    'November',
    'December'

]

endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
print endings
year = raw_input("Year：")
month = raw_input("Month(1-12): ")
day = raw_input("Day(1-31)")

month_number = int(month)
day_number = int(day)
month_day = months[month_number -1]
ordinal = day+endings[day_number -1]

print month_day+' ' +ordinal+'.'+year