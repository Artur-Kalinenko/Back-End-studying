n = int(input("Enter the number of minutes: "))

days = n % 1440
hours = days // 60
minutes = days % 60

print(hours, minutes)
