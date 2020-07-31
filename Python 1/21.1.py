HOURLY_RATE = 15

total_hours = 0

hours_worked = int(input("How many hours did you work on day 1?: "))
total_hours += hours_worked

hours_worked = int(input("How many hours did you work on day 2?: "))
total_hours += hours_worked

hours_worked = int(input("How many hours did you work on day 3?: "))
total_hours += hours_worked

hours_worked = int(input("How many hours did you work on day 4?: "))
total_hours += hours_worked

hours_worked = int(input("How many hours did you work on day 5?: "))
total_hours += hours_worked

wages = total_hours * HOURLY_RATE

print("This week you earned: ${}".format(wages))
