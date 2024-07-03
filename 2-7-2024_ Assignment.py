from datetime import datetime

def find_day_in_week(date_str: str) -> str:

    date = datetime.strptime(date_str, "%Y-%m-%d")

    day = date.strftime("%A")

    return day

date_str = "2003-05-13"

print(find_day_in_week(date_str))
