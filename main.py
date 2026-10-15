# asks user for hourly wage, worked hours in the current pay period, and projected hours
pay = input("what's your hourly pay?")
worked_hours = input("how many hours did you work in the current pay period?")
future_hours = input("how many more hours do you think you'll work in this pay period?")
pay = float(pay)
worked_hours = float(worked_hours)
future_hours = float(future_hours)
current_earned_pay = pay * worked_hours
print (f"earned so far: ${current_earned_pay:.2f}")
total_hours = worked_hours + future_hours
projected_pay = pay * total_hours
print (f"projected earnings: ${projected_pay:.2f}")