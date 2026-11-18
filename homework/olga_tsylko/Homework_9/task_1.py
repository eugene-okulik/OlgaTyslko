import datetime

test_date = "Jan 15, 2023 - 12:05:33"
my_date = datetime.datetime.strptime(test_date, "%b %d, %Y - %H:%M:%S")
print(my_date.strftime("%B"))
print(my_date.strftime("%d.%m.%Y, %H:%M"))
