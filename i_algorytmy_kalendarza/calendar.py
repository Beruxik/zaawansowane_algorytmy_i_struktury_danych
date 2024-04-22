def leap_year(year):
    if year % 400 == 0:
        return True
    
    if year % 4 == 0 and year % 100 != 0:
        return True

    return False

year = int(input('Put year: '))
print(f'{year} is leap year' if leap_year(year) else f'{year} is not leap year')