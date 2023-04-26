def main():
    # Get user input
    item = input("Date: ")
    if item.find(",") == -1:
        year_month_day = split_by_slash(item)
    else:
        year_month_day = split_by_space(item)
    year = year_month_day[0]
    month = year_month_day[1]
    day = year_month_day [2]

    date_by_slash = split_by_dash(year, month, day)
    print(date_by_slash)


def split_by_slash(date):
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    # check if month is in between 1 and 12 and day between 1 and 31
    if (month) >= 1 and (month) <= 12 and (day) >= 1 and (day)<= 31:
        pass
    else:
        return year, month, day


def split_by_space(date):
    # list of months , given
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # remove comma from a date
    date = date.replace(",","")
    # split the date by space
    old_month, day, year = date.split(" ")
    day = int(day)
    year = int(year)
    # find the nomber of month
    for i in range(len(months)):
        if old_month == months[i]:
            month = i + 1
    return year, month, day

def split_by_dash(year, month, day):
    return(f"{year}-{(month):02}-{(day):02}")


main()