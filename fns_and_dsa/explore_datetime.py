def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    display_current_datetime()


days = int(input("Enter number of days to add to the current date:"))


def calculate_future_date(days_to_add):
    from datetime import datetime, timedelta
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    calculate_future_date(days)
