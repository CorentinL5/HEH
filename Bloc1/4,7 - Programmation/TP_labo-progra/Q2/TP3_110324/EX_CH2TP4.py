class WeekDayError(Exception):
    def __init__(self, message="Invalid weekday provided"):
        super().__init__(message)

class Weeker:
    def __init__(self, day):
        valid_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if day not in valid_days:
            raise WeekDayError(f"Invalid weekday '{day}' provided")
        self._day = day

    def __str__(self):
        return self._day

    def add_days(self, n):
        days_in_week = 7
        days_to_add = n % days_in_week
        days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        current_day_index = days_order.index(self._day)
        new_day_index = (current_day_index + days_to_add) % days_in_week

        self._day = days_order[new_day_index]

    def subtract_days(self, n):
        self.add_days(-n)

weekday = Weeker('Mon')
print(weekday)
weekday.add_days(15)
print(weekday)
weekday.subtract_days(23)
print(weekday)
weekday = Weeker('Monday')  # This will raise a WeekDayError since 'Monday' is not an acceptable argument