# assignment02-bankholdiays.py
# Programming for Data Analytics - Assignment 02
# Bank holidays in Northern Ireland (example for the year 2025)

"""
This program prints:
1. All 2025 bank holidays in Northern Ireland.
2. The holidays that are unique to Northern Ireland
   (do not occur elsewhere in the UK).
"""

# 1. Bank holidays in Northern Ireland for 2025
#    (Name, Date)
ni_bank_holidays_2025 = [
    ("New Year's Day", "Wednesday 1 January 2025"),
    ("St Patrick's Day", "Monday 17 March 2025"),
    ("Good Friday", "Friday 18 April 2025"),
    ("Easter Monday", "Monday 21 April 2025"),
    ("Early May bank holiday", "Monday 5 May 2025"),
    ("Spring bank holiday", "Monday 26 May 2025"),
    ("Battle of the Boyne (Orangemen's Day)", "Saturday 12 July 2025"),
    ("Battle of the Boyne (substitute day)", "Monday 14 July 2025"),
    ("Summer bank holiday", "Monday 25 August 2025"),
    ("Christmas Day", "Thursday 25 December 2025"),
    ("Boxing Day", "Friday 26 December 2025"),
]

print("Bank holidays in Northern Ireland (2025):")
for name, date in ni_bank_holidays_2025:
    print(f"- {date}: {name}")

# 2. Names of bank holidays in England and Wales (2025)
england_wales_holiday_names = {
    "New Year's Day",
    "Good Friday",
    "Easter Monday",
    "Early May bank holiday",
    "Spring bank holiday",
    "Summer bank holiday",
    "Christmas Day",
    "Boxing Day",
}

# 3. Names of bank holidays in Scotland (2025)
scotland_holiday_names = {
    "New Year's Day",
    "2nd January",
    "Good Friday",
    "Early May bank holiday",
    "Spring bank holiday",
    "Summer bank holiday",
    "St Andrew's Day",
    "Christmas Day",
    "Boxing Day",
}

# Combine the holidays that happen elsewhere in the UK
other_uk_holiday_names = england_wales_holiday_names.union(scotland_holiday_names)

# 4. Work out which Northern Ireland holidays are unique
unique_ni_holidays = []

for name, date in ni_bank_holidays_2025:
    # If the name is not in the other UK holidays, it is unique to NI
    if name not in other_uk_holiday_names:
        unique_ni_holidays.append((name, date))

print()  # blank line
print("Bank holidays that are UNIQUE to Northern Ireland (2025):")
for name, date in unique_ni_holidays:
    print(f"- {date}: {name}")