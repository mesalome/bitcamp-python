from datetime import date
import inflect
import sys

def main():
    try:
        userInput = input("Input date in YYYY-MM-DD format: ")
        print(read_numbers(days_to_minutes(days_passed(userInput))), "minutes")
    except Exception:
        sys.exit("Invalid date")

def days_passed(customDate, today=date.today()):
    userDateFormat = date.fromisoformat(customDate)
    daysPassed = abs(today-userDateFormat).days
    return daysPassed

def days_to_minutes(days):
    return days*24*60

def read_numbers(number):
    return inflect.engine().number_to_words(f"{number}", andword="")


if __name__ == "__main__":
    main()